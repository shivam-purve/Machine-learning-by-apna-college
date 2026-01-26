class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)
        print("-" * 20)


p1 = Person("Shivam")
p1.display()


p2 = Person("Shivam", 21)
p2.display()

p3 = Person("Shivam", 21, "IIT Tirupati")
p3.display()
