import time

import Pipe as game


# The set up for the player
def player_class():
    game.print_dialogue("Pick your class\n1: warrior\n2: mage\n3: archer\n4: thief")
    while True:
        try:
            act = int(input("> ").lower().strip())
            if act == 1:
                game.gameData.player['class'] = 'warrior'
                break
            elif act == 2:
                game.gameData.player['stats']['max_health'] = 8.0
                game.gameData.player['class'] = 'mage'
                game.gameData.player['stats']['health'] = 8.0
                game.gameData.player['stats']['max_mana'] = 13.0
                game.gameData.player['stats']['mana'] = 13.0
                game.gameData.player['stats']['speed'] = 2.0
                game.gameData.player['stats']['damage']['min_damage'] = 1
                game.gameData.player['stats']['damage']['max_damage'] = 2
                game.magicLogic.give_magic()
                break
            elif act == 3:
                game.gameData.player['stats']['max_health'] = 13.0
                game.gameData.player['class'] = 'archer'
                game.gameData.player['stats']['health'] = 13.0
                game.gameData.player['stats']['speed'] = 4.0
                game.gameData.player['stats']['dodge'] = 45
                break
            elif act == 4:
                game.gameData.player['stats']['max_health'] = 10.0
                game.gameData.player['class'] = 'thief'
                game.gameData.player['stats']['health'] = 10.0
                game.gameData.player['stats']['speed'] = 3.0
                game.gameData.player['stats']['dodge'] = 75
                game.gameData.player['stats']['damage']['min_damage'] = 1
                game.gameData.player['stats']['damage']['max_damage'] = 1
                break
            game.print_dialogue("Please input a valid number!")
        except ValueError:
            game.print_dialogue("Please input a valid number!")

    # Welcome text
    game.print_dialogue("------------")
    game.print_dialogue("Welcome to {RPGName}")
    game.gameData.player['name'] = game.ran.choice(game.gameData.names)
    if input("What would you like to name yourself?\n> ") != "":
        game.print_dialogue("Your name is now {}".format(game.gameData.player['name']))
        game.print_dialogue("Stupid {}! a baby can't name itself!".format(game.gameData.player['name']))
    else:
        game.print_dialogue("Your name is now {}".format(game.gameData.player['name']))


if __name__ == '__main__':
    exit('Please run main.py')
