"""Given a sequence (length <= 100 kbp)"""
"""Return frequencies of lexicographical 4-mers"""


# borrowed from 029, lexicographical permutation 

def lexi_perm(char, num): # char =  list of characters
  
    perm_list = [] # to store all the lexicographical 4-mers

    from itertools import product # native python function, not permutation but Cartesian product

    # https://stackoverflow.com/questions/3099987/generating-permutations-with-repetitions
    
    for i in product(char,repeat = num): # permutations (list to permutate, length)
      
      perm_list.append("".join(i))# use "".join because i is a tuple containing all the char in order
    
    return perm_list 
    
four_mers = lexi_perm(["A", "C", "G", "T"], 4)

with open("/Users/annatswater/Desktop/rosalind_kmer.txt", "r+") as file:

  lst = []

  DNA = ""
  
  for line in file:
    
    if ">" not in line:
      
      lst.append(line.strip())

  DNA = "".join(lst)

ans_array = [] # this is for inputing the frequencies

import regex # to find overlapps and repeats

for item in four_mers:
  
  ans_array.append(len(list(regex.finditer(item, DNA, overlapped=1))))

with open("/Users/annatswater/Desktop/032_ans.txt", "w+") as f:

    f.write(" ".join(str(item) for item in ans_array))

    # apparently this works: https://stackoverflow.com/questions/27826214/how-do-i-make-a-space-between-words-when-writing-to-a-text-file-in-python
    # and this doesn't: https://stackabuse.com/reading-and-writing-lists-to-a-file-in-python/
    # in particular filehandle.write('%s\b' % listitem) didn't
    # because https://stackoverflow.com/questions/26029389/what-is-the-python-3-equivalent-of-s-in-strings
    # %s actually stands for items, so you would end up with \x08 for space
    # https://stackoverflow.com/questions/22961145/the-reason-python-string-assignments-accidentally-change-b-into-x08-and/22961200
    # The string escapes, that way even if they look the same to human eyes, computer would recognize it differently
