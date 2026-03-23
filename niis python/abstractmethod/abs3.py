from abc import ABC, abstractmethod
# Abstract class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
    def sleep(self):  # normal method
        print("Sleeping...")
# Subclass implementing the abstract method
class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")





