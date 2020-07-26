"""given a list of characters, and the length of permutation required"""
"""return all the permutations in lexigraphical order"""

with open ("/Users/annatswater/Desktop/rosalind_pper.txt","r+") as f:
  
  for line in f:
    
    if len(line)>1:
      char_lst = sorted(line.strip().split(" "))
    
    else:
      number = int(line)

def lexi_perm(char, num): # char =  list of characters

    from itertools import product # native python function, not permutation but Cartesian product

    # https://stackoverflow.com/questions/3099987/generating-permutations-with-repetitions
    
    for i in product(char,repeat = num): # permutations (list to permutate, length)
      
      print ("".join(i)) 
        # i = list(i) # returns tuple, so turn into list first

        # output = ""

        # for x in i:

            # output += x # required format: string

        # print(output)

lexi_perm(char_lst,number)
