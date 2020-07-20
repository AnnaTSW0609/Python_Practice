"""Finding motifs that would only exist after splicing"""
"""e.g. "ACG" is found in "TATGCTAAGATC" """
"""Pos 2: A, Pos 5: C, Pos 9: G (1-based)"""

DNA = input("DNA string: ")

motif = input("motif: ")

motif = list(motif) # spliting the motif characters into a list

ans = []

for char in motif:

    if len(ans) == 0: # if the list is empty
      
      pos = DNA.find(char)
      
      ans.append(pos+1) # 1 based index 
      
    else:
      
      pos = DNA.find(char, (ans[-1]+1))# the latest index in the list = the starting position for search for the next
      
      ans.append(pos+1)
      
print(*ans)

# But this is very slow, how to improve on it?
      
      
      
      
    
