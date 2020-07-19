"""Finding the transitions and transversions between 2 DNA strings"""
"""Transitions = Purine for purine (A<->G) or Pyrimidine for Pyrimidine (C<->T)"""
"""Transversions = Purine <-> pyrimidine"""
"""Transversions usually less common (transition: transversion = 2)"""
"""but transversions more common in coding region (ratio = 3) because it causes more drastic changes"""
"""Thus helpful when defining coding regions"""

# to read the file that had \n for the same sequence 

with open ("/Users/annatswater/Desktop/rosalind_subs.txt", "r+") as f:
  
  DNA_string = ""
  
  DNA_lst = []




# start counting 

for x, y in zip(DNA_lst[0], DNA_lst[1]):
  
  if x != y:
    
    if x == "A" and y == "G":
      
      transition += 1
      
    elif  x == "G" and y == "A":
      
      transition += 1
      
    elif  x == "C" and y == "T":
      
      transition += 1
      
    elif  x == "T" and y == "C":
      
      transition += 1
      
    else:
      
      transversion += 1
      
print(transition/transversion)
      
    
