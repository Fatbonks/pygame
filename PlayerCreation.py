import time

import Pipe as game


# The set up for the player
def player_class():
    print("Pick your class\n1: warrior\n2: mage\n3: archer\n4: thief")
    while True:
        try:
            act = int(input("> ").lower().strip())
            if act == 1:
                game.gameData.player['class'] = 'warrior'
                break
            elif act == 2:
                game.gameData.player['class'] = 'mage'
                game.gameData.player['stats']['health'] = 5.0
                game.gameData.player['stats']['max_mana'] = 13.0
                game.gameData.player['stats']['mana'] = 13.0
                game.gameData.player['stats']['speed'] = 2.0
                game.gameData.player['stats']['damage']['min_damage'] = 1
                game.gameData.player['stats']['damage']['max_damage'] = 2
                game.magicLogic.give_magic()
                break
            elif act == 3:
                game.gameData.player['class'] = 'archer'
                game.gameData.player['stats']['health'] = 10.0
                game.gameData.player['stats']['speed'] = 4.0
                break
            elif act == 4:
                game.gameData.player['class'] = 'thief'
                game.gameData.player['stats']['health'] = 8.0
                game.gameData.player['stats']['speed'] = 3.0
                game.gameData.player['stats']['dodge'] = 95
                game.gameData.player['stats']['damage']['min_damage'] = 1
                game.gameData.player['stats']['damage']['max_damage'] = 1
                break
            print("Please input a valid number!")
        except ValueError:
            print("Please input a valid number!")

    # Welcome text
    print("------------")
    print("Welcome to {RPGName}")
    if input("What would you like to name yourself?\n> ") != "":
        print("Stupid! a baby can't name itself!")
    game.gameData.player['name'] = game.ran.choice(game.gameData.names)
    print("Your name is now {}".format(game.gameData.player['name']))
    time.sleep(2.5)


if __name__ == '__main__':
    exit('Please run main.py')
