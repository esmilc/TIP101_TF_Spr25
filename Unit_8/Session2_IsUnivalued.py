'''
A binary tree is uni-valued if every node in the tree has the same value. Given the root of a binary tree, return True if the given tree is uni-valued and False otherwise.

Evaluate the time complexity of your solution.

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def is_univalued(root):
	pass
Example Usage:

Example Input Tree #1

      1
     / \
    /   \
   1     1
  / \     \
 1   1     1

Input: root = 1
Expected Output: True

Example Input Tree #2

      1
     / \
    /   \
   1     2
  / \     \
 1   1     1

Input: root = 1
Expected Output: False
'''

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def is_univalued(root):
    if not root:
        return True
	
    def check(root, num):
        if not root:
            return True
        return root.val == num and check(root.left, num) and check(root.right, num)
    
    return check(root, root.val)

test = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, TreeNode(1, None, TreeNode(1))))
test2 = None

print(is_univalued(test2))
