"""Given: DNA string s and an array of numbers, representing GC%"""
"""Return: common log (base 10) of P(a random string with the GC-content found in A[k] will match s exactly.)"""

# read the Given datafile 
with open(filename, "r+") as f:
  
  for line in f:
    
    if line.isdigit() == True:
      
      Array = line.strip().split()
      
    else:
      
      DNA = line

# GC% can translate into DNA probability 
# e.g. if 40% GC rate, then 20% chance for any nucleotide to be a G/C, and 30% for a A/T
# so GC_rate/2 = G/C and (1-GC_rate)/2 = A/T

import math 
ans = [] # empty list for storing 

for GC_rate in Array:

  Prob = 1 # initializing

  for base in DNA:
  
    if base == A or base == T:
    
      Prob *= ((1-GC_rate)/2)*0.5 # 1 in 2 chances for A/T
   
    elif base == G or base == C:
      
      Prob *= (GC_rate/2)*0.5 # 1 in 2 chances for G/C
 
  ans.append(math.log10(Prob))

print(*ans)  
    
    
  
  
