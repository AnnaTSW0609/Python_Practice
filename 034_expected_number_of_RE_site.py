"""Given: number N, DNA string s, Array A"""
"""Return: Array B containing expected number of times that s will be a substring of t"""
"""t = strings length N and with GC% of A[i]"""

with open("/Users/annatswater/Desktop/rosalind_rstr.txt", "r+") as f:
  
  for line in f:

      line = line.strip()

      if line.isdigit() == True:

          N = float(line.strip())

      elif line.isalpha() == True:

          s = line.strip()
      
      else:

          A = line.strip().split()

B = [] # the answer array 

for GC in A:
  
  Prob = 1 # to obtain probability that matches GC% and matches s
  
  for base in s:
    
    if base == "G" or base == "C":
      
      Prob *= (float(GC)/2)
    
    elif base == "A" or base == "T":
      
      Prob *=  ((1-float(GC))/2) 
      
  B.append(str(Prob*(N-len(s) +1))) # prob of substring matching GC% and s * number of all substring with len(s) in string len(N)
  
  # https://math.stackexchange.com/questions/141044/number-of-substrings-of-length-m-in-a-string-of-length-n

  # last possible starting point = len(string) - len(substring) +1 i.e. move back one position forward


print(" ".join(B))
