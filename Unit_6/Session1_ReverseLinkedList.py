'''
Given the head of a singly linked list, reverse the list, and return the reversed list. You must reverse the list in place. Return the head of the reversed list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def reverse(head):
	pass
Example Usage:

# Input List: 1 -> 2 -> 3 -> 4
# Input: head = 1
Example Output:

# Expected Return Value: 4
# Expected Result List: 4 -> 3 -> 2 -> 1
'''

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def reverse(head):
    if not head:
        return None #empty list
    if not head.next:
        return head #only one node
    prev, curr = None, head
    while curr:
        Next = curr.next
        curr.next = prev
        prev = curr
        curr = Next
    return prev

def printLL(node):
    curr = node
    while curr:
        print(curr.value, end=" -> " if curr.next else "\n")
        curr = curr.next

test = Node(1, Node(2, Node(3, Node(4))))
printLL(reverse(test))





    