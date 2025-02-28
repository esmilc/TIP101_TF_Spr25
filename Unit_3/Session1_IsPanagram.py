'''
Problem 3: Is Pangram
Write a function is_pangram() that takes in a string my_str as a parameter and returns True if the string is a pangram and False if not. 
A pangram is a sentence containing every letter in the English alphabet.

def is_pangram(my_str):
    pass
Example Usage:

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))
Example Output:

True
False

'''

def is_pangram(my_str):
    setLetters = set() #My set will have all letters lowercase
    for char in my_str:
        if char.isalpha():
            setLetters.add(char.lower())
    
    return len(setLetters) == 26

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))

'''
My set is going to contain letters that are in the string, all lower case
'''