"""Ordering different strings of different lengths lexicographically"""

with open("/Users/annatswater/Desktop/rosalind_lexv.txt", "r+") as f:
  
  for line in f:
    
    if line.isdigit() == True:
      
      number = int(line)
    
    else:
      
      char_lst = line.strip().split(" ") # assume alphabet already sorted
      
      alphabet = "" # self-defined alphabet 
      
      # https://stackoverflow.com/questions/26579392/sorting-string-values-according-to-a-custom-alphabet-in-python
      
      for item in char_lst:
        
        alphabet += item
       

def lexi_perm(char, num): # char =  list of characters

    from itertools import product # native python function, not permutation but Cartesian product
    
    ans_lst = [] # an empty list for storing products(i), then outputting in order 

    # https://stackoverflow.com/questions/3099987/generating-permutations-with-repetitions
    
    for x in range(1,num+1):
    
      for i in product(char, repeat = x):# permutations (list to permutate, length)
      
        ans = "".join(i) # product still return tuple, so conconated it into a string first 
        ans_lst.append(ans)
    
    with open("/Users/annatswater/Desktop/ans_030.txt", "w+") as file:
      
        for y in sorted(ans_lst, key=lambda word: [alphabet.index(c) for c in word]):

          file.write(y + '\n') # write it to a file saves all the time waiting for it to print

lexi_perm(char_lst,number)
