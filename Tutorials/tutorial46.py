# Generator
# Iterable - __inter__() and __ getitem__()
# Iterator - __next__()
# There is a lot of work in building an iterator in Python. We have to implement a class with __iter__() and __next__() method, keep track of internal states, and raise StopIteration when there are no values to be returned.

for i in range(10):
    print(i, end=' ')

print('\n')

# Generator is a one time iterator
def gen(n):
    for i in range(n):
        yield i # yield is a generator
g = gen(2)
print(g.__next__())  # Output -> 0
print(g.__next__())  # Output -> 1
# print(g.__next__())  # Output -> StopIteration


i = 'Sandip'
ier = iter(i)  # Define inter()
print(ier.__next__())  # Output -> S
print(ier.__next__())  # Output -> a
print(ier.__next__())  # Output -> n