'''
Problem 4: Reverse String
Write a function reverse_string() that takes a string my_str as a parameter and returns the string reversed.

def reverse_string(my_str):
    pass
Example Usage:

my_str = "live"
print(reverse_string(my_str))
Example Output: evil
'''

def reverse_string(my_str):
    return my_str[::-1]


my_str = "live"
print(reverse_string(my_str))