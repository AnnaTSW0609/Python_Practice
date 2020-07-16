"""Mendel Second Law Application"""
"""Start with one AaBb individual"""
"""Each generation would only mate with AaBb"""
"""Each generation would have 2 offsprings"""
"""Given the above, P(N (min. number of AaBb organisms)) in the kth generation"""

# if confused, refer to https://www.youtube.com/watch?v=qIzC1-9PwQo&t=554s (jbstatistics explanation)


# Binomial distribution 

# P(anything cross with Aa) = 1/2 Aa
# Thus P (anything cross with AaBb) = 1/2 (Aa)*1/2 (Bb) = 1/4 AaBb

# Binomial distribution to solve this problem 



def Mendel_2nd_Law(N, K):
  
  # let total offspring in the kth generation be T, where T = k**2 (each offspring in the kth generation has two offspring)
  T = K**2
  
  P_AaBb = 0.25 # probability that an offspring will be AaBb in any generation that crosses with AaBb = 1/4
  
  from math import comb # import function for combination 
  
  Binomial_Coefficient = comb(T, N) # T Choose N, choose N scenarios from a total of T scenario, Combination = (n!)/(r!(n-r)!)

  return Binomial_Coefficient * (0.25**N) * (0.75**(T-N)) # P(success)^no. of successes needed * P(failure)^no.of failure, return one possible combination, * binomial coefficient to get all possible combinations

print(Mendel_2nd_Law(1,2))


