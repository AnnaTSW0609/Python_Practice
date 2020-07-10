"""Finding substring in string, application to find motif in DNA"""

DNA = "GATATATGCATATACTT"

motif = "ATAT"

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
            all_pos += str(start)
            all_pos += " "
        
        else: 
            # If no further substring is present, pos will = -1 
            break

    
    print((all_pos))

CountOccurrences(DNA, motif)
