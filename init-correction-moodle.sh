#!/bin/bash

DIR=test_dir
original_correction_file=correction_tp4.csv
python3 groupinfo.py
pushd $DIR
for d in $(ls); do
    if [ -d $d ] ; then
        pushd $d 1>/dev/null 2>/dev/null
        echo "========= in $d =========="
        ls
        echo "unzip $(ls *.zip)"
        new_correction_file=${original_correction_file%%.csv}_$d.csv
        if ! [ -e new_correction_file ] ; then
            cp ../../$original_correction_file $new_correction_file
        fi
        popd 1>/dev/null 2>/dev/null
        echo
    fi
done
popd
