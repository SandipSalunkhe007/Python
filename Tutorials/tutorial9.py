# Try Except exception handling

print('Enter first number')
i1 = input()
print('Enter second number')
i2 = input()
try:
    print('Sum', int(i1) + int(i2))
except Exception as e:
    print(e)

print('This is very important line')
'''Output
Enter first number
3
Enter second number
d
invalid literal for int() with base 10: 'd'
This is very important line
'''