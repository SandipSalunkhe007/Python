# OOPs
# Classes - Template
# Object - Is an instance of a Class
# Object consists of - State, Behavior, Identity

# Create Class
class Employee:
    no_of_leave = 9
    pass

harry = Employee()
sandip = Employee()

sandip.name = "Sandip"  #  sandip is a instance
sandip.salary = 16
harry.name = 'Harry'
harry.salary = 17
print(sandip.name)
print(sandip.no_of_leave)
print(sandip.__dict__)  # Output -> {'name': 'Sandip', 'salary': 16}
sandip.no_of_leave = 19  # Create new instance not replace in Employee class
print(sandip.no_of_leave)
print(sandip.__dict__)  # Output -> {'name': 'Sandip', 'salary': 16, 'no_of_leave': 19}
Employee.no_of_leave = 10  # Update in a class
print(harry.no_of_leave)  # Output -> 10
