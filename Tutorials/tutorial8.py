# Functions
a = 8
b = 7
x = sum((a, b))  # built-in function
print(x)


def avg(a, b):  # User define function
    ''' This is the avg function '''
    c = (a + b) / 2
    return c


result = avg(5, 6)
print(result)  # Output -> 5.5
print(avg.__doc__)  # This is the Doc string. We can access for function discription.
# Output -> This is the avg function
