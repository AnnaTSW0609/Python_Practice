"""Fibonacci sequence"""
""" Starting with one pair of rabbit"""
"""Rabbits take a month to mature"""
"""Then, they give birth to k pair(s) of rabbits each month"""
"""Each pair is male and female"""
"""Calculate how many rabbits are there after n months"""
""" Fn = 2*Fn-2 + Fn-1"""

# Fibonacci Series using Dynamic Programming
# Inspiration from https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

def fibonacci(n, k):

    # Setting the first two fibonacci numbers as 1 and 1 in list L

    L = [1, 1]

    for i in range (1, n + 1):

        if i == 1 or i == 2:

            pass
        

        # elif i == 3: # You don't actually need this for the computer to understand

             # item = 1 + 1*k

             # L.append(item)


        else:

            item = L[len(L)-1] + L[len(L)-2] * k

            L.append(item)

    return(L[len(L)-1])
        
print(fibonacci(32, 2))  


    
    
