'''
Problem 5: Replace Node
Using the Node class, write a function ll_replace() that takes a head of a linked list and two values, original and replacement as parameters.

The function updates any node with value original to have value replacement.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_replace(head, original, replacement):
	pass
Example Usage:

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_replace(head, original, replacement):
    while head and head.value != original:
        head = head.next
	#here, either we went through the whole lis or we are at the right one
    
    if not head:
          return -1 #It wasnt found
    head.value = replacement

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"
print(head.value)