BUT

    Automatiser certaines étapes de la correction et de la compilation de notes.

    Un fichier de correction est déposé dans tous les dossiers à corriger.

    Une fois la correction terminée les fichiers de correction individuels sont
    consultés pour pour remplir le fichier de moodle.


UTILISATION
    à ajuster:

        ini

FICHIERS

    globals.py
        Contient les constantes qu'on pourrait vouloir configurer comme les
        numéros de colonnes dans les fichiers CSV et les noms de fichiers et
        dossiers.  En principe, tout devrait être configurable par ce fichier.

    groupinfo.py
        Code responsable de traiter les fichiers CSV individuels.  Lorsqu'exécuté
        comme main (python3 groupinfo.py), le programme lit le fichier de requis
        requis.json et crée un fichier .csv.

        Sinon, ce fichier est utilisé comme module pour fournir des fonctions qui
        traitent les fichiers CSV de chaque groupe.  Il founit la fonction
        get_totals() qui retourne {'tota': <le total> , 'feedback': <le feedback>}

    moodle.py
        Lorsqu'exécuté comme main, le script va remplir le fichier CSV de moodle
        en allant chercher les totaux de chaque fichier individuel de chaque groupe.


    init-correction-moodle.sh
        Ce fichier doit être exécuté au début.  Il appelle groupinfo.py pour générer
        une grille de correction en .csv et en dépose une copie dans le dossier
        chaque groupe et appose le numéro du groupe au fichier pour éviter les erreurs.

        On peut ajouter des commandes dans ce fichier si on veut qu'une action soit
        répétée pour chaque groupe, comme décompresser une archive.

    requis.json


    test_dir:
        Un exemple du dossier qui aurait été téléchargé de Moodle

        test_dir
        ├── Groupe_01
        │   └── correction_tp4_Groupe_01.csv
        ├── Groupe_02
        │   └── correction_tp4_Groupe_02.csv
        └── Groupe_03
            └── correction_tp4_Groupe_03.csv



