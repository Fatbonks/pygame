import Pipe as game


def event_picker():
    if game.ran.random() < 1:
        game.combatLogic.combat_display()


def legal_disclaimer():
    game.print_dialogue("By playing this game you agree to the following terms:")
    game.print_dialogue("1: You agree that you are of legal age to agree to the terms stated.")
    game.print_dialogue("2: You agree that you have read and understood all of these terms.")
    game.print_dialogue("3: You agree that you are comfortable with reading text with disturbing themes such as the "
                        "following:")
    game.print_dialogue("Sexual violence, Physical violence, Drug abuse, and other harmful language.")
    game.print_dialogue("4: You agree that all characters in this game are works of fiction and any connection to "
                        "the real world is just a coincidence.")
    if game.get_input("By typing 'Yes' you agree to all the terms stated.") != "Yes":
        exit("You did not type 'Yes' exactly as stated above, therefore, we cannot let you play")
    else:
        game.print_dialogue("Welcome to {RPGName}")


if __name__ == '__main__':
    # legal_disclaimer()
    # Runs at the start of the game
    game.playerCreation.player_class()
    # Main game loop
    while True:
        game.draw_line()
        print("1 - Move up\n2 - Shows your stats\n3 - To leave the game")
        try:
            answer = int(input("> ").lower().strip())
            # up is debug command to trigger combat
            # if player enters up go into combat
            # if player enters stats print out the stats
            # if player enters exit, exit the game
            if answer <= 0:
                print('please use numbers between 1 - 3')
            if answer >= 4:
                print('please use numbers between 1 - 3')
            if answer == 1:
                # 100% chance to get into a fight
                event_picker()
            elif answer == 2:
                game.print_dialogue("----------------------------")
                game.print_dialogue("Level: {}".format(game.gameData.player['level']['level']))
                game.print_dialogue("Max health: {}".format(game.gameData.player['stats']['max_health']))
                game.print_dialogue("Health: {}".format(game.gameData.player['stats']['health']))
                game.print_dialogue("Max mana: {}".format(game.gameData.player['stats']['max_mana']))
                game.print_dialogue("Mana: {}".format(game.gameData.player['stats']['mana']))
                game.print_dialogue("{} - {} damage"
                                    .format(game.gameData.player['stats']['damage']['min_damage'],
                                            game.gameData.player['stats']['damage']['max_damage']))
                game.print_dialogue("EXP: {}".format(game.gameData.player['level']['exp']))
                game.print_dialogue("Speed: {}".format(game.gameData.player['stats']['speed']))
                game.print_dialogue("Dodge: {}".format(game.gameData.player['stats']['dodge']))
                game.print_dialogue("Level next: {}".format(game.gameData.player['level']['level_next']))
                game.print_dialogue("smeckles: {}".format(game.gameData.player['bag']['gold']))
                # Test this when enemies are working again
                # We add 1 because we wanted slots to start at 1 not 0.
                for spell_slot in range(1, len(game.gameData.player['magic_slots']) + 1):
                    if game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['name'] != '':
                        game.print_dialogue("Spell in slot {}".format(spell_slot))
                        game.print_dialogue(
                            "name: {}".format(game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]
                                              ['name']))
                        game.print_dialogue(
                            "mana cost: {}".format(game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]
                                                   ['mana_cost']))
                        game.print_dialogue("Min damage: {}\nMax damage: {}".format(game.gameData.player['magic_slots']
                                                                                    ['slot_{}'.format(spell_slot)][
                                                                                        'damage']
                                                                                    ['min_damage'],
                                                                                    game.gameData.player['magic_slots']
                                                                                    ['slot_{}'.format(spell_slot)][
                                                                                        'damage']
                                                                                    ['max_damage']))
                        game.print_dialogue(
                            "Proficiency: {}".format(game.gameData.player['magic_slots'] \
                                                         ['slot_{}'.format(spell_slot)]['proficiency']))
                        game.print_dialogue(
                            "Proficiency level up: {}".format(game.gameData.player['magic_slots']['slot_{}'
                                                              .format(spell_slot)]['proficiency_level_up']))
            elif answer == 3:
                exit(0)
        except ValueError:
            print('please use a number')

if __name__ == '__main__':
    exit('Please run main.py')
