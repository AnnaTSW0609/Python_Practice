"""Translation with intron"""

with open() as f:
  
  lst_seq = []
  
  for line in f:
    if ">" in line:
      pass
    else:
      lst_seq.append(line)
      
  sequence = max(lst_seq)
  lst_seq.pop(sequence)
  
  print(lst_seq)
  print(sequence)
      
