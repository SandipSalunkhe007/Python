# Class method as alternative method
# We used, when we have bunch of data with dash or other format then we can used Class method as alternative method
class Employee:
    no_of_leave = 9

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def empdetails(self):
        return f'My name is {self.name} salary is {self.salary} and role is {self.role} Leaves is {self.no_of_leave}'

    @classmethod  # Decorator
    def from_dash(cls, string):  # Class method as alternative method
        # params = string.split('-')
        # print(params)  # Output -> ['Karan', '334', 'Programmer']
        # return cls(params[0], params[1], params[2])
        return cls(*string.split('-'))  # Above two line code in one line using _args

sandip = Employee('Sandip', 235, 'Software')
harry = Employee('Harry',352, 'Designer')
karan = Employee.from_dash('Karan-334-Programmer')  # All parameter in one string then we split
print(karan.__dict__)  # Output -> {'name': 'Karan', 'salary': '334', 'role': 'Programmer'}
print(karan.empdetails())  # Output -> My name is Karan salary is 334 and role is Programmer Leaves is 9