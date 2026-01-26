
class Laptop:
    storage_type = "ssd"

    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage
    

    @classmethod
    def get_storage_type(cls):
        print(f"storage_type = {cls.storage_type}")
    
    def get_info(self):
        print(f"laptop has {self.RAM} RAM and {self.storage} {self.storage_type}")

    @staticmethod
    def calc_discount(price,discount):
        discounted_price = price - (discount*price/100)
        print(f"the final price is {discounted_price}")
    



    


l1 = Laptop("16gb","512gb")
l2 = Laptop("8gb","256gb")

l1.get_info()

l2.calc_discount(40_000,10)