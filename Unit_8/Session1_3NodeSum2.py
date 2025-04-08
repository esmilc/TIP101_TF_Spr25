'''
Given the root of a binary tree that has at most 3 nodes: the root, its left child, and its right child, return True if the value of the root is equal to the sum of the values of its two children. Return False otherwise.

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
 /  
10    
Input: root = 10
Expected Output: True

Example Input Tree #2: 
  5
 / \
3   2
Input: root = 5
Expected Output: True

Example Input Tree #3: 
  5
   \
    2
Input: root = 5
Expected Output: False

Example Input Tree #4: 
Empty Tree (None)
Input: root = None
Expected Output: False

'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    leftChild = root.left.val if root.left else 0
    rightChild = root.right.val if root.right else 0
    return (root.val == (leftChild + rightChild))
     

test1 = TreeNode(5, TreeNode(5))
test2 = TreeNode(5, TreeNode(1), TreeNode(2))
test3 = TreeNode(5, TreeNode(3), TreeNode(2))

print(check_tree(test1))
print(check_tree(test2))
print(check_tree(test3))