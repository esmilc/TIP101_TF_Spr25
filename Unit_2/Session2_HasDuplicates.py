'''
Problem 6: Has Duplicates
Write a function hasDuplicates() that takes in a list of integers nums and a positive number k as parameters. The function returns True if the list contains any duplicate elements within the range 0 to k (inclusive). If k is greater than the list's length, the solution should check for duplicates in the complete list. The function should return False otherwise.

def hasDuplicates(nums, k):
	pass
Example Usage:

nums = [5, 6, 8, 2, 6, 4, 9]
check1 = hasDuplicates(nums, 3)
print(check1)
check2 = hasDuplicates(nums, 5)
print(check2)
Example Output:

False
True

'''

def hasDuplicates(nums, k):
	freqDict = {}
	for i in range(k):
		freqDict[nums[i]] = freqDict.get(nums[i], 0) + 1
	for freq in freqDict.values():
		if freq > 1:
			return True
	return False

nums = [5, 6, 8, 2, 6, 4, 9]
check1 = hasDuplicates(nums, 3)
print(check1)
check2 = hasDuplicates(nums, 5)
print(check2)