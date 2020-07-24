"""Inferring all possible mRNA that can give rise to a protein"""
""" ans = total number of possible mRNA mod 1,000,000; to avoid storage of large numbers"""

# Codon table

bases = "UCAG"
codons = [a + b + c for a in bases for b in bases for c in bases] # random forming ttt, ttc,tta, ttg, to get the 64 codons
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'# already in the right order 
codon_table = dict(zip(codons, amino_acids))

# for key, value in codon_table.items(): # item() yield key-value pairs
    # print(key, "->", value)

# Group keys with the same value by creating a new dictionary 
# https://stackoverflow.com/questions/54249400/python-how-to-group-keys-that-have-the-same-values-in-a-dictionary

# store the names (the keys of the new dict) as a set (keeps elements unique)
names = set(codon_table.values())

# use a list comprehension, iterating through keys and checking the values match each n
# i.e. matching the amino acids in the names dictionary
new_codon_table = {}
for n in names:
    new_codon_table[n] = [k for k in codon_table.keys() if codon_table[k] == n]
    
 # this will return 'I': ['AUU', 'AUC', 'AUA'], i.e. all possible codes for an amino acid

for key, value in new_codon_table.items():
  
  value_count = len(value)
  
  new_codon_table[key] = len(value)
    
print(new_codon_table)

Prot = input("Your protein: ")

Prot += "*" # add back the stop codon

M = 1 # there is only 1 start codon

for aa in Prot:
    
    aa_prob = int(new_codon_table.get(aa)) # get the total number of codons for an aa
    
    M = (M*aa_prob)%1000000

print(M)
    

    
        

        
        
        

# python modulo operator = %
# 7 % 2 (7/2 = 3...1)
# >>> 1

