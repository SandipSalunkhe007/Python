# __init__(), Constructor
# The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created.In Python the __init__() method is called the constructor and is always called when an object is created.
# Syntax -
#   def __init__(self):
#       body of the constructor

class Employee:
    no_of_leave = 9

    def __init__(self, aname, asalary, arole):  # aname, asalary, arole is argument - __init__ is a Constructor
        self.name = aname  # name is instance variable name
        self.salary = asalary  # salary is instance variable name
        self.role = arole  # role is instance variable name

    def empdetails(self):  # method
        return f'My name is {self.name} salary is {self.salary} and role is {self.role}'


sandip = Employee('Sandip', 235, 'Software')
harry = Employee('Harry',352, 'Designer')


print(sandip.empdetails())  # Output -> My name is Sandip and salary is 16
print(harry.empdetails())  # Output -> My name is Harry and salary is 17


