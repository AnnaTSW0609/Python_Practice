"""permutation of k out of n numbers, mod 1,000,000"""

n = int(input("n: "))

k = int(input("k: "))

def permutation(x):
  
  Per = 1

  for i in range(2, x+1): # return the total possible number of permutations, i.e. n!/(n-r)!, if select all (r=n), nPr = n!
  
    Per = Per*i
  
  return Per 

print((int(permutation(n))/int(permutation(n-k)))%1000000)
