"""Given: DNA string s and an array of numbers, representing GC%"""
"""Return: common log (base 10) of P(a random string with the GC-content found in A[k] will match s exactly.)"""

# read the Given datafile 
with open("/Users/annatswater/Desktop/rosalind_rand.txt", "r+") as f:
  
  for line in f:
    
    if "A" not in line: # if DNA characters not in line
      
      Array = line.strip().split()
      
    else:
      
      DNA = line.strip()

# GC% can translate into DNA probability 
# e.g. if 40% GC rate, then 20% chance for any nucleotide to be a G/C, and 30% for a A/T
# so GC_rate/2 = G/C and (1-GC_rate)/2 = A/T

import math 
ans = [] # empty list for storing 

for GC_rate in Array:

  Prob = 1 # initializing

  for base in DNA:
  
    if base == "A" or base == "T":
    
      Prob *= ((1-float(GC_rate))/2) 
   
    elif base == "G" or base == "C":
      
      Prob *= (float(GC_rate)/2) 
 
  ans.append("{:.3f}".format(math.log10(Prob)))

print(*ans)  
    
