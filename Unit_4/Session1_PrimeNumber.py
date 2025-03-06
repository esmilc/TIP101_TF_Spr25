'''
Problem 1: Prime Number
Write a function is_prime() that takes in a positive integer n and returns True if it is a prime number and False otherwise. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

def is_prime(n):
    pass
Example Usage:

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))
Example Output:

True
False
False
'''

def is_prime(n):
    for num in range(2, int(n**0.5)+1):
        if n % num == 0:
            return False
    return True

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))

'''
A neat trick: you only have to check numbers from 2 until the square root of the number to check

if that number divides the og number cleanly return false

return true at the end bc nothing was flagged
'''