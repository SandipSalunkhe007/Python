# __name == '__main__'
# When we used any function from other files then used
# tutorial24 and tutorial25 is a example of that accessing other file content

def printhar(strg):
    return f'String is {strg}'

def add(a, b):
    return f'Sum of {a + b + 5}'


if __name__ == '__main__':  # this code not execute in other import file but this below code execute in current file
    x = printhar('World')
    print(x)
    y = add(5, 6)
    print(y)

