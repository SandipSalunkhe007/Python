# range() function
# range(start,stop, stepsize)
# range() -  Default start value started from 0 and Stop value end with (stop_value - 1)
# if range(10) - one value then this is the Stop value
# if range(2,10) - two value then this is the Start and Stop value
# if range(0,10,2) - third value is stop value - 1
for i in range(10):
    print(i, end=' ')  # Output -> 0 1 2 3 4 5 6 7 8 9
print()
for i in range(2,10):
    print(i, end=' ')  # Output -> 2 3 4 5 6 7 8 9
print()
for i in range(1,10,2):  # Output -> 1 3 5 7 9
    print(i, end=' ')
