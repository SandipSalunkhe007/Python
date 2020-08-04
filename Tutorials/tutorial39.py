# Polymorphism
# Ability to take various form means it refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.
# Example + operator with different form like 2 + 3 = 5 and "2" + "3" = 23

# Function polymorphism in Python, Class polymorphism in Python,

# Super() method and Method Overriding in class
# -------- 1 --------
class A:
    classvar = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"

class B(A):
    classvar1 = "I am in class B"

a = A()
b = B()
print(b.classvar1)  # Output -> Instance var in class A
# first search the variable in instance variable/constructor

# -------- 2 --------
class A:
    classvar = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"

class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        self.vars = "Hello I am in class B"

a = A()
b = B()
print(b.classvar1)  # Output -> I am in class B
# class B constructor are override with class A
# Firstly search in class B constructor and that constructor is override with parent. So class B constructor that instance variable not found then it will search in global variable


# -------- 3 --------
class A:
    classvar = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"

class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        super().__init__()
        self.vars = "Hello I am in class B"

a = A()
b = B()
print(b.classvar1)  # Output -> Instance var in class A
# super().__init() we can add parent constructor instance variable in that class B


# -------- 4 --------
class A:
    classvar = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"

class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        super().__init__()
        self.vars = "Hello I am in class B"
        self.classvar1 = "Override instance var in class B"

a = A()
b = B()
print(b.classvar1)  # Output -> Override instance var in class B
# Override that var in class B


# -------- 5 --------
class A:
    classvar = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"

class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        self.vars = "Hello I am in class B"
        self.classvar1 = "Override instance var in class B"
        super().__init__()
a = A()
b = B()
print(b.classvar1)  # Output -> Instance var in class A
# If super() method add in bottom of the constructor then it will override with above instance var
