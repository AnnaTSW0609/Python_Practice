"""Given: number N, DNA string s, Array A"""
"""Return: Array B containing expected number of times that s will be a substring of t"""
"""t = strings length N and with GC% of A[i]"""

with open("filename", "r+") as f:
  
  for line in f:
    
    if line.isdigit() == True:
      
      N = line.strip()
      
    elif line.isalpha() == True:
      
      s = line.strip()
      
    else:
      
      A = line.strip().split()
      
B = [] # the answer array 

for GC in A:
  
  Prob = 1 # to obtain probability that matches GC% and matches s
  
  for base in s:
    
    if base == "G" or base == "C":
      
      Prob *= ((1-float(GC))/2) 
    
    elif base == "A" or base == "T":
      
      Prob *= (float(GC)/2) 
      
  B.append(Prob*N) # expected number in a string length N

print(B)
