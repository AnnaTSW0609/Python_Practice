"""Inferring all possible mRNA that can give rise to a protein"""
""" ans = total number of possible mRNA mod 1,000,000; to avoid storage of large numbers"""

# python modulo operator = %
# 7 % 2 (7/2 = 3...1)
# >>> 1

# but then 1%6 = 1 because 1/6 = 6*0 +1 
# so if x%y where y>x, x%y = x

# Codon table

bases = "UCAG"
codons = [a + b + c for a in bases for b in bases for c in bases] # random forming ttt, ttc,tta, ttg, to get the 64 codons
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'# already in the right order


# actually you could just count the number of amino acids in the amino_acid variable to get all possibilities
# sigh

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
    


Prot = input("Your protein: ")

Prot += "*" # add back the stop codon

M = 1 # there is only 1 start codon

for aa in Prot:
    
    aa_prob = int(new_codon_table.get(aa)) # get the total number of codons for an aa
    
    M = (M*aa_prob)%1000000

    # this is because there is up to 6 different codons for an amino acid

    # and 1/2/3/4/5/6 mod 1000000 = the same 

print(M)
    

   




