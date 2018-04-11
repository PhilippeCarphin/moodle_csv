import csv
import logging

class Configs:
    DIR = 'test_dir'
    # Warning, do not put '.csv', it will be put automatically because it is
    # mandatory
    ORIGINAL_CORRECTION_FILE = 'correction_tp4'
    MOODLE_CORRECTION_FILE = 'moodle.csv'
    REQUISITES_FILE = 'requis.json'


""" This part specifies things in regards to correction """
class Correction:
    REQUIS = 0
    POINTS = 1
    POIDS = 2
    DESCRIPTION = 3
    COMMENTAIRE = 4
    HEADER = ['Requis', 'Points', 'Points max', 'Description', 'Commentaire']


""" This part specifies things in regards to the accumulation of grades into
the CSV file provided by moodle """
class Moodle:
    IDENTIFIANT = 0
    NOM_COMPLET = 1
    MATRICULE = 2
    COURRIEL = 3
    STATUT = 4
    GROUPE = 5
    NOTE = 6
    NOTE_MAX = 7
    MODIF_PERMISE = 8
    DERNIERE_MODIF_TRAVAIL = 9
    DERNIERE_MODIF_NOTE = 10
    COMMENTAIRE = 11


""" CSV dialect specification for the project """
csv_dialect = csv.Dialect
csv_dialect.delimiter = ','
csv_dialect.quotechar = '"'
csv_dialect.escapechar = '\\'
csv_dialect.quoting = csv.QUOTE_ALL
csv_dialect.lineterminator = '\r\n'
csv_dialect.skipinitialspace = True

""" Logger instance for project """
logging.basicConfig(filename='output.log', filemode='w')
console = logging.StreamHandler()
logger = logging.getLogger('Moodle helper')
logger.addHandler(console)