'''
Problem 1: String to Integer
Write a function string_to_integer_mapping() that takes in a string of digits s as a parameter and returns a list where each element is the integer value of the corresponding digit in the string.

def string_to_integer_mapping(s):
    pass
Example Input: s="12345"
Example Output: [1, 2, 3, 4, 5]
'''
def string_to_integer_mapping(s):
    lst = []
    for char in s:
        lst.append(int(char))
    return lst

s = "12345"
print(string_to_integer_mapping(s))