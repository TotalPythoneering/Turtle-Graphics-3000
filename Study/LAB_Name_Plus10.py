# MISSION: Solution examples for the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-06-21 12:40:58
# FILE: LAB_Name_Plus10.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#

print("Offs", "Char", "ord()", "+10", sep='\t')
for ss, dat in enumerate("John Doinski"):
    val = ord(dat)
    print(int(ss), dat,
          val, chr(val + 10),
          sep="\t")
          
    
