'''
Problem 4: Move Even Integers
Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and moves all the even integers at the beginning of the list followed by all the odd integers. The function returns any list that satisfies this condition.

def sort_array_by_parity(nums):
    pass
Example Usage:

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))
Example Output:

[2,4,3,1]
# Additional acceptable outputs are [4,2,3,1], [2,4,1,3], and [4,2,1,3]
[0]

'''

def sort_array_by_parity(nums):
    left, right = 0, len(nums)-1
    while left < right:
        if nums[left] % 2 == 1:
            if nums[right] % 2 == 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1
            else:
                right -= 1
                continue
        else:
            left += 1
    return nums

nums = [3,1,2,4,5,9,10,11,20]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))