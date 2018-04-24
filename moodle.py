import csv
from globals import Moodle, csv_dialect, logger, Configs


def fill_in_moodle_sheet(filename, outfilename, info_getter):
    """
    Applies a transformation to all the rows of a CSV file
    Info_getter is a function that takes a group and returns
    a dictionary with keys 'total' and 'feedback'
    """
    with open(filename, 'r', encoding='UTF-8') as csv_in, \
            open(outfilename, 'w', encoding='UTF-8') as csv_out:

        reader = csv.reader(csv_in, dialect=csv_dialect)
        writer = csv.writer(csv_out, dialect=csv_dialect)
        for row in reader:
            new_row = row
            try:
                new_row = fill_in_row(row, info_getter)
            except Exception as e:
                logger.warning("Could not fill in row " + str(row) + str(e))

            writer.writerow(new_row)


def fill_in_row(row, info_getter):
    """
    Fills in the grade column and feedback column
    Info_getter is a function that takes a group and returns
    a dictionary with keys 'total' and 'feedback'
    """
    new_row = row
    if skip_row(row):
        new_row = row
    else:
        group_info = info_getter(row[Moodle.GROUPE])
        new_row[Moodle.NOTE] = group_info['total']
        new_row[Moodle.COMMENTAIRE] = group_info['feedback']
    return new_row


def skip_row(row):
    """ 
    Determine whether to skip a row
    """
    if row[Moodle.IDENTIFIANT].endswith('Identifiant'):
        return True
    if 'bidon' in row[Moodle.GROUPE]:
        return True
    if 'Pas de travail remis' in row[Moodle.STATUT]:
        return True

    return False


if __name__ == '__main__':
    import groupinfo

    fill_in_moodle_sheet(Configs.MOODLE_CORRECTION_FILE, 'out.csv', groupinfo.get_group_info)
