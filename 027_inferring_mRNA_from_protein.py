"""Inferring all possible mRNA that can give rise to a protein"""
""" ans = total number of possible mRNA mod 1,000,000; to avoid storage of large numbers"""

# Codon table

bases = "ucag"
codons = [a + b + c for a in bases for b in bases for c in bases] # random forming ttt, ttc,tta, ttg, to get the 64 codons
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'# already in the right order 
codon_table = dict(zip(codons, amino_acids))

# python modulo operator = %
# 7 % 2 (7/2 = 3...1)
# >>> 1


