'''
roblem 1: Contains Duplicates
Given an integer array nums, return True if any value appears at least twice in the array, and return False if every element is distinct.

def contains_duplicate(nums):
	pass

Example Usage:

Example #1: 
Input: nums = [1,2,3,1]
Output: True

Example #2:
Input: nums = [1,2,3,4]
Output: False

Example #3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: True

'''

def contains_duplicate(nums):
    looked = set()
    for num in nums:
        if num in looked:
            return True
        looked.add(num)
    return False

nums = [1,2,3,1]
print(contains_duplicate(nums))
nums = [1,2,3,4]
print(contains_duplicate(nums))
nums = [1,1,1,3,3,4,3,2,4,2]
print(contains_duplicate(nums))

