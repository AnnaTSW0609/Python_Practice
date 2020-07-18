"""Computing probability of an offspring carrying a dominant allele A"""

k = 2 # Number of AA
m = 2 # Number of Aa
n = 2 # Number of aa

# Apparently it would be faster to deduct the recessive cases from the dominant cases

T = (k+m+n)*(k+m+n-1) # first seletion: 1/6, second selection: 1/5

Recessive = m*(m-1)*0.25 + n*m + n*(n-1) # All recessive cases

P_Rec = Recessive/T

print("{:.5f}".format(1-P_Rec))
