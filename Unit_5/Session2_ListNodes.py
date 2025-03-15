'''
Problem 6: List Nodes
Write a function listify_first_n() that takes in a head of a linked list and a non-negative integer n as parameters.

The function returns a list of values of the first n nodes.

If n is greater than the length of the linked list, return a list of the values of all nodes in the linked list.
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def listify_first_n(head, n):
	pass
Example Usage:

# linked list: a -> b -> c
head = a
lst = listify_first_n(head,2)
print(lst)

# linked list: j -> k -> l 
head2 = j
lst2 = listify_first_n(head2,5)
print(lst2)
Example Output:

[`a`, `b`]
[`j`, `k`, `l`]
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def listify_first_n(head, n):
	lst = []
	count = 0
	curr = head
	while curr and count < n:
		lst.append(curr.value)
		count += 1
		curr = curr.next
	return lst

test1 = Node("a", Node("b", Node("c")))
test2 = Node("j", Node("k", Node("l")))

print(listify_first_n(test1, 2))
print(listify_first_n(test2, 5))