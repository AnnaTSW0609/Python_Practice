"""Fibonacci sequence with mortal rabbits"""
""" Starting with one pair of rabbit"""
"""Rabbits take a month to mature"""
"""Then, they give birth to 1 pair of rabbits each month"""
""" Rabbits die after m months"""
"""Each pair is male and female"""
"""Calculate how many rabbits are there after n months"""
""" Fn = Fn-2 + Fn-1 - F(n-(m-1))"""
""" Because rabbits born F(n-(m-1)) month ago will die in Fn (Fn = F(n-(m+1)) + m) month"""

# Fibonacci Series using Dynamic Programming
# Inspiration from https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
# Explanation from https://chrispresso.coffee/2019/02/28/rosalind-mortal-fibonacci-rabbits/
# Algorithm modified from http://saradoesbioinformatics.blogspot.com/2016/06/mortal-fibonacci-rabbits.html

def fibonacci(n, m):

    # Setting the first two fibonacci numbers as 1 and 1 in list L

    L = [1, 1]

    for month in range(1, n+1): # point, don't need to write len(L)-index, just -index will do

        if 2 < month <= m: # no rabbit die yet

            L.append(L[-1]+L[-2])

        elif month == m+1: # only the rabbit in the first gen will die

            L.append(L[-1]+L[-2]-1)

        elif month > m+1: # from now on follow the seq

            L.append(L[-1]+L[-2] - L[-(m+1)])
        
    return L[-1]

print(fibonacci(95,17))
