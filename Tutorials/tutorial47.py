# Comprehension
# Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.) using sequences which have been already defined. Python supports the following 4 types of comprehensions:
# List Comprehensions
# Dictionary Comprehensions
# Set Comprehensions
# Generator Comprehensions

# List Comprehension
ls = []

for i in range(100):
    if i%3 == 0:
        ls.append(i)

print(ls)
# Same output in minimum code
ls = [i for i in range(100) if i%3 == 0]
print(ls)

# Dictionary Comprehension
dect1 = {i:f"item{i}" for i in range(3)}
print(dect1)  # Output -> {0: 'item0', 1: 'item1', 2: 'item2'}

dect1 = {i:f"item{i}" for i in range(5) if i%2 == 0}
print(dect1)  # Output -> {0: 'item0', 2: 'item2', 4: 'item4'}

dect1 = {i:f"item{i}" for i in range(3)}
dect2 = {value:key for key,value in dect1.items()}
print(dect2)  # Output -> {'item0': 0, 'item1': 1, 'item2': 2}

# Set Comprehension
i = {dress for dress in ['dress1','dress2','dress3', 'dress1', 'dress2']}
print(i)  # Output -> {'dress1', 'dress3', 'dress2'}
print(type(i))  # Output -> <class 'set'>

# Generator Comprehension used for ()
evens = (i for i in range(10) if i%2 == 0)
print(type(evens))  # Output -> <class 'generator'>
print(evens.__next__())  # Output -> 0
print(evens.__next__())  # Output -> 2
print(evens.__next__())  # Output -> 4