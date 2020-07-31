# Scope,Global Variables and Global Keyword
# Local Variable - can not access out of the local scope
# Global Variable - Global variable can not edit in local scope
# Global Keyword - Global keyword used for edit global variable in local scope using 'global' keyword
l = 10
def function1(n):
    global l  # edit global variable in local scope using 'global' keyword
    l = l + 5  # after global keyword define we can edit that global variable
    print(n, 'I have printed')
    print(l)
print(l)
function1('this is me')

x = 20
def print1():
    x = 10
    def print2():
        global x
        x = 5
        print('local : ',x)  # Output -> 5
    print('before calling print2 : ',x)  # Output -> 10
    print2()
    print('after calling print2 : ',x)  # Output -> 10
print1()
print(x)  # Output -> 5