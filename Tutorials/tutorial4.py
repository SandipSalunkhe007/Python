# Faulty Calculator
# 45 * 3 = 555, 56 + 6 = 77, 56/6 = 4

print('Enter a first number')
i1 = int(input())
print('Enter a second number')
i2 = int(input())
print("what operator u want use +/-/*//")
i3 = input()
if i3 == '+':
    if i1 == 56 and i2 == 6:
        print('77')
    else:
        print(i1 + i2)
elif i3 == '-':
    print(i1 - i2)
elif i3 == '*':
    if i1 == 45:
        print('555')
    else:
        print(i1 * i2)
elif i3 == '/':
    if i1 == 56 and i2 == 6:
        print('4')
    else:
        print(i1 / i2)
else:
    print('You have enter wrong operator')