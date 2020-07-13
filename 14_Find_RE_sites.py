"""Finding position and length of panlindrome sequences (4-12bp) in given sequence"""

DNA = "TTTAAATTTAAA"

import re 

def ReverseComplement(string): # need to consider reverse complementary string and its ORF as well

    intab = "ATCG"
    outtab = "TAGC" # corresponding position for elements to be replaced
    trantab = string.maketrans(intab, outtab) # provide template
    return(string.translate(trantab) [::-1]) # translate the string in the pattern defined in trantab, + reverse in our case

RE_list = []
RE_index_list = {}

for i in range(len(DNA)):

    for j in range(i+4, i+13):

        Substring = DNA[i:j]

        if len(Substring) >= 4:

            print(Substring)
            
            rev_Substring = ReverseComplement(Substring)
            
            if rev_Substring == Substring:
              
              RE_list.append(Substring)
              RE_list = list(dict.fromkeys(RE_list))

        else:
            pass
        
print(RE_list)

for i in RE_list:
    Iter_index = [m.start() for m in re.finditer(i, DNA)] # this would return lists of position, one list for each of the RE substrings
    
    
    

