'''
A variation of the two-pointer technique introduced in Unit 4 is to have a slow and a fast pointer that increment at different rates. Given the head of a linked list, use the slow-fast pointer technique to find the middle node of a linked list. If there are two middle nodes, return the second middle node.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
	pass
Example Usage:

# Input List:
# 1 -> 2 -> 3
# Input: head = 1
Example Output:

# Expected Return Value: 2
'''
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value

test = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(find_middle_element(test))
'''
thought process us to use a fast pointer that moves twice as fast as the slow pointer

so we need fast.next and fast.next.next bc:

If you only used fast.next.next without first checking fast.next, there could be cases
(especially in short or even-length lists) where fast.next is None. Trying to access 
None.next would raise an AttributeError.
'''