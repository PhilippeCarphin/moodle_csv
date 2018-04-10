import csv
import os
from globals import Moodle, csv_dialect, logger
from groupinfo import get_totals, load_requisites

def skip_row(row):
    """ Determine whether to skip a row, right now, this function only
    says to skip the header row, but it will maybe skip the rows when there
    is nothing handed in."""
    if row[Moodle.IDENTIFIANT].endswith('Identifiant'):
        return True
    if 'bidon' in row[Moodle.GROUPE]:
        return True
    if 'Pas de travail remis' in row[Moodle.STATUT]:
        return True

    return False

def get_group_info(group):
    """ Construct the path of the CSV file for that group and call get_totals """
    total = 'NOT_FOUND'
    feedback = 'NOT_FOUND'
    filename = Moodle.CORRECTION_FILE_PREFIX \
           + group.replace(' ', '_') \
           + Moodle.CORRECTION_FILE_POSTFIX
    path = os.path.join(
            Moodle.CORRECTION_DIR,
            group.replace(' ', '_'),
            filename
    )

    try:
        return get_totals(path, load_requisites('./requis.json'))
    except FileNotFoundError:
        pass

    return {'total': total, 'feedback': feedback}


if __name__ == '__main__':
    with open(Moodle.CSV_FILE, 'r', encoding='UTF-8') as csv_in:
        reader = csv.reader(
                csv_in,
                dialect=csv_dialect,
        )
        with open('out.csv', 'w', encoding='UTF-8') as csv_out:
            writer = csv.writer(
                    csv_out,
                    dialect=csv_dialect
            )
            for row in reader:
                new_row = row
                if skip_row(row):
                    new_row = row
                else:
                    group = row[Moodle.GROUPE]
                    group_info = get_group_info(group)
                    new_row = row[:Moodle.NOTE] \
                              + [group_info['total']] \
                              + row[Moodle.NOTE+1:Moodle.COMMENTAIRE] \
                              + [group_info['feedback']]
                writer.writerow(new_row)
