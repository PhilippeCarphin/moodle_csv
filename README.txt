BUT

    Automatiser certaines étapes de la correction et de la compilation de notes.

    Un fichier de correction est déposé dans tous les dossiers à corriger.

    Une fois la correction terminée les fichiers de correction individuels sont
    consultés pour pour remplir le fichier de moodle.


UTILISATION
    Avant de commencer

        Télécharger les choses

            Clôner cet entrepôt

            À la racine de l'entrepôt, télécharger les travaux et le fichier de
            notes en cliquant sur "Consulter tous les travaux remis" et dans le
            menu "Actions d'Évaluations", choisir "Télécharger tous les travaux
            remis" et ensuite choisir "télécharger le formulaire d'évaluation".

            On devrait avoir
                moodle_csv
                ├── <Dossier téléchargé de moodle> <-- Configs.DIR
                │   ├── Groupe_01
                │   ├── Groupe_02
                │   └── Groupe_03
                ├── <Formulaire d'évaluation> <-- Configs.MOODLE_CORRECTION_FILE
                ├── README.txt
                ├── globals.py
                ├── group.py
                ├── init-correction.py
                ├── initial-operations.sh
                ├── requis.json <-- Configs.REQUISITES_FILE
                └── moodle.py

        Faire un fichier de requis:

            Suivre l'exemple pour faire un fichier de requis pour spécifier
            les points attribués à chaque partie du travail.  Fiez vous au
            fichier requis.json.  Un tel fichier pourrait être déjà fourni.

        Ajuster les configurations

            Dans le fichier globals.py, ajuster les attributs de la classe
            Configs.

        Optionnel: Définir des opérations à exécuter dans chaque dossier

            Optionnellement, le fichier initial-operations.py peut être modifié
            pour ajouter des opérations initiales.  Le script init-correction.py
            va exécuter ce script à l'intérieur de tous les dossiers groupe_*.

            Ensuite, exécuter le script python init-correction.py

        Initialiser la correction:

            $ python3 init-correction.py

    Corriger

        Faire la correction et compléter les fichiers CSV pour chaque groupe.
        Les commentaires donnés dans la colonne commentaires seront insérés dans
        le fichier final.

    Rassembler les résultats

        Quand on a tout fini, on exécute le script moodle.py

        $ python3 moodle.py

        Ce script produit un fichier out.csv qui est la version remplie du
        formulaire d'évaluation.  Un fichier output.log dira s'il manque des
        choses et le fichier out.csv aura aussi des mentions 'NOT_FOUND' s'il
        manque quelque chose pour un certain groupe.

FICHIERS

    globals.py
        Contient les constantes qu'on pourrait vouloir configurer comme les
        numéros de colonnes dans les fichiers CSV et les noms de fichiers et
        dossiers.  En principe, tout devrait être configurable par ce fichier.

    group.py

        Code responsable de traiter les fichiers CSV individuels.
        Lorsqu'exécuté comme main (python3 group.py), le programme lit le
        fichier de requis requis.json et crée un fichier .csv.

        Sinon, ce fichier est utilisé comme module pour fournir des fonctions
        qui traitent les fichiers CSV de chaque groupe.  Il founit la fonction
        get_totals() qui retourne {'tota': <le total> , 'feedback': <le
        feedback>}

    moodle.py

        Lorsqu'exécuté comme main, le script va remplir le fichier CSV de moodle
        en allant chercher les totaux de chaque fichier individuel de chaque
        groupe.


    init-correction-moodle.sh

        Ce fichier doit être exécuté au début.  Il appelle group.py pour générer
        une grille de correction en .csv et en dépose une copie dans le dossier
        chaque groupe et appose le numéro du groupe au fichier pour éviter les
        erreurs.

        On peut ajouter des commandes dans ce fichier si on veut qu'une action
        soit répétée pour chaque groupe, comme décompresser une archive.

    requis.json

        Fichier contenant les requis du travail.  C'est-à-dire le nombre de
        points associés à chaque item du travail pour la correction.  Le format
        est

            {
                CODE : {
                    "weight" : POINTS
                    "description" : DESCRIPTION
                },
                ...
            }

    test_dir:
        Un exemple du dossier qui aurait été téléchargé de Moodle

        test_dir
        ├── Groupe_01
        │   └── correction_tp4_Groupe_01.csv
        ├── Groupe_02
        │   └── correction_tp4_Groupe_02.csv
        └── Groupe_03
            └── correction_tp4_Groupe_03.csv



