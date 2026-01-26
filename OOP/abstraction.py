from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):   #abstarct method implementation will be in inherited class
        pass


class Lion(Animal):
    def make_sound(self):
        print("roar")

class Cow(Animal):
     def make_sound(self):
        print("Moo!")





lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()