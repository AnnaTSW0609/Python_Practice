"""Translation with intron"""

# define the codon table for translation

bases = "TCAG"
codons = [a + b + c for a in bases for b in bases for c in bases] # random forming ttt, ttc,tta, ttg, to get the 64 codons
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'# already in the right order 
codon_table = dict(zip(codons, amino_acids))

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

  

