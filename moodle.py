import csv
import os
from globals import Moodle, csv_dialect, logger, Configs
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

def group_to_file(group):
    filename = '_'.join([Configs.ORIGINAL_CORRECTION_FILE, group])
    filename += '.csv'
    path = os.path.join(Configs.DIR, group, filename)
    return path

def get_group_info(group):
    """ Construct the path of the CSV file for that group and call get_totals """
    total = 'NOT_FOUND'
    feedback = 'NOT_FOUND'
    path = group_to_file(group)

    try:
        return get_totals(path, load_requisites('./requis.json'))
    except FileNotFoundError:
        pass

    return {'total': total, 'feedback': feedback}


if __name__ == '__main__':
    with open(Configs.MOODLE_CORRECTION_FILE, 'r', encoding='UTF-8') as csv_in:
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
