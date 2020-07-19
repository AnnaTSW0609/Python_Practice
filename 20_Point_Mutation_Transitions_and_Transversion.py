"""Finding the transitions and transversions between 2 DNA strings"""
"""Transitions = Purine for purine (A<->G) or Pyrimidine for Pyrimidine (C<->T)"""
"""Transversions = Purine <-> pyrimidine"""
"""Transversions usually less common (transition: transversion = 2)"""
"""but transversions more common in coding region (ratio = 3) because it causes more drastic changes"""
"""Thus helpful when defining coding regions"""


# input

first_DNA = input("First DNA: ")

second_DNA = input("Second DNA: ")


transition = 0
transversion = 0

# start counting 

for x, y in zip(first_DNA, second_DNA):
  
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
