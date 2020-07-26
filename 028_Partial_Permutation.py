"""permutation of k out of n numbers, mod 1,000,000"""

n = int(input("n: "))

k = int(input("k: "))

def perm(x):
  
  Per = 1

  for i in range(2, x+1): # return the total possible number of permutations, i.e. n!/(n-r)!, if select all (r=n), nPr = n!
  
    Per *= i

    # Per %= 10**6 # only doing the modulo at the end doesn't prevent the overflow, or does it?
  
  return Per 

print((perm(n)/perm(n-k))%10**6)




