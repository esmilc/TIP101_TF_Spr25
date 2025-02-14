'''
Write a function sum_ten() that returns the sum of numbers from 1 to 10.

def sum_ten():
    pass
Example Usage: output = sum_ten()
Example Result: output = 55

'''

def sum_ten():
    count = 0
    for i in range(10):
        count += (i+1)
    return count

output = sum_ten()
print(output)

'''
My approach was to use a for loop which goes from 0 to 9. I initialized a variable called count
which gets added by the count variable

'''