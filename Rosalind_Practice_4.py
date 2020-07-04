"""Computing the Hamming Distance, i.e. the number of nucleotides differing between two strings, s and t"""

s = "ATCGATCG"

t = "ATCCACTG"

count = 0

for a, b in zip(s, t): # couple two lists loop through stuff at the same position 
    if a != b:
        count += 1
        
print(count)
        
# set(a).intersection(b) finds how many different items between two lists, returns a dictionary
# but this doesn't return the number of total differents but rather how many categories are different
# e.g. A, T, C, G but not how many As, Ts, Cs, and Gs are different 
# list () turns the dictionary into a list
# len() finds out the length, i.e. number of items in that list, thus the number of differing items
