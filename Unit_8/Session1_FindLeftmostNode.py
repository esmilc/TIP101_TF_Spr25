'''
Given the root of a binary tree, write a function that finds the value of the left most node in the tree.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
	pass

Example Usage:


Example Input Tree #1: 

      1
     / \
    /   \
   2     5
  / \    
 4   3    

Input: root = 1
Expected Output: 4

Example Input Tree #2: 

     1
      \
       2
      / 
     3    

Input: root = 1
Expected Output: 1

Example Input Tree #3: 

Input: root = None
Output: None

'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    if not root:
        return None
    return root.val if not root.left else left_most(root.left)


test1 = TreeNode(5, TreeNode(5))
test2 = TreeNode(5, TreeNode(1), TreeNode(2))
test3 = TreeNode(5, TreeNode(3, TreeNode(2)), TreeNode(2))

print(left_most(test1))
print(left_most(test2))
print(left_most(test3))