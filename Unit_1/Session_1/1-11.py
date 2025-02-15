'''
Write a function counter() that uses the range function to print numbers between 1 and a given stop value (inclusive).

def counter(stop):
    pass
Example Usage: counter(7). Example Output:

1
2
3
4
5
6
7
'''

def counter(stop):
    for num in range(1, stop+1):
        print(num)

counter(7)

'''
My approach is to use a for loop ranging from 1 to stop + 1 (since the ending parameter is non-
inclusive) and then printing 1. Another approach would of been to have the for loop go till
stop and just add 1 to the variable that I'm printing

'''