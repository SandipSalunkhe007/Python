# lambda function or anonymous function
# lambda function used for minimum code for define a function
minus = lambda x, y : x - y
print(minus(50,8))
# OR normal function
def minus(x,y):
    print(x - y)
minus(50,8)

# sort function using def function
def a_first(a):
    return a[0]  # a[0] for first position sorting
a = [[2,55],[502,100],[56,21]]
a.sort(key=a_first)
print('Sorting using def function :',a)  # Output -> Sorting using def function : [[2, 55], [56, 21], [502, 100]]

# sort function using lambda function
a = [[2,55],[502,100],[56,21]]
a.sort(key=lambda x: x[1])  # x[1] for second position sorting
print('Sorting using lambda function :',a)  # Output -> Sorting using lambda function : [[56, 21], [2, 55], [502, 100]]
