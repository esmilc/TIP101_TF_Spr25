'''
Problem 10: FizzBuzz
Write a function fizzbuzz() that takes in an integer n as a parameter and prints the numbers from 1 to n.
For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.

def fizzbuzz(n):
    pass
Example Usage: fizzbuzz(13)

Example Output:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
'''

def fizzbuzz(n):
    for num in range(1, n+1):
        if num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz(13)