import Pipe as game


def event_picker():
    if game.ran.random() < 1:
        game.combatLogic.in_combat()


if __name__ == '__main__':
    # Runs at the start of the game
    game.playerCreation.player_class()
    # Main game loop
    while True:
        option = ['up', 'left', 'right', 'stats', 'exit']
        print('----------------------------')
        print("Up: Move up\nStats: Shows your stats\nExit: To leave the game")
        answer = input("> ").lower().strip()
        if answer in option:
            # up is debug command to trigger combat
            # if player enters up go into combat
            # if player enters stats print out the stats
            # if player enters exit, exit the game
            if answer == 'up':
                # 100% chance to get into a fight
                event_picker()
            elif answer == 'stats':
                print("----------------------------")
                print("Level: {}".format(game.gameData.player['level']['level']))
                print("Max health: {}".format(game.gameData.player['stats']['max_health']))
                print("Health: {}".format(game.gameData.player['stats']['health']))
                print("Max mana: {}".format(game.gameData.player['stats']['max_mana']))
                print("Mana: {}".format(game.gameData.player['stats']['mana']))
                print("Min damage: {}\nMax damage: {}"
                      .format(game.gameData.player['stats']['damage']['min_damage'],
                              game.gameData.player['stats']['damage']['max_damage']))
                print("EXP: {}".format(game.gameData.player['level']['exp']))
                print("Speed: {}".format(game.gameData.player['stats']['speed']))
                print("Dodge: {}".format(game.gameData.player['stats']['dodge']))
                print("Level next: {}".format(game.gameData.player['level']['level_next']))
                # Test this when enemies are working again
                for spell_slot in range(len(game.gameData.player['magic_slots'])):
                    if game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['name'] != '':
                        print("slot {} is active".format(spell_slot))
                        print("Spell in slot {}".format(spell_slot))
                        print("name: {}".format(game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]
                                                ['name']))
                        print("mana cost: {}".format(game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]
                                                     ['mana_cost']))
                        print("Min damage: {}\nMax damage: {}".format(game.gameData.player['magic_slots']
                                                                      ['slot_{}'.format(spell_slot)]['damage']
                                                                      ['min_damage'],
                                                                      game.gameData.player['magic_slots']
                                                                      ['slot_{}'.format(spell_slot)]['damage']
                                                                      ['max_damage']))
                        print("Proficiency: {}".format(game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)
                                                       ]['proficiency']))
                        print("Proficiency level up: {}".format(game.gameData.player['magic_slots']['slot_{}'
                                                                .format(spell_slot)]['proficiency_level_up']))
            elif answer == 'exit':
                exit(0)
        else:
            print('please use a word to select your choices')

if __name__ == '__main__':
    exit('Please run main.py')
