"""Finding the transitions and transversions between 2 DNA strings"""
"""Transitions = Purine for purine (A<->G) or Pyrimidine for Pyrimidine (C<->T)"""
"""Transversions = Purine <-> pyrimidine"""
"""Transversions usually less common (transition: transversion = 2)"""
"""but transversions more common in coding region (ratio = 3) because it causes more drastic changes"""
"""Thus helpful when defining coding regions"""

with open ("/Users/annatswater/Desktop/rosalind_subs.txt", "r+") as f:
  
  DNA_string = ""
  
  DNA_lst = []

  final_lst = []
  
  for line in f:
    
    if ">" in line:
      pass
    
    else:

        if len(DNA_lst) == 0:

            DNA_lst.append(line)

        elif len(DNA_lst) != 0 and len(line) < len(max(DNA_lst)):

            for item in DNA_lst:

                DNA_string += item

            final_lst.append(DNA_string)
            DNA_string = ""
            
  print(final_lst)
          

  
          
