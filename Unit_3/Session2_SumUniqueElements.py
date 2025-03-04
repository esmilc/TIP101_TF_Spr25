'''
Problem 6: Sum Unique Elements
Write a function sum_of_unique_elements() that takes in two lists of integers, lst1 and lst2, as parameters and returns the sum of the elements that are unique in lst1.

An element is unique if:

it appears exactly once in lst1
it does not appear in lst2
def sum_of_unique_elements(lst1, lst2):
	pass
Example Usage:

lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)
Example Output

3

'''

def sum_of_unique_elements(lst1, lst2):
    set2 = set(lst2)
    freq1 = {}
	
    for elem in lst1:
        freq1[elem] = freq1.get(elem, 0) + 1

    sum = 0

    for num in lst1:
        if freq1[num] == 1 and num not in set2:
            sum += num
    return sum

lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)