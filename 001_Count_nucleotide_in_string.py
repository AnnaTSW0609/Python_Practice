# Rosalind Practice no.1

"""Counting the number of each nucleotides in any given string"""

DNA = "ATCGATCG"

A_count = 0
T_count = 0
C_count = 0
G_count = 0

for letter in DNA:
  if letter == "A":
    A_count+=1
  elif letter == "T":
    T_count+=1
  elif letter == "C":
    C_count += 1
  else:
    G_count += 1
 

print(A_count, C_count, G_count, T_count)
