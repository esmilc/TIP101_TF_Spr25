'''
Problem 5: Reverse Vowels
Write a function reverse_vowel() that takes in a string s as a parameter and returns a string with all the vowels in the string reversed. The consonants should remain in the same position. For this question, we consider a, e, i, o, and u as vowels but not y. The vowels can appear in both lower and upper cases, more than once.

def reverse_vowels(s):
    pass
Example Usage:

s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)

s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2)
Example Output:

holle
leotcede

'''

def reverse_vowels(s):
    vow = set(["a", "e", "i", "o", "u"])
    lst = list(s)
    left, right = 0, len(s) -1

    while left < right:
        if lst[left].lower() not in vow:
            left += 1
        elif lst[right].lower() not in vow:
            right -= 1
        else:
            temp = lst[left]
            lst[left] = lst[right]
            lst[right] = temp
            left += 1
            right -= 1
    return "".join(lst)


s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)

s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2)