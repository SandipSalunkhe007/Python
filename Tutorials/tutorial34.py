# Static method
# When we want to simple method which is used for only print then used static method
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

sandip = Employee('Sandip', 235, 'Software')
harry = Employee('Harry',352, 'Designer')
harry.printpara('Harry')