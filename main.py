class game_logic:
    # Declare all global variables 
    def __init__(self):
        self.name = ''
        self.number = 0
        self.player = {"class": {"warrior": {"stats": ({"health": 10.0}, {"mana": 10.0})}}}


    def add_one(self):
        self.number += 1
        print(self.player.get("class").get("warrior"))

if __name__ == '__main__':
    game = game_logic()

    

    # Main game loop
    while True:
        game.add_one()  

