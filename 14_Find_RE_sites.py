"""Finding position and length of panlindrome sequences (4-12bp) in given sequence"""

DNA = "TTTAAATTTAAA"

DNA = input() # use input to avoid cut and paste problem

import re 

def ReverseComplement(string): # need to consider reverse complementary string and its ORF as well

    intab = "ATCG"
    outtab = "TAGC" # corresponding position for elements to be replaced
    trantab = string.maketrans(intab, outtab) # provide template
    return(string.translate(trantab) [::-1]) # translate the string in the pattern defined in trantab, + reverse in our case

RE_list = []

for i in range(len(DNA)): # the i here is already index, so can directly print

    for j in range(4, 13): # index issue: if len = 12, i+13
        
        # if len(Substring) >= 4:
        
        # Originally I have the above line to shuffle out those substring at the end of the DNA string, turns out it is the wrong way
        
        Substring = DNA[i:i+j]

        rev_Substring = ReverseComplement(Substring)

        if rev_Substring == Substring and i+j<=len(DNA): # can directly print index

        # i+j <= DNA = limit on length, or it wouldn't make sense that the substring extend beyond the string
        
            print(i+1, j) # i = starting position, j = ending, i.e. length
              
              # RE_list.append(Substring)
              # RE_list = list(dict.fromkeys(RE_list))

        # else:
            # pass
        
# print(RE_list)

# RE_index_list = [] # this list stores all the lists (some with one item) for the position matches

# for i in RE_list:
    # Iter_index = [m.start() for m in re.finditer(i, DNA)] # this would return lists of position, one list for each of the RE substrings
    # RE_index_list.append(Iter_index)
# So, the index of the item in RE_index_list will match the index of the items in RE_list
# i.e. each palindrome in RE_list matches the positions in RE_index_list

# print(RE_index_list)
            
#for i,j in zip(RE_list, RE_index_list):

    # if RE_list.index(i) == RE_index_list.index(j): # i.e. each palindrome corresponds to position of each list in the index list

        # for item in j: # return all matching positions in the list for each palindrome

            # print(item+1, len(i)) # +1 to match 1-based position
            

            
        
        
            
            
    
    
    

