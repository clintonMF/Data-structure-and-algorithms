# in this file i would create 2 functions to calculate the nth term of the fibonacci sequence
# the first function would be a recursive function and the other an iterative function

def fibonacci_rec(n):
    """
    A recursive function that finds the nth value of the fibonacci sequence
    """
    if n in [0,1]:
        return n
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)
    
print(fibonacci_rec(6))


def fibonacci_iter(n):
    """
    An iterative function that finds the nth value of the fibonacci sequence
    """
    num1 = 0
    num2 = 1
    for i in range(n):
        num1,num2= num2, num1+num2
    return num1

print(fibonacci_iter(6))