# An algorithm that uses double recursion has a big O of 2 raised to power of N
# an example of such algorithm is the algorithm for fibonacci sequence

def fibonacci(n):
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(7))