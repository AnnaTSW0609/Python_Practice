"""Reading sequences from fasta file and find the sequence with the highest GC%"""

# used "awk '/^>/ {printf("\n%s\n",$0);next; } { printf("%s",$0);}  END {printf("\n");}' < rosalind_gc.txt > new_rosalind_gc.txt"

# in Bash to solve the problem (cd Desktop first, and need to delete the first empty line)

# because the fasta file is not in the same line 

with open("/Users/annatswater/Desktop/new_rosalind_gc.txt","r+") as f:

    # all_seq = {} # empty dictionary to store the sequences

    name = []

    seq = []

    for line in f: # save names and sequences separately 

        line = line.rstrip() # remove \n

        if ">" in line:

            line = line.replace(">","") # answer format required 
            
            name.append(line)

        else:

            count = 0

            for char in line:

                if char == "G" or char == "C":

                    count += 1

            GC_count = count/len(line)

            seq.append(GC_count)
    

    max_item = max(seq) # the largest GC% in the list 

    print(name[seq.index(max_item)])

    print("{:.6f}".format(max_item*100)) # you must get the % or else it wouldn't be right! times 100! 
 
# Reference: https://www.researchgate.net/post/How_can_I_join_the_wrap_lines_in_a_huge_FASTA_file and https://www.biostars.org/p/9262/

            

    
