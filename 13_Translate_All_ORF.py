"""Translation from ALl ORF in a sequence, modification of 8"""

# Generate codon table as a python dictionary 
# from http://www.petercollingridge.co.uk/tutorials/bioinformatics/codon-table/ with annotation and modification 

bases = "TCAG"
codons = [a + b + c for a in bases for b in bases for c in bases] # random forming ttt, ttc,tta, ttg, to get the 64 codons
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'# already in the right order 
codon_table = dict(zip(codons, amino_acids))

print(codon_table)

def translate (seq):
    
    peptide = ""
    
    all_possible_seq = []
    
    for i in range(0, len(seq), 3): # range(start, stop, step) https://www.geeksforgeeks.org/python-range-function/
        
        codon = seq [i: i+3] # +3 so that cover the third base, index issue
        
        amino_acid = codon_table.get(codon, '*')

        if amino_acid == "ATG":
            
            peptide += amino_acid
           
        elif amino_acid != '*': # use dictionary get method to obtain the amino acid, which is the value for the key (codon)
            
            peptide += amino_acid
            
        else: # * =  stop codon, so if have * break
            all_possible_seq.append(peptide)
            peptide = ""

translate("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")
