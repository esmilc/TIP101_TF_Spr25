'''
Problem 7: Binary Tree Size
Given the root of a binary tree, write a function size() that returns the number of nodes in the binary tree.

Evaluate the time complexity of your function.

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def size(root):
	pass

Example Usage:

Example Input Tree #1: 

      4
     / \
    /   \
   2     5
  / \    
 1   3    

Input: root = 4
Expected Output: 5

Example Input Tree #2: 

Empty tree (None)
Input: root = None
Expected Output: 0

'''

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def size(root):
    if not root:
        return 0
    return 1 + size(root.left) + size(root.right)

test = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))

print(size(test))