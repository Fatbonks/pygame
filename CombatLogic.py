import Pipe as game


def do_damage():
    dmg = game.ran.randint(int(game.gameData.player['stats']['damage']['min_damage']),
                           int(game.gameData.player['stats']['damage']['max_damage']))
    game.gameData.enemy['stats']['health'] -= dmg

    if game.gameData.player['stats']['health'] <= 0:
        game.gameData.enemy['stats']['health'] += dmg
    elif game.gameData.enemy['stats']['health'] <= 0:
        print("------------------")
        print("{} has been slain by {}".format(game.gameData.enemy['name'], game.gameData.player['name']))
        print("{} has {:.2f} health left".format(game.gameData.player['name'], game.gameData.player['stats']['health']))
        gain_health = 0
        gain_health += game.gameData.player['stats']['max_health'] / 2
        game.gameData.player['stats']['health'] += gain_health
        print('you gain {} hp back!'.format(gain_health))
        if game.gameData.player['stats']['health'] > game.gameData.player['stats']['max_health']:
            game.gameData.player['stats']['health'] = game.gameData.player['stats']['max_health']
        game.gameData.player['bag']['gold'] += game.gameData.enemy['drops']['gold']
        game.gameData.player['level']['exp'] += game.gameData.enemy['level']['exp']
        print('you gained {} smeckles! and you gained {} EXP'.format(
            game.gameData.enemy['drops']['gold'], game.gameData.enemy['level']['exp']
            )
        )
    else:
        print("------------------")
        print("{} takes {} damage".format(game.gameData.enemy['name'], dmg))
        print("{} health is {}\nThe {} health is {}".format(game.gameData.player['name'],
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
        print("{} has been slain by {}".format(game.gameData.player['name'], game.gameData.enemy['name']))
        input('press enter to leave')
        exit(0)
    else:
        print("------------------")
        print("{} takes {} damage".format(game.gameData.player['name'], dmg))
        print("{} health is {}\nThe {} health is {}".format(game.gameData.player['name'],
                                                            game.gameData.player['stats']['health'],
                                                            game.gameData.enemy['name'],
                                                            game.gameData.enemy['stats']['health']))


def in_combat():
    game.enemyCreation.random_enemy()
    print("------------------")
    print(
        "You have encountered {}, I hope you can win!\n{} has {} hp\n{} has {} min_damage\n{} has {} max_damage".format(
            game.gameData.enemy['name'], game.gameData.enemy['name'], game.gameData.enemy['stats']['health'],
            game.gameData.enemy['name'], game.gameData.enemy['stats']['damage']['min_damage'],
            game.gameData.enemy['name'], game.gameData.enemy['stats']['damage']['max_damage']
            )
          )
    while game.gameData.player['stats']['health'] > 0 and game.gameData.enemy['stats']['health'] > 0:
        print("------------------")
        print("1: Attack\n2: Magic attack\n3: Run")
        ans = int(input('> ').lower().strip())
        if ans == 1:
            if game.gameData.player['stats']['speed'] >= game.gameData.enemy['stats']['speed']:
                do_damage()
                game.time.sleep(2.5)
                if game.gameData.player['stats']['dodge'] / 100 > game.ran.random():
                    if game.gameData.enemy['stats']['health'] > 0:
                        print("{} dodged the enemies attack".format(game.gameData.player['name']))
                        do_damage()
                else:
                    take_damage()
                    game.time.sleep(2.5)
            else:
                if game.gameData.player['stats']['dodge'] / 100 > game.ran.random():
                    if game.gameData.enemy['stats']['health'] > 0:
                        print("{} dodged the enemies attack".format(game.gameData.player['name']))
                        do_damage()
                else:
                    take_damage()
                    game.time.sleep(2.5)
                    do_damage()
            game.time.sleep(2.5)
            game.levelLogic.level_up()
        elif ans == 2:
            print('your mana is {}'.format(game.gameData.player['stats']['mana']))
            print('0: {}\n1: {}\n2: {}\n3: {}\n'.format(
                game.gameData.player['magic_slots']['slot_0']['name'],
                game.gameData.player['magic_slots']['slot_1']['name'],
                game.gameData.player['magic_slots']['slot_2']['name'],
                game.gameData.player['magic_slots']['slot_3']['name']
            )
            )
            ans_magic_slot = int(input('> ').lower().strip())
            if ans_magic_slot == 0 and game.gameData.player['magic_slots']['slot_0']['name'] != '':
                if game.gameData.player['stats']['mana'] >= game.gameData.player['magic_slots']['slot_0']['mana_cost']:
                    game.magicLogic.magic_attacking(ans_magic_slot)
                    #game.gameData.player['stats']['mana'] -= game.gameData.player['magic_slots']['slot_0'][
                        #'mana_cost']
                else:
                    print(
                        'you dont have enough mana you have {} mana left'.format(
                            game.gameData.player['stats']['mana']
                        )
                    )
            elif ans_magic_slot == 1 and game.gameData.player['magic_slots']['slot_1']['name'] != '':
                if game.gameData.player['stats']['mana'] >= game.gameData.player['magic_slots']['slot_1']['mana_cost']:
                    game.magicLogic.magic_attacking(ans_magic_slot)
                    #game.gameData.player['stats']['mana'] -= game.gameData.player['magic_slots']['slot_1'][
                        #'mana_cost']
                else:
                    print(
                        'you dont have enough mana you have {} mana left'.format(
                            game.gameData.player['stats']['mana']
                        )
                    )
            elif ans_magic_slot == 2 and game.gameData.player['magic_slots']['slot_2']['name'] != '':
                if game.gameData.player['stats']['mana'] >= game.gameData.player['magic_slots']['slot_2']['mana_cost']:
                    game.magicLogic.magic_attacking(ans_magic_slot)
                    #game.gameData.player['stats']['mana'] -= game.gameData.player['magic_slots']['slot_2'][
                        #'mana_cost']
                else:
                    print(
                        'you dont have enough mana you have {} mana left'.format(
                            game.gameData.player['stats']['mana']
                        )
                    )
            elif ans_magic_slot == 3 and game.gameData.player['magic_slots']['slot_3']['name'] != '':
                if game.gameData.player['stats']['mana'] >= game.gameData.player['magic_slots']['slot_3']['mana_cost']:
                    game.magicLogic.magic_attacking(ans_magic_slot)
                    #game.gameData.player['stats']['mana'] -= game.gameData.player['magic_slots']['slot_3'][
                        #'mana_cost']
                else:
                    print(
                        'you dont have enough mana you have {} mana left'.format(
                            game.gameData.player['stats']['mana']
                        )
                    )
            else:
                print('That slot does not have an ability please use one that does have an a ability')

        elif ans == 3:
            if game.ran.random() < 0.5:
                print('you ran away!')
                break
            else:
                print('the {} did not let you escape and he attacked you'.format(game.gameData.enemy['name']))
                take_damage()


if __name__ == '__main__':
    exit('Please run main.py')
