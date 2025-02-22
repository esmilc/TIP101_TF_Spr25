'''
Problem 8: First Unique Items
Write a function find_unique_items() that takes two lists list_a and list_b as parameters. The function identifies unique items from the lists and returns a dictionary with the items as keys and a boolean value as the value indicating whether the item is unique to the first list (True) or not (False).

def find_unique_items(list_a, list_b):
    pass
Example Input:

list_a = ["apple", "banana", "carrot"]
list_b = ["apple", "banana", "date"]
Example Output: {"carrot": True, "date": False}


'''

def find_unique_items(list_a, list_b):
    dictToReturn = {}
    setA = set(list_a)
    setB = set(list_b)

    for item in list_a:
        if item not in setB:
            dictToReturn[item] = True

    for item in list_b:
        if item not in setA:
            dictToReturn[item] = False
    return dictToReturn

list_a = ["apple", "banana", "carrot"]
list_b = ["apple", "banana", "date"]
print(find_unique_items(list_a, list_b))
'''
I'm planning on using sets to improve time complexity


'''