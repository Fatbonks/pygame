import Pipe as game





def display_stats():
    game.draw_line()
    print('Name: {}'.format(game.gameData.player['name']))
    print('-------')
    print('Class: {} | Race: {}'.format(game.gameData.player['class'], game.gameData.player['race']))
    print('Level: {} | Level_next: {} | EXP: {}'.format(
        game.gameData.player['level']['level'], game.gameData.player['level']['level_next'],
        game.gameData.player['level']['exp']
    )
    )
    print('MX_HP: {} | Health: {}'.format(game.gameData.player['stats']['max_health'],
                                          game.gameData.player['stats']['health']))
    print('MX_MP: {} | Mana: {}'.format(game.gameData.player['stats']['max_mana'],
                                        game.gameData.player['stats']['mana']))
    print('-------')
    print('SPD: {}'.format(game.gameData.player['stats']['speed']))
    print('DMG: {} - {}'.format(game.gameData.player['stats']['damage']['min_damage'],
                                game.gameData.player['stats']['damage']['max_damage']))
    print('Dodge: {}'.format(game.gameData.player['stats']['dodge']))
    print('Smeckles: {}'.format(game.gameData.player['bag']['gold']))
    print('Drugs: {}'.format(game.gameData.player['bag']['Drugs']))
    game.draw_line()
    input('press enter to leave')


def display_skills():
    game.clear()
    for skill_slot in range(1, len(game.gameData.player_skills['physical_skills']) + 1):
        if game.gameData.player_skills['physical_skills']['slot_{}'.format(skill_slot)]['name'] != '':
            print('Skill in slot {}'.format(skill_slot))
            print('-------')
            print('{}:'.format(game.gameData.player_skills['physical_skills']['slot_{}'.format(skill_slot)]['name']))
            print('SP Cost: {} | Accuracy: {:.0f}'.format(
                game.gameData.player_skills['physical_skills']['slot_{}'.format(skill_slot)]['stamina_cost'],
                game.gameData.player_skills['physical_skills']['slot_{}'.format(skill_slot)]['accuracy'] * 100)
            )
            print('Bonus Damage: {}'.format(game.gameData.player_skills['physical_skills']['slot_{}'.format(skill_slot)]
                                            ['damage']['bonus_damage']))
            print('Proficiency: {} | Proficiency level up: {}'.format(
                game.gameData.player_skills['physical_skills']['slot_{}'.format(skill_slot)]['proficiency'],
                game.gameData.player_skills['physical_skills']['slot_{}'.format(skill_slot)]['proficiency_level_up'])
            )
            game.draw_line()


def display_spell():
    game.clear()
    for spell_slot in range(1, len(game.gameData.player['magic_slots']) + 1):
        if game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['name'] != '':
            game.draw_line()
            print('Spell in slot {}'.format(spell_slot))
            print('-------')
            print('{}:'.format(game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['name']))
            print('mana cost: {}'.format(game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['mana_cost'])
                  )
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
        game.gameData.map = 'World Map'
        game.map_creation.create_map(game.gameData.world_map, game.gameData.biome,
                                     game.gameData.player_x_world,
                                     game.gameData.player_y_world)
