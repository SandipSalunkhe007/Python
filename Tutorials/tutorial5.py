# For Loop
# Access list using for loop
list1 = ['Sandip', 'John', 'Marry']
list2 = [['Sandip',1],['John',2],['Swap',3]]
for item, item3 in list2:
    print(item, item3)
'''Output
Sandip 1
John 2
Swap 3
'''

# Access Dictionary using for loop
list3 = {'sandip':'Salunhkhe',
         'Temp':'woz',
         'Queen':'pop'}
for pips, pips2 in list3.items():
    print(pips,'value is', pips2)
'''Output
sandip value is Salunhkhe
Temp value is woz
Queen value is pop
'''

# print the all values greater than 6
list4 = [3,4,6,2,4,'sandip',22,'John',4,53]
for items in list4:
    if str(items).isnumeric() and items > 6:
        print(items)
'''Output
22
53'''