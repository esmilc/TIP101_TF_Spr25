'''
Problem 5: Palindrome
Write a function first_palindrome() that takes in a list of strings words as a parameter and returns the first palindromic string in the list. A string is palindromic if it reads the same forward and backward. If there is no such string, return an empty string ""

def first_palindrome(words):
    pass
Example Usage:

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)
Example Output:

ada
racecar
'''

def first_palindrome(words):
    for word in words:
        if word[::-1] == word:
            return word
    return ""

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)

def first_palindrome2(words): #This is the more manual way of doing it
    def isPalindrom(word):
        left, right = 0, len(word)-1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True
    for word in words:
        if isPalindrom(word):
            return word
    return ""

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome2(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome2(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome2(words3)
print(palindrome3)