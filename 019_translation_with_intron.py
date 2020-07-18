"""Translation with intron"""

# define the codon table for translation

bases = "TCAG"
codons = [a + b + c for a in bases for b in bases for c in bases] # random forming ttt, ttc,tta, ttg, to get the 64 codons
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'# already in the right order 
codon_table = dict(zip(codons, amino_acids))

# then define translation algorithm 

def translate (seq):
    
    peptide = ""
    
    for i in range(0, len(seq), 3): # range(start, stop, step) https://www.geeksforgeeks.org/python-range-function/
        codon = seq [i: i+3] # +3 so that cover the third base, index issue
        amino_acid = codon_table.get(codon, '*')

        if amino_acid != '*': # use dictionary get method to obtain the amino acid, which is the value for the key (codon)
            peptide += amino_acid
            
        else: # * =  stop codon, so if have * break
            break

    return (peptide)

with open("/Users/annatswater/Desktop/rosalind_splc_1.txt", "r+") as f:
  
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
      
  sequence = lst_seq[0] # the first item is by default the original string
  # sequence = max(lst_seq, key=len) # if want to find the max item length, when the position of the longest string is not fixed 
  lst_seq.pop(0) # remove it from the list to get a list of introns 
  
  
for intron in lst_seq: # remove the introns from the DNA seq

    if sequence.find(intron) != -1:

        sequence = sequence.replace(intron, "")

pep = translate (sequence)
print(pep)
