# Object Introspection
# Introspection is an ability to determine the type of an object at runtime.
# Python provides some built-in functions that are used for code introspection.They are:
# type() : This function returns the type of an object.
# dir() :This function return list of methods and attributes associated with that object.
# str() :This function converts everything into a string .
# id() :This function returns a special id of an object.
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
import inspect
print(id(sandip)) # it print unique id
print(type(sandip))  # Output -> <class '__main__.Employee'>
print(dir(sandip))
