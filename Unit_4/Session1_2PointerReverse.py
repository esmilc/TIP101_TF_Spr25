'''
Problem 2: Two-Pointer Reverse List
Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. lst[::-1]).

Instead, use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.

def reverse_list(lst):
    pass
Example Input: [1, 2, 3, 4, 5]
Example Output: [5, 4, 3, 2, 1]


'''

def reverse_list(lst):
    left, right = 0, len(lst)-1
    while left < right:
        temp = lst[left]
        lst[left] = lst[right]
        lst[right] = temp
        left += 1
        right -= 1

lst = [1, 2, 3, 4, 5, 6]
print(lst)
reverse_list(lst)
print(lst)