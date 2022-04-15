# this .py file is dedicated to showing the difference between 
# Recursion and iteration


def powertwo_rec(n):
    """
    A recursive function that gives the value of 2 raised to the
    power of the input (n)
    """
    if n==0:
        return 1
    else:
        return 2*powertwo_rec(n-1)
    
print(powertwo_rec(4))

def powertwo_iter(n):
    """
    A function that uses iteration to give the value of 2 raised
    to the power of the input (n)
    """
    i = 0
    power = 1
    while i<n:
        power *= 2
        i += 1
    return power

print(powertwo_iter(4))