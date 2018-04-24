import groupinfo
import os
from shutil import copyfile
from globals import Configs
from moodle import group_to_file
import subprocess

groupinfo.make_csv(
    Configs.REQUISITES_FILE,
    Configs.ORIGINAL_CORRECTION_FILE + '.csv'
)

for group in os.listdir(Configs.DIR):
    target = group_to_file(group)
    copyfile(Configs.ORIGINAL_CORRECTION_FILE + '.csv',target)
    subprocess.call(['./initial-operations.sh', os.path.dirname(target)])