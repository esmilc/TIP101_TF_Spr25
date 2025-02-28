'''
Problem 5: First Unique
Write a function first_unique_char() that given a string my_str as a parameter, it finds the first non-repeating character in it and returns its index. If it does not exist, then return -1.

def first_unique_char(my_str):
    pass
Example Usage:

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))
Example Output

0
2
-1
'''

def first_unique_char(my_str):
    freqDict = {}

    for char in my_str:
        freqDict[char] = freqDict.get(char, 0) + 1
    
    for index, char in enumerate(my_str):
        if freqDict[char] == 1:
            return index
    return -1

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))

'''
I'm first making a frequency dictionary to store the frequency of the characters

Then, I go though the string using enumerate(STRING), this is just like .items() in a dictionsty where it is a index, char being returned. There i'm going in order checking if
the frequency of the character is 1, if so return index


'''