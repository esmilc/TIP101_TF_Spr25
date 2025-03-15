'''
Problem 3: Add First
Write a function add_first() that takes in a head of a linked list and a new_node from the Node class as parameters.

It should insert new_node as the new head of the linked_list. The function returns new_node.

Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
		
def add_first(head, new_node):
	pass
Example Usage:

# Using the Linked List from Problem 2
print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)
Example Output:

Jigglypuff -> Wigglytuff 
Ditto -> Jigglypuff
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
		
def add_first(head, new_node):
	new_node.next = head
	return new_node

def printLL(head):
	while head:
		print(head.value, end="\t")
		head = head.next

head = Node(1, Node(2, Node(3)))
head = add_first(head, Node(0))

printLL(head)