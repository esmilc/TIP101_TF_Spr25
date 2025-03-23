'''
Problem 3: Remove Tail
The following code attempts to remove the tail of a singly linked list. However, it has a bug!

Step 1: Copy this code into Replit.

Step 2: Create your own test cases to run the code against, and use print statements and the stack trace to identify and fix the bug so that the function correctly removes the tail of the list.

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
        
# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next: 
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head
Example Usage:

# Input List: 1 -> 2 -> 3 -> 4
# Input: head = 1
Example Output:

# Expected Return Value: 1
# Expected Result List: 1 -> 2 -> 3
'''

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
        
# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next: #HERE WAS THE BUG!!!!!!! changed from while current.next
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head

test1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))

print_list(test1)
remove_tail(test1)
print_list(test1)