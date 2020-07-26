"""given a list of characters, and the length of permutation required"""
"""return all the permutations in lexigraphical order"""

with open ("filename","r+") as f:
  
  for line in f:
    
    if len(line)>1:
      line = sorted(line.split(" "))
    
    else:
      number = line

print(line)
print(number)
      
