"""Finding a shared motif between multiple strings"""

# Adapted from https://www.geeksforgeeks.org/longest-common-substring-array-strings/?ref=rp


with open("/Users/annatswater/Desktop/rosalind.revp.txt","r+") as f:

    seq_array = []

    for line in f:

        if ">" not in line:

            seq = []

            if "\n" in line:

                line = line.replace("\n", "")

            seq_array.append(line) # create nested list for lists of nucleotides in each strin


    common_motif = ""
    
    # take the longest sequence as reference

    longest_seq = max(seq_array)
    longest_length = len(longest_seq)

    for i in range(longest_length):

        for j in range(i+1, longest_length+1):

            # generate all possible substrings in the longest string

            substring = longest_seq[i:j]

            for k in range(1, len(seq_array)): # scan through all sequences

                if substring not in seq_array[k]:
                    break

                elif (k+1 == len(seq_array) and len(common_motif) < len(substring)):
                    common_motif = substring

    print(common_motif)
    
