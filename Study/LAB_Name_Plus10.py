# MISSION: tbd.
# STATUS: tbd.
# VERSION: 1.0.0
# NOTES: tbd.
# DATE: 2018-06-21 12:40:58
# FILE: LAB_Name_Plus10.py
# AUTHOR: tbd.
#

print("Offs", "Char", "ord()", "+10", sep='\t')
for ss, dat in enumerate("John Doinski"):
    val = ord(dat)
    print(int(ss), dat,
          val, chr(val + 10),
          sep="\t")
          
    
