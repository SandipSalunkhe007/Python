# Class Methods
# Class method used for access to instance or access to class
# By using Class method we can change value of class attribute using instance or class name
class Employee:
    no_of_leave = 9

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def empdetails(self):
        return f'My name is {self.name} salary is {self.salary} and role is {self.role} Leaves is {self.no_of_leave}'

    @classmethod  # Decorator
    def change_leave(cls, newleaves):  # this is class method used for getting class
        cls.no_of_leave = newleaves


sandip = Employee('Sandip', 235, 'Software')
harry = Employee('Harry',352, 'Designer')

Employee.change_leave(34)  # By using Class method we can change value of class attribute
sandip.change_leave(56)  # By using Class method we can change value of class attribute
print(sandip.empdetails())  # Output -> My name is Sandip salary is 235 and role is Software Leaves is 56
print(harry.empdetails())  # Output -> My name is Harry salary is 352 and role is Designer Leaves is 56