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

