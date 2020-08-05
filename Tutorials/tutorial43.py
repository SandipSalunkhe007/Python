# Setter and Property Decorators
# main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation.
# We use getters & setters to add validation logic around getting and setting a value.
# To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.

# ----- 1 -----
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f'{fname}.{lname}@gmail.com'

sandip = Employee('Sandip', 'Salunkhe')

print(sandip.email)  # Output -> Sandip.Salunkhe@gmail.com
sandip.email = 'raj.rathod@gmail.com'
print(sandip.email)  # Output -> raj.rathod@gmail.com

# ----- 2 -----
# class Employee:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         # self.email = f'{fname}.{lname}@gmail.com'
#
#     def emails(self):
#         return f'{self.fname}.{self.lname}@gmail.com'
#
# sandip = Employee('Sandip', 'Salunkhe')
#
# print(sandip.emails())  # Output -> Sandip.Salunkhe@gmail.com
# sandip.emails = 'raj.rathod@gmail.com'
# print(sandip.emails())  # Output -> TypeError: 'str' object is not callable


# ----- 3 -----
# Using @property decorators to achieve getters and setters behaviour
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f'{fname}.{lname}@gmail.com'

    @property
    def emails(self):
        if self.fname == None or self.lname == None:
            return f'Email is not set'
        return f'{self.fname}.{self.lname}@gmail.com'

    @emails.setter  # if we update that email then setter used
    def emails(self, string):
        name = string.split('@')[0]
        self.fname = name.split('.')[0]
        self.lname = name.split('.')[1]

    @emails.deleter  # if we delete that email then deleter used
    def emails(self):
        self.fname = None
        self.lname = None

sandip = Employee('Sandip', 'Salunkhe')

print(sandip.emails)  # Output -> Sandip.Salunkhe@gmail.com
sandip.emails = 'raj.rathod@gmail.com'
print(f'New {sandip.emails}')  # Output -> raj.rathod@gmail.com
del sandip.emails
print(f'{sandip.emails}')  # Output -> Email is not set



# Using normal function to achieve getters and setters behaviour
# To achieve getters & setters property, if we define normal get() and set() methods it will not reflect any special implementation. For Example
# Python program showing a use of get() and set() method in normal function
class Geek:
    def __init__(self, age=0):
        self._age = age

        # getter method

    def get_age(self):
        return self._age

        # setter method

    def set_age(self, x):
        self._age = x

raj = Geek()

# setting the age using setter
raj.set_age(21)

# retrieving age using getter
print(raj.get_age())  # Output -> 21

print(raj._age)  # Output -> 21


# Using property() function to achieve getters and setters behaviour
# In Python property()is a built-in function that creates and returns a property object. A property object has three methods, getter(), setter(), and delete(). property() function in Python has four arguments property(fget, fset, fdel, doc), fget is a function for retrieving an attribute value. fset is a function for setting an attribute value. fdel is a function for deleting an attribute value. doc creates a docstring for attribute. A property object has three methods, getter(), setter(), and delete() to specify fget, fset and fdel individually. For Example
# Python program showing a use of property() function
class Geeks:
    def __init__(self):
        self._age = 0

    # function to get value of _age
    def get_age(self):
        print("getter method called")
        return self._age

        # function to set value of _age

    def set_age(self, a):
        print("setter method called")
        self._age = a

        # function to delete _age attribute

    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)


mark = Geeks()

mark.age = 10

print(mark.age)  # Output -> 10