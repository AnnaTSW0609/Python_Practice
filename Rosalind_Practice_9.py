"""Calculating Protein Mass"""

# Create Monoisotopic Table from file 

mol_weight = {} # empty dictionary 

with open ("/Users/annatswater/Desktop/Monoisotopic_Table.txt", "r+") as f: # this is a txt I copied from the question prompt, format: A 71.03711 etc.

    for line in f:

        line = line.split()

        mol_weight.update({line[0]: float(line[1])}) # parse file result in string, so need to float() it
       
    
prot = "SKADYEK"

total_mol = 0

for char in prot:

    total_mol += mol_weight.get(char) # dict.get(key) returns value of that key
    
print("{:.3f}".format(total_mol))
