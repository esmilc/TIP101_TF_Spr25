'''
Given the head of a singly linked list, return True if the values of the linked list are palindromic and False otherwise. Use the two-pointer technique in your solution.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def is_palindrome(head):
	pass
Example Usage:

# Input List:
# 1 -> 2 -> 1
# Input: head = 1
Example Output:

# True

'''

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def is_palindrome(head):
	#First get to the middle and reverse the first half as you do it
    curr = head
    slowPrev, slowCurr, slowNext, fast = curr, curr, curr.next, curr
    odd = None

    while fast.next and fast.next.next:
        fast = fast.next.next
        slowCurr = slowNext
        slowNext = slowNext.next
        slowCurr.next = slowPrev
        slowPrev = slowCurr
    if fast.next:
        odd = False
    else:
        odd = True

    left = None
    if odd:
        left = slowCurr.next #we want to skip the middle one
    else:
        left = slowCurr
    right = slowNext
    while left and right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.next

    return True
        

        



test = Node(1, Node(2, Node(3, Node(2, Node(1)))))
test2 = Node(2, Node(1, Node(2)))
print(is_palindrome(test2))
'''
Odd Check:
fast pointer will be pointing at last element, meaning fast.next wont exist

Even Check:
fast pointer will be pointing second to last element meaning fast.next exists but fast.next.next doesnt exist


'''