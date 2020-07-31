# While Loop
'''
i = 0
while i < 45:
    print(i)
    i += 1


# show value which is greater than 4 upto less than 45
i = 0
while(True):
    if i+1<5:
        i = i + 1
        continue

    print(i+1, end=' ')
    if(i==44):
        break
    i = i + 1
# Output -> 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45


# User enter a number upto if number is greater than 100 then stop that loop
lists = []
i =0
while i < 100:
    i = int(input("Enter a number"))
    lists.append(i)
print(lists)
'''

# User enter a number upto if number is greater than 100 then stop that loop
lists = []
while(True):
    inpts = int(input('Enter a number'))
    lists.append(inpts)
    if inpts > 100:
        print('Value is greater than 100')
        break
    else:
        continue
print(lists)