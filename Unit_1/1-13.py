'''
Problem 13: Total Sum
Write a function sum_positive_range() that returns the sum of numbers from 1 to a given stop value (inclusive).

def sum_positive_range(stop):
    pass
Example Usage: sum = sum_positive_range(6)
Example Result: sum = 21
'''

def sum_positive_range(stop):
    count = 0
    for num in range(stop):
        count += (num + 1)
    return count

sum = sum_positive_range(6)
print("Sum is:", sum)