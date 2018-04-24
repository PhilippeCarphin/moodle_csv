import moodle
import groupinfo
from globals import Configs
"""
Example usage of my thing

Assumes a file from moodle with rows as defined in the globals.Moodle class.

Provides the function group_info_factory to construct a function that
returns a dictionary {'totals': XYZ, 'feedback': "bla bla bla"} that
the fill_in_moodle_sheet function will use to fill in the rows of the file.

The factory needs a way of getting a filename from a group and a way of getting
the info from that file.
"""

info_getter = groupinfo.group_info_factory(groupinfo.group_to_file, groupinfo.get_group_info_internal)


moodle.fill_in_moodle_sheet(Configs.MOODLE_CORRECTION_FILE, 'out.csv', info_getter=info_getter)