'''
Write a function get_last() that takes in a list as a parameter and returns the last item in the list. Return None if the list is empty.
def get_last(lst):
    pass
Example Input: [3,1,6,7,5]
Example Output: 5
'''


def get_last(lst):
    if not lst:
        return None
    else:
        return lst[-1]

print(get_last([3,1,6,7,5]))

'''
If not lst just checks if the list has anything in it, so if this condition is true then there is nothing 
in the list and we are going to return none, per the instructions. Else, return lst[-1] which automatically
grabs the last element in the list in python

'''