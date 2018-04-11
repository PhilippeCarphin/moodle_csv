import csv
import json
from globals import Correction, csv_dialect, logger

class ConsistencyError(Exception):
    pass

def load_requisites(path):
    """ Loads the json file that specifies the requisites for the
    particular assignment"""
    with open(path, 'r', encoding='UTF-8') as json_file:
        return json.loads(json_file.read())


def get_totals(file, requisites):
    """ Reads the file according and compiles the total of points
    Returns {'total': total, 'feedback': feedback}
    where total is just the sum of the points column and feedback is a
    formatted string made from the comments of individual requisites.
    On each line the requisite code is written with the comment."""
    with open(file, 'r', encoding='UTF-8') as group_csv:
        reader = csv.reader(group_csv)
        total = 0.0
        feedback = ''
        missing_data = False
        for row in reader:
            req_code = row[0]
            if req_code == Correction.HEADER[0]:
                continue
            if req_code not in requisites:
                logger.warning("CSV-JSON Inconsistency in file={}, req_code={}"
                               .format(value, file, req_code))
                raise ConsistencyError
                continue

            value = row[Correction.POINTS]
            try:
                value = float(value)
                total += value
            except:
                if row[Correction.POIDS] != '0':
                    missing_data = True
                    logger.warning("Missing points in file={}, req_code={}"
                                   .format(value, file, req_code))
            comment = row[Correction.COMMENTAIRE]
            if comment != "":
                feedback +=  "{} : {} \r\n".format(req_code, comment)
        if missing_data:
            total = 'CORRECTION_INCOMPLETE - See output.log'
    return {'total': total, 'feedback': feedback}


def make_csv(requisites_file, filename):
    """ Creates a CSV file corresponding the the requisites JSON file """
    requisites = load_requisites(requisites_file)
    with open(filename, 'w', encoding='UTF-8') as csv_out:
        writer = csv.writer(csv_out, dialect=csv_dialect)
        writer.writerow(Correction.HEADER)
        for key in requisites:
            req = requisites[key]
            row = [key, '', req['weight'], req['description'], '']
            writer.writerow(row)


if __name__ == "__main__":
    """ If this module is called as main, create the CSV file corresponding
    to the JSON file """
    make_csv('correction_tp4.csv', load_requisites('requis.json'))
