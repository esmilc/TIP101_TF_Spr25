'''
Write a function multiples_of_five() that prints out multiples of 5 between 1 and 100 (inclusive).

def multiples_of_five():
    pass
Example Output:

5
10
15
20
25
....
90
95
100
'''

def multiples_of_five():
    for num in range(101):
        if num % 5 == 0: #this checks if its cleanly divisible by 5
            print(num)
multiples_of_five()