import Pipe as game


def give_magic():
    print('what spell would you like?\n0: Fireball\n1: Water whip\n2: Air blades\n3: earthquake')
    ans = int(input('> ').lower().strip())
    if ans == 0:
        magic = game.gameData.magic['fire']['fireball']
    elif ans == 1:
        magic = game.gameData.magic['water']['water_whip']
    elif ans == 2:
        magic = game.gameData.magic['air']['air_blades']
    elif ans == 3:
        magic = game.gameData.magic['earth']['earthquake']
    print('what slot would you like to assign it to\n0: slot 0\n1: slot 1\n2: slot 2\n3: slot 3')
    ans2 = int(input('> ').lower().strip())

    magic_slot_adder(magic, ans2)


def magic_attacking(ans):
    if game.gameData.player['stats']['speed'] >= game.gameData.enemy['stats']['speed']:
        do_magical_damage(ans)
        game.time.sleep(2.5)
        if game.gameData.player['stats']['dodge'] / 100 > game.ran.random():
            if game.gameData.enemy['stats']['health'] > 0:
                print('{} dodged the enemies attack'.format(game.gameData.player['name']))
        else:
            game.combatLogic.take_damage()
            game.time.sleep(2.5)
    else:
        if game.gameData.player['stats']['dodge'] / 100 > game.ran.random():
            if game.gameData.enemy['stats']['health'] > 0:
                print('{} dodged the enemies attack'.format(game.gameData.player['name']))
        else:
            game.combatLogic.take_damage()
            game.time.sleep(2.5)
            do_magical_damage(ans)
    game.time.sleep(2.5)
    game.levelLogic.level_up()


def magic_slot_adder(magic, ans):
    if len(game.gameData.player['magic_slots']) - 1 >= ans >= 0:
        if game.gameData.player['magic_slots']['slot_{}'.format(ans)]['name'] == '':
            game.gameData.player['magic_slots']['slot_{}'.format(ans)] = magic


def do_magical_damage(ans):
    if len(game.gameData.player['magic_slots']) - 1 >= ans >= 0:
        dmg = game.ran.randint(int(game.gameData.player['magic_slots']['slot_{}'.format(ans)]['damage']['min_damage']),
                               int(game.gameData.player['magic_slots']['slot_{}'.format(ans)]['damage']['max_damage']))
    game.gameData.enemy['stats']['health'] -= dmg

    if game.gameData.player['stats']['health'] <= 0:
        game.gameData.enemy['stats']['health'] += dmg
    elif game.gameData.enemy['stats']['health'] <= 0:
        print('------------------')
        print('{} has been slain by {}'.format(game.gameData.enemy['name'], game.gameData.player['name']))
        print('{} has {} health left'.format(game.gameData.player['name'], game.gameData.player['stats']['health']))
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
        print('------------------')
        print('{} takes {} damage'.format(game.gameData.enemy['name'], dmg))
        print('{} health is {}\nThe {} health is {}'.format(game.gameData.player['name'],
                                                            game.gameData.player['stats']['health'],
                                                            game.gameData.enemy['name'],
                                                            game.gameData.enemy['stats']['health']))


if __name__ == '__main__':
    exit('Please run main.py')
