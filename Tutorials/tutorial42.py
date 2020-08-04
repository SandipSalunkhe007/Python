# Abstract Base Class(ABC)
# It allows you to create a set of methods that must be created within any child classes built from the abstract class.
# A class which contains one or more abstract methods is called an abstract class.
# While we are designing large functional units we use an abstract class. When we want to provide a common interface for different implementations of a component, we use an abstract class.

from abc import ABC, abstractmethod
class Animal(ABC):

    def move(self):
        pass


class Human(Animal):

    def move(self):
        print("I can walk and run")


class Snake(Animal):

    def move(self):
        print("I can crawl")


class Dog(Animal):

    def move(self):
        print("I can bark")


class Lion(Animal):

    def move(self):
        print("I can roar")

    # Driver code

R = Human()
R.move()  # Output -> I can walk and run

K = Snake()
s = K.move()  # Output -> I can crawl

R = Dog()
R.move()  # Output -> I can bark

K = Lion()
K.move()  # Output -> I can roar