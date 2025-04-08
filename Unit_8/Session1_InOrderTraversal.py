'''
Given the root of a binary tree, return a list representing the inorder traversal of its nodes' values. In an inorder traversal we traverse the left subtree, then the current node, then the right subtree.

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def inorder_traversal(root):
	pass

Example Usage:

Example Input Tree #1: 
     1
      \
       2
      / 
     3    

Input: root = 1
Expected Output: [1,3,2]

Example Input Tree #2 : 

Input: root = None
Output: []

Example Input Tree #3:
    1  

Input: root = 1
Output: [1]


'''

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def inorder_traversal(root):
    lst = []

    def recurse(root):
        if not root:
            return
        recurse(root.left)
        lst.append(root.val)
        recurse(root.right)
    recurse(root)
    return lst

test = TreeNode(1, None, TreeNode(2, TreeNode(3)))

print(inorder_traversal(test))
	