# Enumerate function
# In Enumerate function we can access index with value
# A lot of times when dealing with iterators, we also get a need to keep a count of iterations. Python eases the programmers’ task by providing a built-in function enumerate() for this task.
# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
# Syntax - enumerate(iterable, start=0)

i = ['Sandip', 'Swapnil','John', 'Pratik', 'Ravi', 'Dipak', 'Amol']

# We can access only odd number value using for loop
x = 0
for item in i:
    if x%2 == 0:
        print(f'{item} is our team')
    x += 1

# We can access only odd number using enumerate function
for index, item in enumerate(i):
    if index%2 == 0:
        print(f'{item} is our team')


l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
print("Return type:", type(obj1))  # Output -> Return type: <class 'enumerate'>
print(list(enumerate(l1)))  # Output -> [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
# changing start index to 2 from 0
print(list(enumerate(s1, 2)))  # Output -> [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]