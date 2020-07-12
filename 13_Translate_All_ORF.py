"""Finding motif, from 11"""

# Reference:
# http://recologia.com.br/2013/06/problema-rosalind-open-reading-frames-orf/

DNA = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

motif = "ATG"

def ReverseComplement(string): # need to consider reverse complementary string and its ORF as well

    intab = "ATCG"
    outtab = "TAGC" # corresponding position for elements to be replaced
    trantab = string.maketrans(intab, outtab) # provide template
    return(string.translate(trantab) [::-1]) # translate the string in the pattern defined in trantab, + reverse in our case

Rev_DNA = ReverseComplement(DNA)


# Reference:
# https://www.geeksforgeeks.org/python-count-overlapping-substring-in-a-given-string/


def CountOccurrences(string, substring): 
  
    # Initialize start to 0 and list for all position to empty 
    start = 0
    all_pos = ""

    # Search through the string till 
    # we reach the end of it 
    while start < len(string): # forever loop back until I break it
        
        pos = string.find(substring, start) # default start = 0
        
        if pos != -1: 
            start = pos + 1 # loop back to search from after first match after while, +1 becasue answer wants 1-based index
            all_pos += str(pos) # so use original for 0-based index, since we are dealing with python strings 
            all_pos += " "
        
        else: 
            # If no further substring is present, pos will = -1 
            break

    
    return(all_pos.split())

ATG_pos = CountOccurrences(DNA, motif)

Rev_ATG_pos = CountOccurrences(Rev_DNA, motif)


"""Translation from ALl ORF in a sequence, modification of 8"""

# Generate codon table as a python dictionary 
# from http://www.petercollingridge.co.uk/tutorials/bioinformatics/codon-table/ with annotation and modification 

bases = "TCAG"
codons = [a + b + c for a in bases for b in bases for c in bases] # random forming ttt, ttc,tta, ttg, to get the 64 codons
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'# already in the right order 
codon_table = dict(zip(codons, amino_acids))

def translate (ATG_positions, seq): # seq = a string to be translated, ATG_positions = a list of positions of ORF
    
    peptide = ""
    
    all_possible_pep = [] # for storing all possible translation
    
    for item in ATG_positions: # starting from the ORFs
        item = int(item)
        for i in range(item, len(seq), 3):
            codon = seq [i: i+3] # +3 so that cover the third base, index issue
            amino_acid = codon_table.get(codon, '*')

            if amino_acid != '*': # use dictionary get method to obtain the amino acid, which is the value for the key (codon)
                peptide += amino_acid
            
            else:
                peptide += amino_acid # so I'll include the * in the sequence to distinguish
                # as only peps with start and stop without stop in between are ORFs
                break
                
        all_possible_pep.append(peptide) # this must be inside the loop, so it would append all the items with the opening index in ATG_position
        peptide = ""

    new_possible_pep = [] # for storing all with start and *
    
    for item in all_possible_pep:
        if "*" in item:
            new_possible_pep.append(item.replace("*", "")) # if replace in original string will cause confusion
            
    
    return(new_possible_pep) # if print, the result would be a non-type instead if you want to save it as below of a variable
    
    
F = translate(ATG_pos, DNA)

R= translate(Rev_ATG_pos, Rev_DNA)

for item in list(set(F+R)):
    print(item) # intersection between the two lists
        
        
    
    
    
