import Pipe as game


def do_damage():
    dmg = game.ran.randint(int(game.gameData.player['stats']['damage']['min_damage']),
                           int(game.gameData.player['stats']['damage']['max_damage']))
    game.gameData.enemy['stats']['health'] -= dmg

    if game.gameData.player['stats']['health'] <= 0:
        game.gameData.enemy['stats']['health'] += dmg
    elif game.gameData.enemy['stats']['health'] <= 0:
        game.print_dialogue("------------------")
        game.print_dialogue("{} has been slain by {}".format(game.gameData.enemy['name'], game.gameData.player['name']))
        game.print_dialogue(
            "{} has {:.1f} health left".format(game.gameData.player['name'], game.gameData.player['stats']['health']))
        gain_health = 0
        gain_health += round(game.gameData.player['stats']['max_health'] / 2)
        game.gameData.player['stats']['health'] += gain_health
        game.print_dialogue('you gain {} hp back!'.format(gain_health))
        if game.gameData.player['stats']['health'] > game.gameData.player['stats']['max_health']:
            game.gameData.player['stats']['health'] = game.gameData.player['stats']['max_health']
        game.gameData.player['bag']['gold'] += game.gameData.enemy['drops']['gold']
        game.gameData.player['level']['exp'] += game.gameData.enemy['level']['exp']
        game.print_dialogue('you gained {} smeckles! and {} EXP'.format(
            game.gameData.enemy['drops']['gold'], game.gameData.enemy['level']['exp']
        )
        )
    else:
        game.print_dialogue("------------------")
        game.print_dialogue("{} takes {} damage".format(game.gameData.enemy['name'], dmg))
        game.print_dialogue("{} health is {}\n {} health is {}".format(game.gameData.player['name'],
                                                                       game.gameData.player['stats']['health'],
                                                                       game.gameData.enemy['name'],
                                                                       game.gameData.enemy['stats']['health']))


def take_damage():
    dmg = game.ran.randint(int(game.gameData.enemy['stats']['damage']['min_damage']),
                           int(game.gameData.enemy['stats']['damage']['max_damage']))
    game.gameData.player['stats']['health'] -= dmg
    if game.gameData.enemy['stats']['health'] <= 0:
        game.gameData.player['stats']['health'] += dmg
    elif game.gameData.player['stats']['health'] <= 0:
        game.print_dialogue("{} has been slain by {}".format(game.gameData.player['name'], game.gameData.enemy['name']))
        input('press enter to leave')
        exit(0)
    else:
        game.print_dialogue("------------------")
        game.print_dialogue("{} takes {} damage".format(game.gameData.player['name'], dmg))
        game.print_dialogue("{} health is {}\nThe {} health is {}".format(game.gameData.player['name'],
                                                                          game.gameData.player['stats']['health'],
                                                                          game.gameData.enemy['name'],
                                                                          game.gameData.enemy['stats']['health']))


def in_combat():
    game.enemyCreation.random_enemy()
    game.print_dialogue("------------------")
    game.print_dialogue(
        "You have encountered {}, I hope you can win!\n{} has {} hp\n{} has {} min_damage\n{} has {} max_damage\n"
        "{} has {} speed".format(
            game.gameData.enemy['name'], game.gameData.enemy['name'], game.gameData.enemy['stats']['health'],
            game.gameData.enemy['name'], game.gameData.enemy['stats']['damage']['min_damage'],
            game.gameData.enemy['name'], game.gameData.enemy['stats']['damage']['max_damage'],
            game.gameData.enemy['name'], game.gameData.enemy['stats']['speed']
        )
    )
    while game.gameData.player['stats']['health'] > 0 and game.gameData.enemy['stats']['health'] > 0:
        game.print_dialogue("------------------")
        game.print_dialogue("1: Attack\n2: Magic attack\n3: Run\n4: call god to give you drugs")
        ans = int(input('> ').lower().strip())
        if ans == 1:
            if game.gameData.player['stats']['speed'] >= game.gameData.enemy['stats']['speed']:
                do_damage()
                if game.gameData.player['stats']['dodge'] / 100 > game.ran.random():
                    if game.gameData.enemy['stats']['health'] > 0:
                        game.print_dialogue("{} dodged the enemies attack".format(game.gameData.player['name']))
                        do_damage()
                else:
                    take_damage()
            else:
                if game.gameData.player['stats']['dodge'] / 100 > game.ran.random():
                    if game.gameData.enemy['stats']['health'] > 0:
                        game.print_dialogue("{} dodged the enemies attack".format(game.gameData.player['name']))
                        do_damage()
                else:
                    take_damage()
                    do_damage()
            game.levelLogic.level_up()
        elif ans == 2:
            game.print_dialogue('your mana is {}'.format(game.gameData.player['stats']['mana']))
            game.print_dialogue('1: {}\n2: {}\n3: {}\n4: {}\n'.format(
                game.gameData.player['magic_slots']['slot_1']['name'],
                game.gameData.player['magic_slots']['slot_2']['name'],
                game.gameData.player['magic_slots']['slot_3']['name'],
                game.gameData.player['magic_slots']['slot_4']['name']
            )
            )
            ans_magic_slot = int(input('> ').lower().strip())
            if len(game.gameData.player['magic_slots']) >= ans >= 1:
                if game.gameData.player['magic_slots']['slot_{}'.format(ans_magic_slot)]['name'] != '':
                    if game.gameData.player['stats']['mana'] >= \
                            game.gameData.player['magic_slots']['slot_{}'.format(ans_magic_slot)]['mana_cost']:
                        game.magicLogic.magic_attacking(ans_magic_slot)
                        game.gameData.player['stats']['mana'] -= \
                        game.gameData.player['magic_slots']['slot_{}'.format(ans_magic_slot)]['mana_cost']
                    else:
                        game.print_dialogue(
                            'you dont have enough mana you have {} mana left'.format(
                                game.gameData.player['stats']['mana']
                            )
                        )
                else:
                    game.print_dialogue('That slot does not have an ability please use one that does have an a ability')
            else:
                game.print_dialogue('That slot is invalid please choose again')

        elif ans == 3:
            if game.ran.random() < 0.5:
                game.print_dialogue('you ran away!')
                break
            else:
                game.print_dialogue(
                    'the {} did not let you escape and he attacked you'.format(game.gameData.enemy['name']))
                take_damage()
        elif ans == 4:
            pass

if __name__ == '__main__':
    exit('Please run main.py')
