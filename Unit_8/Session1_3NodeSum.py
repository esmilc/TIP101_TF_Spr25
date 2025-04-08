'''
Given the root of a binary tree that has exactly 3 nodes: the root, its left child, and its right child, return True if the value of the root is equal to the sum of the values of its two children. Return False otherwise.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
	pass

Example Usage:

Example Input Tree #1: 
  10
 /  \
4    6
Input: root = 10
Expected Output: True

Example Input Tree #2: 
  5
 / \
3   1
Input: root = 5
Expected Output: False
'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
	return (root.val == (root.left.val + root.right.val))

test1 = TreeNode(5, TreeNode(3), TreeNode(2))
test2 = TreeNode(5, TreeNode(1), TreeNode(2))

print(check_tree(test1))
print(check_tree(test2))