"""Permutation in this context: ordering of positive integers"""
"""e.g. x = (5,4,3,2,1) is a permutation of length of 5"""
"""Finding all possible permutations of n integers"""

n = int(input("Integer: "))

Per = 1

for i in range(2, n+1): # return the total possible number of permutations, i.e. n!/(n-r)!, if select all (r=n), nPr = n!
  
  Per = Per*i
  
print(Per)

from itertools import permutations

for i in permutations(range(1,n+1), n): # print all permutations of range (1 to n) of length n
    i = list(i)
    print(*i)

