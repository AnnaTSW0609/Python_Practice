"""Finding motifs that would only exist after splicing"""
"""e.g. "ACG" is found in "TATGCTAAGATC""""
"""Pos 2: A, Pos 5: C, Pos 9: G (1-based)"""

DNA = input("DNA string: ")

motif = input("motif: ")

motif = motif.split # spliting the motif characters into a list

for char in motif:
  
  print(DNA.find(char))
