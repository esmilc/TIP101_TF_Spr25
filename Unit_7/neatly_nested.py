'''
Problem 1: Neatly Nested
Given a string, return True if it is a nesting of zero or more pairs of parentheses. Return False otherwise. A valid pair of parentheses is defined as (). The input string will only contain the characters ( or ). Your solution must be recursive.

Evaluate the time and space complexity of your solution.

def is_nested(paren_s):
	pass
Example Usage:

# Example Input: "(())"
Example Output:

# Expected Output: True
'''

def is_nested(word):
    if not word:
        return True
    if len(word) % 2 == 1:
        return False
    if word[0] == "(" and word[-1] == ")":
        return is_nested(word[1:-1])
    else:
        return False

test = "()"
print(is_nested(test))
    