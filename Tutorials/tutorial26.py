# Map, Filter and Reduce

# Map function
# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
# Applies a given function to all the iterables and return a new list
# Syntax - map(fun, iter)
# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.

#  List in string convert to integer and addition of that list
numbers = ['2','8','12','100']
numbers = list(map(int, numbers))
print(f'List value : {numbers} ')
res = 0
for i in range(len(numbers)):
    res = res + numbers[i]
print(f'Total : {res}')

# List value Square using def function
def sq(a):
    return a * a
num = [2, 4, 6, 3, 7, 44, 7, 88]
square = list(map(sq, num))
print(square)  # Output -> [4, 16, 36, 9, 49, 1936, 49, 7744]

# List value Square using lambda function
num = [2, 4, 6, 3, 7, 44, 7, 88]
square = list(map(lambda x: x * x, num))
print(square)  # Output -> [4, 16, 36, 9, 49, 1936, 49, 7744]

# Square and Cube function
def square(a):
    return a*a
def cube(a):
    return a*a*a
func = [square,cube]
x = [3,5,7,8,9,10]
for i in range(len(x)):
    val = list(map(lambda x: x(i), func))
    print(f'Value is : {val}')

# Two list multiplication using map
list1 = [1,2,3,4,6,7]
list2 = [8,7,5,4,7,8]
res = list(map(lambda x,y: x*y , list1, list2))
print(f"Two list multiplication : {res}")  # Output -> [8, 14, 15, 16, 42, 56]


# Filter function
# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
# filter greater value than 5 in a list
list1 = [2,3,5,7,8,8,23,566]
def is_greater(num):
    return num > 5
result = list(filter(is_greater, list1))
print(f'def : {result}')  # Output -> def : [7, 8, 8, 23, 566]
# OR using lambda function
res = list(filter(lambda x: (x>5), [2,3,5,7,8,8,23,566]))
print(f'Lambda : {res}')  # Output -> Lambda : [7, 8, 8, 23, 566]
# Reduce function
# Addition of list value using reduce function
from _functools import reduce
list2 = [1,2,4,5,7]
num = reduce(lambda x,y: x + y, list2)
print(num)


# Map within Filter
res = list(map(lambda x: x+x, filter(lambda x: (x>=3),[2,3,4,5,6,7])))
print(f'Map within Filter = {res}')  # Output -> Map within Filter = [6, 8, 10, 12, 14]

# Map and Filter within Reduce
res = reduce(lambda x,y: x+y, map(lambda x: x+x, filter(lambda x: (x >= 4), [1,2,3,4,5,76,8,9])))
print(f'Map and Filter within Reduce = {res}')  # Output -> Map and Filter within Reduce = 204