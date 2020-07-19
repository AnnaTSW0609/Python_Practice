"""Finding the transitions and transversions between 2 DNA strings"""
"""Transitions = Purine for purine (A<->G) or Pyrimidine for Pyrimidine (C<->T)"""
"""Transversions = Purine <-> pyrimidine"""
"""Transversions usually less common (transition: transversion = 2)"""
"""but transversions more common in coding region (ratio = 3) because it causes more drastic changes"""
"""Thus helpful when defining coding regions"""

with open (file, "r+") as f:
  
  DNA_string = ""
  
  DNA_lst = []
  
  for line in f:
    
    if ">" in line:
      pass
    
    else:
      
      for char in line:
        
        DNA_string += char
        
        if char = " ":
          
          DNA_lst.append(DNA_string)
          DNA_string = ""
          
  print(DNA_lst)
  
          
