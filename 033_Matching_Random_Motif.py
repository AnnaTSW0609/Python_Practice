"""Given an integer N, GC% x and a random DNA string s"""
"""Return probability if N random strings is constructed with GC% x, at least 1 = s"""

with open("/Users/annatswater/Desktop/rosalind_rstr.txt", "r+") as f:
  
  for line in f:
    
    if line.isalpha() == True:
      
      s = line.strip()

    else:
      
      lst = line.strip().split()
      
      N = float(lst [0]) # float**float =  True
      
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

# Compute 1- not P in N sequence, i.e. 1-P**N
# Ref: https://www.youtube.com/watch?v=dwjQaJ5xt1o

print("{:.3f}".format(1- (1-Prob)**N))
