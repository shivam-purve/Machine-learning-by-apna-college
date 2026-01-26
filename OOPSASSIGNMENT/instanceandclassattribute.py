class Player:
    player_count = 0
    def __init__(self,name,level):
        self.name = name
        self.level = level
        Player.player_count += 1
    

    def get_player_count(cls):
        return cls.player_count
    def get_info(self):
        print(f"the player name is {self.name} and his/her level is {self.level}")
    


pl1 = Player("shivam","L-2")
pl2 = Player("shiv","L-6")
pl3 = Player("Raaz","L-1")
pl4 = Player("Manish","L-4")

print(f"the total players are {pl1.get_player_count()}")
pl1.get_info()
pl2.get_info()

pl3.get_info()

pl4.get_info()


        