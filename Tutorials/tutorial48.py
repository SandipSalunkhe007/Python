# Using Else with For Loop
khana = ['roti', 'sabzi', 'chaval']
for item in khana:
    print(item, end=' / ')
else:
    print("This for loop ended properly")  # Output -> roti / sabzi / chaval / This for loop ended properly



for item in khana:
    print(item)
    break
else:
    print("This for loop ended properly")  # Output -> roti


for item in khana:
    if khana == 'roti':
        break
else:
    print("This for loop ended properly")  # Output -> This for loop ended properly


for item in khana:
    if khana == 'rotiroll':
        break
else:
    print("This for loop ended properly")  # Output -> This for loop ended properly