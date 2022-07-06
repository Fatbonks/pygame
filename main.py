import Pipe as game


def event_picker():
    if game.ran.random() < 1:
        game.combatLogic.combat_display()


def display_stats():
    game.draw_line()
    print('{}:')
    print('-------')
    print('Class: {} | Race: {}')
    print('Level: {} | Level_next: {} | EXP: {}')
    print('MX_HP: {} | Health: {}')
    print('MX_MP: {} | Mana: {}')
    print('-------')
    print('SPD: {}')
    print('DMG: {} - {}')
    print('Dodge: {}')
    print('Smeckles: {}')
    game.draw_line()


def display_skills():
    pass


def display_spell():
    game.clear()
    for spell_slot in range(1, len(game.gameData.player['magic_slots']) + 1):
        if game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['name'] != '':
            game.draw_line()
            print('Spell in slot {}'.format(spell_slot))
            print('-------')
            print('{}:'.format(game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['name']))
            print(
                'mana cost: {}'.format(game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['mana_cost']))
            print('DMG: {} - {}'.format(
                game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['damage']['min_damage'],
                game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['damage']['max_damage']
            )
            )
            print('Proficiency: {} | Proficiency level up: {}'.format(
                game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['proficiency'],
                game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['proficiency_level_up']
            )
            )
            game.time.sleep(1.3)
            if spell_slot == 4:
                input('press enter to leave')
                game.clear()


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
    while True:
        print('1 - load save file\n2 - new game')
        ans = int(input('> '))
        # legal_disclaimer()
        # Runs at the start of the game
        if ans == 1:
            game.SavedGame.load_game()
            if game.gameData.has_loaded is True:
                game.gameData.has_loaded = False
                break
        if ans == 2:
            game.playerCreation.player_class()
            break

    # Main game loop
    while True:
        game.draw_line()
        print("1 - Move up\n2 - Shows your stats\n3 - To leave the game\n4 - save")
        try:
            answer = int(input("> "))
            # up is debug command to trigger combat
            # if player enters up go into combat
            # if player enters stats print out the stats
            # if player enters exit, exit the game
            if answer <= 0:
                print('please use numbers between 1 - 4')
            if answer >= 5:
                print('please use numbers between 1 - 4')
            if answer == 1:
                # 100% chance to get into a fight
                event_picker()
            elif answer == 2:
                display_spell()
            elif answer == 3:
                exit(0)
            elif answer == 4:
                game.SavedGame.save_game()
                game.draw_line()
                print('the game is saving')
                game.print_dialogue('......')
                print('the game has saved')
        except ValueError:
            print('please use a number')
