'''
Write a function get_evens() that takes in a list of integers lst as a parameter and returns a list of all even numbers in the list.

def get_evens(lst):
    pass
Example Usage:

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)
Example Output:

[2, 4]

'''

def get_evens(lst):
    return [num for num in lst if num % 2 == 0]

test = [1,2,3,4]

print(get_evens(test))

'''
Decided to practice my list comprehension, a simpler way to do it is as follows

evens_list = []
for num in lst:
    if num % 2 == 0: #If the number is cleanly divisible by 2...its even and therefore should go in the list
        evens_list.append(num)
return evens_list

'''
