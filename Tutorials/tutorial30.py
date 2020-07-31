# The Self
# Class methods must have an extra first parameter in method definition. We do not give a value for this parameter when we call the method, Python provides it.
# If we have a method which takes no arguments, then we still have to have one argument
class Employee:
    no_of_leave = 9
    # Method
    def empdetails(self):  # a method for printing data members
        return f'My name is {self.name} and salary is {self.salary}'

# creating object of the class
sandip = Employee()
harry = Employee()

sandip.name = "Sandip"
sandip.salary = 16
harry.name = 'Harry'
harry.salary = 17

print(sandip.empdetails())  # Ourput -> My name is Sandip and salary is 16
print(harry.empdetails())  # Output -> My name is Harry and salary is 17


