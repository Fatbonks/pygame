import Pipe as game


# The setup for the player
def player_class():
    game.draw_line()
    print("Pick your class\n1: warrior\n2: mage\n3: thief")
    while True:
        try:
            act = int(input("> ").lower().strip())
            if act == 1:
                game.gameData.player['class'] = 'warrior'
                game.gameData.player['race'] = 'BeastMan'
                game.physical_skill.skill_slot_adder(game.gameData.physical_skills['Big Swing'], 1)
                game.physical_skill.skill_slot_adder(game.gameData.physical_skills['spin attack'], 2)
                game.physical_skill.skill_slot_adder(game.gameData.physical_skills['Sword swipe'], 3)
                break
            elif act == 2:
                game.gameData.player['stats']['max_health'] = 8
                game.gameData.player['class'] = 'mage'
                game.gameData.player['race'] = 'Dark Elf'
                game.gameData.player['stats']['health'] = 8
                game.gameData.player['stats']['max_mana'] = 13
                game.gameData.player['stats']['mana'] = 13
                game.gameData.player['stats']['speed'] = 2
                game.gameData.player['stats']['damage']['min_damage'] = 1
                game.gameData.player['stats']['damage']['max_damage'] = 2
                game.physical_skill.skill_slot_adder(game.gameData.physical_skills['staff bash'], 1)
                game.magicLogic.give_magic()
                break
            elif act == 3:
                game.gameData.player['stats']['max_health'] = 10
                game.gameData.player['class'] = 'thief'
                game.gameData.player['race'] = 'human'
                game.gameData.player['stats']['health'] = 10
                game.gameData.player['stats']['speed'] = 3
                game.gameData.player['stats']['dodge'] = 75
                game.gameData.player['stats']['damage']['min_damage'] = 1
                game.gameData.player['stats']['damage']['max_damage'] = 3
                game.physical_skill.skill_slot_adder(game.gameData.physical_skills['Big Swing'], 1)
                game.physical_skill.skill_slot_adder(game.gameData.physical_skills['Stab'], 2)

                break
            elif act == 2134:
                game.gameData.player['stats']['max_health'] = 13
                game.gameData.player['class'] = 'archer'
                game.gameData.player['race'] = 'Forest Elf'
                game.gameData.player['stats']['health'] = 13
                game.gameData.player['stats']['speed'] = 4
                game.gameData.player['stats']['dodge'] = 45
                break
            print("Please input a valid number!")
        except ValueError:
            print("Please input a valid number!")
    input('press enter to continue')
    game.clear()

    # Welcome text
    game.draw_line()
    print("Welcome to {RPGName}")
    game.gameData.player['name'] = game.ran.choice(game.gameData.names)
    if input("What would you like to name yourself?\n> ") != "":
        print("Stupid! a baby can't name itself!")
        print("Your name is now {}".format(game.gameData.player['name']))
    else:
        print("Your name is now {}".format(game.gameData.player['name']))
    input('press enter to continue')
    game.clear()


if __name__ == '__main__':
    exit('Please run main.py')
