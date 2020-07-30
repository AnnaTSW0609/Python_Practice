"""Given an integer N, GC% x and a random DNA string s"""
"""Return probability if N random strings is constructed with GC% x, at least 1 = s"""

with open(file, "r+") as f:
  
  for line in f:
    
    if line.isalpha() == True:
      
      s = line.strip()
      
    else:
      
      lst = line.strip().split()
      
      N = lst [0]
      
      x = lst [1]

# P(A) + P(not A) = 1
# thus at least 1 = 1 -  no sequence matching s in N sequences

# Compute P(matches GC% and exactly s)
# Borrowed from 031

Prob = 1 # initializing 

for base in s:
  
    if base == "A" or base == "T":
    
      Prob *= ((1-float(x))/2) 
   
    elif base == "G" or base == "C":
      
      Prob *= (float(x)/2) 

print(Prob)      
