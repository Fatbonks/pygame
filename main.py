class game_logic:
    # Declare all global variables 
    def __init__(self):
        self.name = ''
        self.number = 0

    def add_one(self):
        self.number += 1
        print(self.number)

if __name__ == '__main__':
    game = game_logic()
    game.add_one()  

