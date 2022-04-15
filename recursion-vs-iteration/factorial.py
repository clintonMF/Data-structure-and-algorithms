# in this file i would create 2 functions to calculate the factorial of numbers
# the first function would be a recursive function and the other an iterative function

def factorial_rec(n):
    """A function that gives the factorial of the input number (n) using recursion"""
    assert n>=0 and int(n) == n, "the number must be positive integer only"
    if n in [0,1]:
        return 1
    else:
        return n*factorial_rec(n-1)
    
print(factorial_rec(5))


def factorial_iter(n):
    """ 
    A function that gives the factorial of the input number (n) using iterations
    """
    assert n>=0 and int(n)==n, 'n must be a positive integers'
    i = 1
    fact = 1
    while i < (n+1):
        fact *= i
        i += 1
    return fact


print(factorial_iter(5))
    