
print("Offs", "Char", "ord()", "+10", sep='\t')
for ss, dat in enumerate("John Doinski"):
    val = ord(dat)
    print(int(ss), dat,
          val, chr(val + 10),
          sep="\t")
          
    
