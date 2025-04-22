'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', return True if the input string is valid and False otherwise.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
def is_valid(s):
	pass

Example Usage:

Example #1:
Input: s = "()"
Expected Output: True

Example #2:
s = "()[]{}"
Expected Output: True

Example #3: 
s = "(())"
Expected Output: True

Exampel #4:
s = "(]"
Expected Output: False

'''

def is_valid(s):
    complements = {")" : "(", "}" : "{", "]" : "["}
    stack = []

    for char in s:
        if char == "{" or char == "[" or char == "(":
            stack.append(char)
        elif char in complements:
            if stack.pop() != complements[char]:
                return False
    
    if len(stack) == 0:
        return True
    return False

s1 = "()"
s2 = "()[]{}"
s3 = "(())"
s4 = "(]"

print(is_valid(s1))
print(is_valid(s2))
print(is_valid(s3))
print(is_valid(s4))