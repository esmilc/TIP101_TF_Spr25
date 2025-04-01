'''
Problem 5: Binary Search I
Binary search is a searching algorithm that allows us to efficiently find the index of a given value within a sorted list. Given the pseudo code for binary search below, implement an iterative (non-recursive) implementation of binary search. There is also a recursive alternative that we’ll cover in the session 2 problem set!

Evaluate the time and space complexity of your implementation.

def binary_search(lst, target):
	# Initialize a left pointer to the 0th index in the list
	# Initialize a right pointer to the last index in the list
	
	# While left pointer is less than right pointer:
		# Find the middle index of the array
		
		# If the value at the middle index is the target value:
			# Return the middle index
		# Else if the value at the middle index is less than our target value:
			# Update pointer(s) to only search right half of the list in next loop iteration
		# Else
			# Update pointer(s) to only search left half of the list in next loop iteration
	
	# If we search whole list and haven't found target value, return -1

def binary_search(lst, target):
	pass
Example Usage:

# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
Example Output:

# Expected Output: 5
# Explanation: 11 has index 5 in the list
'''

def binary_search(lst, target):
    if not lst:
        return False
    left, right = 0, len(lst)-1
    mid = (left+right) // 2
	
    if lst[mid] == target:
        return True
    elif lst[mid] < target:
        return binary_search(lst[mid+1:], target)
    else:
        return binary_search(lst[:mid], target)
    
lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 1
print(binary_search(lst, target))
    