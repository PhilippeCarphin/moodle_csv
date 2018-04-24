import csv
import json
from globals import Correction, Configs, csv_dialect, logger
import os


class ConsistencyError(Exception):
    pass


def group_info_factory(path_maker, file_reader):
    """
    All you have to do is supply a way of knowing which file contains
    the info for the group and a way of getting the info from the file
    """
    def group_info(group):
        """
        Construct the path of the CSV file for that group and call get_totals
        """
        total = 'NOT_FOUND'
        feedback = 'NOT_FOUND'
        path = path_maker(group)

        try:
            return file_reader(path)
        except FileNotFoundError:
            logger.warning("File not found : {}".format(path))

        return {'total': total, 'feedback': feedback}

    return group_info


def group_to_file(group):
    """
    Returns the path of the file to look at to find the group's information
    """
    filename = '_'.join([Configs.ORIGINAL_CORRECTION_FILE, group.replace(' ', '_')])
    filename += '.csv'
    path = os.path.join(Configs.DIR, group.replace(' ', '_'), filename)
    return path


def load_requisites(path):
    """ 
    Loads the json file that specifies the requisites for the
    particular assignment
    """
    with open(path, 'r', encoding='UTF-8') as json_file:
        return json.loads(json_file.read())


requisites = load_requisites('./requis.json')
requisite_list = requisites['requisite_list']


def get_group_info_internal(file):
    """
    Reads the file according and compiles the total of points
    Returns {'total': total, 'feedback': feedback}
    where total is just the sum of the points column and feedback is a
    formatted string made from the comments of individual requisites.
    On each line the requisite code is written with the comment.
    """
    error_value = {'total': 'SEE_LOG', 'feedback': 'SEE_LOG'}
    codes = map(lambda req: req['code'], requisite_list)
    with open(file, 'r', encoding='UTF-8') as group_csv:
        reader = csv.reader(group_csv)
        total = 0.0
        feedback = ''
        for row in reader:
            req_code = row[0]
            """
            Skip the header row
            """
            if req_code == Correction.HEADER[0]:
                continue

            """
            Check that req_code is valid
            """
            if req_code not in codes:
                logger.warning("CSV-JSON Inconsistency in file={}, req_code={} not in codes from JSON file"
                               .format(file, req_code))
                raise ConsistencyError

            """
            Get points and check for consistency
            """
            points = row[Correction.POINTS]
            try:
                points = float(points)
            except ValueError:
                if row[Correction.POIDS] != '0':
                    logger.warning("Missing points in file={}, req_code={}"
                                   .format(file, req_code))
                    return error_value
            weight = float(row[Correction.POIDS])
            if points > weight:
                logger.warning("Inconsistency in file={}, req_code={} : points={} greater than weight={}"
                               .format(file, req_code, points, weight))
                return error_value

            """
            Add points and comment to return value
            """
            total += points
            comment = row[Correction.COMMENTAIRE]
            if comment != "":
                feedback += "{} ({}/{}): {} \r\n".format(req_code, points, weight, comment)

    return {'total': total, 'feedback': feedback}


def make_csv(requisites_file, filename):
    """
    Creates a CSV file corresponding the the requisites JSON file
    """
    with open(filename, 'w', encoding='UTF-8') as csv_out:
        writer = csv.writer(csv_out, dialect=csv_dialect)
        writer.writerow(Correction.HEADER)
        for req in load_requisites(requisites_file)['requisite_list']:
            row = [req['code'], '', req['weight'], req['description'], '']
            writer.writerow(row)


get_group_info = group_info_factory(group_to_file, get_group_info_internal)


if __name__ == "__main__":
    """ If this module is called as main, create the CSV file corresponding
    to the JSON file """
    make_csv('requis.json', 'json_to_csv.csv')
