'''
Problem 1: Subsequence
Write a function is_subsequence() that takes in a list of integers lst and a list of integers sequence as parameters. Given these two lists, determine whether the sequence list is a subsequence of the lst list. A subsequence of a list is a set of numbers that aren't necessarily adjacent but are in the same relative order as they appear in the list. Return True if sequence is a subsequence, and False otherwise.

def is_subsequence(lst, sequence):
    pass
Example Usage:

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))
Example Output: True
'''

def is_subsequence(lst, sequence):
    subPtr = 0
    lstPtr = 0
    while subPtr < len(sequence) and lstPtr < len(lst):
        if sequence[subPtr] == lst[lstPtr]:
            subPtr += 1
            lstPtr += 1
        else:
            lstPtr += 1
    if subPtr < len(sequence):
        return False
    return True

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))

'''
Thought Process:

Have two pointers that go through each list independently.

If the value at both pointers equal each other, move both pointers one over.
If they don't go ahead and only move the lst pointer, bc ALL values in the subsequece must be in lst so we need to find it in lst

Remember, we are wrapping them in a while loop, so once one of those pointers go out of bound exit to avoid an index out of range error

If the pointer for the substring is < len(subseq)...we never found the value in lst(bc we kept moving one over till the end) -> Retrn False

If not then return true


'''