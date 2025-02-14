'''
Problem 14: Total Sum in Range
Write a function sum_range() that returns the sum of numbers from a given start value to a given stop value (inclusive).

def sum_range(start, stop):
    pass
Example Usage: sum = sum_range(3, 9)
Example Result: sum = 42
'''

def sum_range(start, stop):
    count = 0
    for num in range(start, stop+1):
        count += num
    return count

sum = sum_range(3,9)
print("The sum of numbers between 3 and 9 is:", sum)