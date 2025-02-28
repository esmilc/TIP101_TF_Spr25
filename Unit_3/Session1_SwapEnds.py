'''
Problem 2: Swap Ends
Write a function swap_ends() that accepts a string my_str as a parameter and returns a new string where the first and last characters from my_str are swapped.

def swap_ends(my_str):
    pass
Example Usage:

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)
'''

def swap_ends(my_str):
    if not my_str:
        return ""
    stringList = list(my_str)
    if len(my_str) == 1:
        return my_str
    temp = stringList[-1]
    stringList[-1] = stringList[0]
    stringList[0] = temp
    return "".join(stringList)

print(swap_ends("Esmil"))

'''
.join() function:
    var = seperator.join(listToJoin)

'''