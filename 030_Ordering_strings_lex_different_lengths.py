"""Ordering different strings of different lengths lexicographically"""

with open("/Users/annatswater/Desktop/rosalind_pper.txt", "r+") as f:
  
  for line in f:
    
    if line.isdigit() == True:
      
      length = line
    
    else:
      
      alphabet = sorted(line.strip().split(" "))

print(length)
print(alphabet)
