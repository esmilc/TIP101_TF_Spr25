'''
Problem 2: Remove Duplicates
Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes all duplicates in the list. The function returns the modified list.

def remove_duplicates(nums):
    pass
Example Input: nums = [1,1,1,2,3,4,4,5,6,6]
Example Output: no_dups = [1,2,3,4,5,6]
'''
def remove_duplicates(nums):
    index = 0

    for i in range(1, len(nums)):
        if nums[index] != nums[i]:
            index += 1
            nums[index] = nums[i]
    return nums[:index+1]

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))