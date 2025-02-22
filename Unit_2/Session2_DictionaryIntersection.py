'''
Problem 2: Dictionary Intersection
Write a function dict_intersection() that takes in two dictionaries as parameters and returns a new dictionary containing the key-value pairs found in both dictionaries.

def dict_intersection(d1, d2):
    pass
Example Input:

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4}
Example Output: {'b': 2}
'''
def dict_intersection(d1, d2):
    intersectionDict = {}
    for key, val in d1.items():
        if d2.get(key, None) == val:
            intersectionDict[key] = val
    return intersectionDict

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4}
print(dict_intersection(d1, d2))