"""Computing Summation of probability"""
"""Given number of parent of each of the 6 possible genotype"""
"""Return expected number of offspring that are dominant"""

# take a probability

number = "18076 17624 16519 18578 19320 18215"

# numbers correspond to number of couple with a certain genotype

# AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa

number = list(map(int, number.split())) # switch to integer type

total = sum(number)

ans = 2*total * ((number[0] + number [1] + number [2])/total + (number[3]*3)/(4*total) + 0.5*number[4]/total)

print(ans)


# try summation, not necessarily useful for this question 

def summation(n):

    Sum = 0

    for i in range(1, (n+1)):

        Sum += i*(1/n) # assuming equal prob for every outcome

    return Sum
