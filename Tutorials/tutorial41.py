# Operator overloading and Dunder/Magic method
# Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name. 
# Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading. Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.

class Employee:
    no_of_leave = 9

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def empdetails(self):
        return f'My name is {self.name} salary is {self.salary} and role is {self.role} Leaves is {self.no_of_leave}'

    def __add__(self, other):  # Dunder method
        return self.salary + other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __repr__(self):  # if we print object then by default print __repr__ method or if not present then it show empty
        return f'Welcome {self.name}'

    def __str__(self):  # This is same as __str__ only diff is if __str__ present then return there value than __repr__ value
        return f'Hi, {self.name}, {self.role}'

sandip = Employee('Sandip', 235, 'Software')
harry = Employee('Harry',352, 'Designer')

print(sandip + harry)  # Output -> 587
print(sandip * harry)  # Output -> 82720
print(sandip)  # Output -> Hi, Sandip, Software

import operator
a = 5
b = 23
print(operator.mul(a,b))  # Output -> 115

