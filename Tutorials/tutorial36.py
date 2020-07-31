# Multiple Inheritance
class Employee:
    no_of_leave = 9
    var = 8
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

class Player:
    no_of_games = 4
    var = 9
    def __init__(self, name, game):
        self.name = name
        self.game = game
    def printdetails(self):
        return f'The name is {self.name}. Game is {self.game}'

class CoolProgrammer(Employee, Player):
    var = 10
    language = '[C++]'
    def printlanguage(self):
        print(self.language)
    def coolmeth(self,empid,empsource):
        self.empid = empid
        self.empsource = empsource

sandip = Employee('Sandip', 235, 'Software')
harry = Employee('Harry',352, 'Designer')
karan = CoolProgrammer('Karan',757,'Cool Programmer')
karan.coolmeth('101','Web')
karan.game = 'Video'
karan.printdetails()
print(karan.__dict__)
print(karan.var)  # Output -> 10. If that variable not in CoolProgrammer class then it will access first inheritance class i.e. 8