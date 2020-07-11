"""Return consensus sequence"""

# Execution time very long (2+ minutes for 1kb sequences, look for suggestions and improvements

import numpy as np 

with open ("/Users/annatswater/Desktop/seq_file.txt", "r+") as f:
    seq_array = [] 
    consensus = ""

    for line in f:

        line = line.rstrip()

        if ">" in line:

            pass

        else:

            seq = [] 

            for char in line:

                seq.append(char) # store all nucleotides in a string in a list

            
            seq_array.append(seq) # create nested list for lists of nucleotides in each string

    seq_array = np.array(seq_array) # turn nested list into array
    
    Seq_count = []
    
    A = []

    T = []

    C = []

    G = [] 

    for i in range(len(seq_array[0])): # number of nucleotides in each string

        A_count = 0
        T_count = 0
        C_count = 0
        G_count = 0

        for char in seq_array[:,i]: # the position of nucleotide in all strings, e.g. 2nd pos in every stirng

            if char == "A":

                A_count+=1

            elif char == "C":

                C_count+=1

            elif char == "G":

                G_count += 1

            else:

                T_count += 1
        
        A.append(A_count)
        T.append(T_count)
        C.append(C_count)
        G.append(G_count)

    
    Seq_count.append(A)
    Seq_count.append(C)
    Seq_count.append(G)
    Seq_count.append(T)

    Seq_count = np.array(Seq_count) # put the ATGC count for each position into the same list then the same array for comparison
    
    # horizontal = list, each item = count in each position, vertical = ATCG

    for i in range(len(Seq_count[0])):

        ATCG_max = []

        for char in Seq_count[:,i]:

            ATCG_max.append(char) # adding all the count number to a list, because technically they belong to different lists (horizontal) and we want vertical

        if max(ATCG_max) == ATCG_max[0]: # they are in that order

            consensus += "A"

        elif max(ATCG_max) == ATCG_max[1]:

            consensus += "C"

        elif max(ATCG_max) == ATCG_max[2]:

            consensus += "G"

        elif max(ATCG_max) == ATCG_max[3]:

            consensus += "T"
            
    # print the answer in the asked format
    print(consensus)
    print("A: ",*A)
    print("C: ",*C)
    print("G: ",*G)
    print("T: ",*T)
