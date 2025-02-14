'''
Problem 15: Negative Numbers
Write a function print_negatives() that takes a list of integers lst and prints all negative numbers in the list.

def print_negatives(lst):
Example Usage: print_negatives([3,-2,2,1,-5])
Example Output:

-2
-5
Example Usage: print_negatives([1,2,3,4,5])
Example Output:

None
'''

def print_negatives(lst):
    [print(num) for num in lst if num < 0]

lst = [3, -2, 2, 1, -5]
print_negatives(lst)

'''
I decided to print my list comprehension for this one. Alternate approacg
    for num in lst:
        if num < 0:
            print(num)
'''