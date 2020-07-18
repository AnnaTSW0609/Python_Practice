"""Translation with intron"""

with open("/Users/annatswater/Desktop/rosalind_ini6.txt", "r+") as f:
  
  lst_seq = []
  
  for line in f:
    if ">" in line:
      pass
    else:
      if "\n" in line:
          line = line.replace("\n", "")
          lst_seq.append(line)
      else:
          lst_seq.append(line)
      
  sequence = max(lst_seq) # save every line to the list, then remove the max lengthed item

  lst_seq.pop(lst_seq.index(sequence)) # this list would be the introns


  for intron in lst_seq: # remove the introns from the DNA seq

      if sequence.find(intron) != -1:
          sequence = sequence.replace(intron, "")

  

