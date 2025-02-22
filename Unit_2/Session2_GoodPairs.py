'''
Write a function numIdenticalPairs() that takes in a list of integers nums and returns the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.

def numIdenticalPairs(nums):
    pass
Example 1:

nums = [1,2,3,1,1,3]
ans = numIdenticalPairs(nums)
# ans == 4
Explanation:

nums[0] == 1
- nums[0] == nums[3]
- nums[0] == nums[4]
Good Pairs: (0,3) and (0,4) --> count = 2

nums[1] == 2
No identical pairs found

nums[2] == 3
- nums[2] == nums[5]
Good Pairs: (2,5) --> count = 3

nums[3] == 1
*will not check any any indices less than current index*
- nums[3] == nums[4]
Good Pairs: (3,4) --> count = 4

nums[4] == 1
*will not check any any indices less than current index*
No identical pairs found

nums[5] == 3
*will not check any any indices less than current index*
No identical pairs found
Example 2:

nums = [1,1,1,1]
ans = numIdenticalPairs(nums)
# ans == 6
Example 3:

nums = [1,2,3]
ans = numIdenticalPairs(nums)
# ans == 0
'''

def numIdenticalPairs(nums):
    numGoodPairs = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                numGoodPairs += 1
    return numGoodPairs

nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))

nums = [1,2,3]
print(numIdenticalPairs(nums))

nums = [1,1,1,1]
print(numIdenticalPairs(nums))