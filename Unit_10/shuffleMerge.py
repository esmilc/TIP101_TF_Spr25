'''
Problem 3: Shuffle Merge
Given the heads of two singly linked lists of integers, merge their nodes to make one list, taking nodes alternately between the two lists. If either list runs out of elements before the other, all nodes from the list with remaining nodes should be appended onto the end of the merged list. Return the head of the merged list.

def shuffle_merge(head_a, head_b):
	pass


Input Lists: List 1: 1 —> 2 —> 3, List 2: 4 —> 5 —> 6
Input: head_a = 1, head_b = 4
Expected Return value: 1
Expected Result List: 1 —> 4 —> 2 —> 5 —> 3 —> 6

Input Lists: List 1: 1 —> 2 —> 3, List 2: 4
Expected Return value: 1
Expected Result List: 1 —> 4 —> 2 —> 3
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def printLL(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next
        


def shuffle_merge(head_a, head_b):
    curr1, curr2 = head_a, head_b
    if not head_b:
        return head_a
    if not head_a:
        return head_b
    newLL = ListNode(0) #We must return newLL.next
    tail = newLL
    while curr1 and curr2:
        tail.next = curr1
        curr1 = curr1.next
        tail = tail.next

        tail.next = curr2
        curr2 = curr2.next
        tail = tail.next
    
    if curr1:
        tail.next = curr1
    if curr2:
        tail.next = curr2
    return newLL.next

list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(4, ListNode(5, ListNode(6)))

list3 = ListNode(1, ListNode(2, ListNode(3)))
list4 = ListNode(4)

printLL(shuffle_merge(list1, list2))

printLL(shuffle_merge(list3, list4))

