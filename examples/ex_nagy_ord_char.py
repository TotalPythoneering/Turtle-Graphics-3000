# MISSION: Examples from the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-08-09 05:18:34
# FILE: ex_nagy_ord_char.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#

for ss in range(100):
    print() #  clear the screen

data = "Randall Nagy"

for dat in data:
    print(dat, ord(dat),
          chr(ord(dat)), sep='\t')


