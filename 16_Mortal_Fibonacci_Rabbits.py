"""Fibonacci sequence with mortal rabbits"""
""" Starting with one pair of rabbit"""
"""Rabbits take a month to mature"""
"""Then, they give birth to 1 pair of rabbits each month"""
""" Rabbits die after m months"""
"""Each pair is male and female"""
"""Calculate how many rabbits are there after n months"""
""" Fn = Fn-2 + Fn-1 - F(n-(m-1))"""
""" Because rabbits born F(n-(m-1)) month ago will die in Fn (Fn = F(n-(m-1)) + m) month"""

# Fibonacci Series using Dynamic Programming
# Inspiration from https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
# with help from https://chrispresso.coffee/2019/02/28/rosalind-mortal-fibonacci-rabbits/

def fibonacci(n, m):

    # Setting the first two fibonacci numbers as 1 and 1 in list L

    L = [1, 1]

    for i in range (1, n + 1):

        if i == 1 or i == 2:

            pass
        

        # elif i == 3: # You don't actually need this for the computer to understand

             # item = 1 + 1*k

             # L.append(item)


        else:

            item = L[len(L)-1] + L[len(L)-2] - L[len(L)-(m-1)]

            L.append(item)

    return (L[len(L)-1])
        
print(fibonacci(6, 3))  
