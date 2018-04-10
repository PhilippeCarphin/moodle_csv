#!/bin/bash

DIR=test_dir
CORRECTION_FILE=correction_tp4.csv
python3 groupinfo.py
pushd $DIR
for d in $(ls); do
    if [ -d $d ] ; then
        pushd $d 1>/dev/null 2>/dev/null
        echo "========= in $d =========="
        ls
        echo "unzip $(ls *.zip)"
        cp ../../$CORRECTION_FILE ${CORRECTION_FILE%%.csv}_$d.csv
        popd 1>/dev/null 2>/dev/null
        echo
    fi
done
popd
