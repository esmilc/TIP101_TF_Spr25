'''
Problem 3: Reverse Letters
Write a function reverse_only_letters() that takes in a string s as a parameter. The function reverses the order of the letters in the string and returns the new string. Non-letter characters should remain in their original positions.

def reverse_only_letters(s):
    pass
Example Usage:

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
Example Output: j-Ih-gfE-dCba


'''

def reverse_only_letters(s):
    sList = list(s)

    left, right = 0, len(s) -1

    while left < right:
        if sList[left] == "-":
            left += 1
            continue
        if sList[right] == "-":
            right -= 1
            continue
        temp = sList[left]
        sList[left] = sList[right]
        sList[right] = temp
        left += 1
        right -= 1
    return ''.join(sList)

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)