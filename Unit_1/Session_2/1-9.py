'''
Problem 9: Divisors
Write a function find_divisors() that takes in an integer n as a parameter that returns a list of all divisors of n.

def find_divisors(n):
    pass
Example Usage:

lst = find_divisors(6)
print(lst)
Example Output:

[1, 2, 3, 6]
'''

def find_divisors(n):
    return [num for num in range(1, n+1) if n % num == 0]

print(find_divisors(6))

'''
One thing to look at is to make sure bounds are from 1 to n+1 if not you 
will get either a division by 0 error and/or not include n
'''