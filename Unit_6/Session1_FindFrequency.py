'''
Given the head of a linked list and a value val, return the frequency of val in the list. Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def count_element(head, val):
	pass
Example Usage:

# Input List: 3 -> 1 -> 2 -> 1
# Input: head = 3, val = 1
Example Output:

# 2
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def count_element(head, val):
    count = 0
    curr = head
    while curr:
        if curr.value == val:
            count += 1
        curr = curr.next
    return count

test1 = Node(3, Node(1, Node(2, Node(1))))
print(count_element(test1, 1))