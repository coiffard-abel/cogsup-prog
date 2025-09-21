"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""

def is_factor(d, n):
    return not(bool(n%d))

def is_prime(n):
    for i in range(n//2):
        if is_factor(i+2, n):
            return False
    return True

list_of_primes = [i+1 for i in range(10000) if is_prime(i+1)]
print(list_of_primes)