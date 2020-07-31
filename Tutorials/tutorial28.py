# Decorator

# In Python, functions are the first class objects, which means that –
# Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
# Functions can be defined inside another function and can also be passed as argument to another function.
# Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

def funct1():
    print('Subscribe now')
func2 = funct1
func2()


def functret(num):
    if num == 0:
        return sum
    if num == 1:
        return print

a = functret(0)
print(a)  # Output -> <built-in function sum>


def exercutor(funct):
    funct('Hello World')
exercutor(print)  # Output -> Hello World


def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print('Executed')

    return nowexec


@dec1
def funct2():
    print("Hello World")

# funct2 = dec1(funct2)
funct2()

