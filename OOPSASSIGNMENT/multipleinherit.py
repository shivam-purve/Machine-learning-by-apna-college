class Herbivore:
    def __init__(self):
        self.plant_food = "Plants"

    def eat_plants(self):
        print("Eating plants 🌿")


class Carnivore:
    def __init__(self):
        self.meat_food = "Meat"

    def eat_meat(self):
        print("Eating meat 🍖")



class Omnivore:
    def __init__(self):
        self.mixed_food = "Plants and Meat"

    def eat_everything(self):
        print("Eating both plants and meat 🍎🍖")


class Bear(Herbivore, Carnivore, Omnivore):

    def __init__(self, name):
        Herbivore.__init__(self)
        Carnivore.__init__(self)
        Omnivore.__init__(self)
        self.name = name

    def show_diet(self):
        print("Bear Name:", self.name)
        print("Diet Types:", self.plant_food, ",", self.meat_food)


bear = Bear("Grizzly")

bear.eat_plants()
bear.eat_meat()
bear.eat_everything()
bear.show_diet()


    


