# Write a function that calculates the nth Fibonacci number in O(n) time or 
# better without using any "for" or "while" loops. (Feel free to use the space below or submit a link to your work.)

# - You can use any programming language you like.
# - The function you submit shall be runnable. *

#create global memeory to retain information
temp = {0: 0, 1: 1}

def calc_fib(n):
     
     # return from memory
     if n in temp:  
         return temp[n]
     
     # repeat
     temp[n] = calc_fib(n - 1) + calc_fib(n - 2)  
     return temp[n]

