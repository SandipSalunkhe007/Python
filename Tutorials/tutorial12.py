# Pattern Printing
# Input = Integer n
# Boolean = if True then increment pattern or False then decrement pattern
# *
# **
# ***
# ****
def star():
    print('Star Pattern')
    print('Enter How many rows you want :')
    n = int(input())
    print('Enter 1 for True |OR| 0 for False')
    bool_val = input()
    if bool_val == '1':
        for i in range(0,n+1):
            print('*' * i)
    if bool_val == '0':
        for i in range(n,0,-1):
            print('*' * i)
    star_cond()


def star_cond():
    print('Enter Yes for Play again |OR| No for Quit')
    s = input()
    if s == 'Yes':
        star()
    else:
        print("----Game Over-----")

star()