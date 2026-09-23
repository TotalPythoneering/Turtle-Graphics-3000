# MISSION: Solution examples for the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-06-21 12:40:58
# FILE: LAB_Name_Plus10.py
# AUTHOR: Randall Nagy
#

print("Offs", "Char", "ord()", "+10", sep='\t')
for ss, dat in enumerate("John Doinski"):
    val = ord(dat)
    print(int(ss), dat,
          val, chr(val + 10),
          sep="\t")
          
    
