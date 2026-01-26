class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self,seat,brand,model):
        super().__init__(brand,model)
        self.seat = seat


class Bike(Vehicle):
    def __init__(self,brand,model,engine_cc):
        super().__init__(brand,model)
        self.engine_cc = engine_cc


car = Car(100,"Thar","swat")
bike = Bike("BMW","new_race_Bike","35cc")


