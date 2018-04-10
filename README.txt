BUT

    Automatiser certaines étapes de la correction et de la compilation de notes.

    Un fichier de correction est déposé dans tous les dossiers à corriger.

    Une fois la correction terminée les fichiers de correction individuels sont
    consultés pour pour remplir le fichier de moodle.

FICHIERS

    globals.py
        Contient les constantes qu'on pourrait vouloir configurer comme les
        numéros de colonnes dans les fichiers CSV et les noms de fichiers et
        dossiers.  En principe, tout devrait être configurable par ce fichier.

    groupinfo.py
        Code responsable de traiter les fichiers CSV individuels


    moodle.py


    init-correction-moodle.sh


    requis.json


    test_dir:

        test_dir
        ├── Groupe_01
        │   └── correction_tp4_Groupe_01.csv
        ├── Groupe_02
        │   └── correction_tp4_Groupe_02.csv
        └── Groupe_03
            └── correction_tp4_Groupe_03.csv



