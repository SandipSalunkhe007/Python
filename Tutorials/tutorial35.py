# Single Inheritance
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
        return cls(*string.split('-'))  # Above two line code in one line using _args

    @staticmethod
    def printpara(strings):  # simple print string
        print("This is ", strings)

class Programmer(Employee):
    def __init__(self, aname, asalary, arole, alanguage):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = alanguage

    def printprog(self):
        return f'My programmer name is {self.name} salary is {self.salary} and role is {self.role} Leaves is {self.no_of_leave} and he know {self.languages}'

sandip = Employee('Sandip', 235, 'Software')
harry = Employee('Harry',352, 'Designer')
karan = Programmer('Karan',654,'Programmer', ['Python', 'Javascript'])
print(karan.printprog())  # Output -> My programmer name is Karan salary is 654 and role is Programmer Leaves is 9 and he know ['Python', 'Javascript']
print(karan.empdetails())  # Output -> My name is Karan salary is 654 and role is Programmer Leaves is 9