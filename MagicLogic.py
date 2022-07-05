import Pipe as game


def give_magic():
    game.print_dialogue('Learn a spell of legends young mage, now which do you desire?\n1: Fireball\n2: Water '
                        'whip\n3: Air blades\n4: earthquake\n5: I don\'t know')
    ans = int(input('> ').lower().strip())
    if ans == 1:
        magic = game.gameData.magic['fire']['fireball']
    elif ans == 2:
        magic = game.gameData.magic['water']['water_whip']
    elif ans == 3:
        magic = game.gameData.magic['air']['air_blades']
    elif ans == 4:
        magic = game.gameData.magic['earth']['earthquake']
    elif ans == 5:
        game.print_dialogue('Fool a mage must always be certain of themself')
        game.print_dialogue('Be certain when to hold in their farts or not, it\'s a matter of life and death!')
        game.print_dialogue('I see you find that funny don\'t you well we will teach you no longer we will see whose '
                            'laughing then!')
        return
    game.print_dialogue('what slot would you like to assign it to\n1: slot 1\n2: slot 2\n3: slot 3\n4: slot 4')
    ans2 = int(input('> ').lower().strip())

    magic_slot_adder(magic, ans2)


def magic_attacking(ans):
    if game.gameData.player['stats']['speed'] >= game.gameData.enemy['stats']['speed']:
        do_magical_damage(ans)
        if game.gameData.player['stats']['dodge'] / 100 > game.ran.random():
            if game.gameData.enemy['stats']['health'] > 0:
                game.print_dialogue('{} dodged the enemies attack'.format(game.gameData.player['name']))
                if game.gameData.player['class'] == 'thief':
                    do_magical_damage(ans)
        else:
            game.combatLogic.take_damage()
    else:
        if game.gameData.player['stats']['dodge'] / 100 > game.ran.random():
            if game.gameData.enemy['stats']['health'] > 0:
                game.print_dialogue('{} dodged the enemies attack'.format(game.gameData.player['name']))
                do_magical_damage(ans)
        else:
            game.combatLogic.take_damage()
            do_magical_damage(ans)
    game.levelLogic.level_up()


def magic_slot_adder(magic, ans):
    if len(game.gameData.player['magic_slots']) >= ans >= 1:
        if game.gameData.player['magic_slots']['slot_{}'.format(ans)]['name'] == '':
            game.gameData.player['magic_slots']['slot_{}'.format(ans)] = magic


def do_magical_damage(ans):
    if len(game.gameData.player['magic_slots']) >= ans >= 1:
        dmg = game.ran.randint(int(game.gameData.player['magic_slots']['slot_{}'.format(ans)]['damage']['min_damage']),
                               int(game.gameData.player['magic_slots']['slot_{}'.format(ans)]['damage']['max_damage']))
    game.gameData.enemy['stats']['health'] -= dmg

    if game.gameData.player['stats']['health'] <= 0:
        game.gameData.enemy['stats']['health'] += dmg
    elif game.gameData.enemy['stats']['health'] <= 0:
        game.draw_line()
        print('{} has been slain by {}'.format(game.gameData.enemy['name'], game.gameData.player['name']))
        game.gameData.has_healed = False
        if game.gameData.player['stats']['health'] > game.gameData.player['stats']['max_health']:
            game.gameData.player['stats']['health'] = game.gameData.player['stats']['max_health']
        game.levelLogic.spell_level_up()
        game.gameData.player['magic_slots']['slot_1']['spell_used'] = False
        game.gameData.player['magic_slots']['slot_2']['spell_used'] = False
        game.gameData.player['magic_slots']['slot_3']['spell_used'] = False
        game.gameData.player['magic_slots']['slot_4']['spell_used'] = False
        game.levelLogic.level_up()
        game.levelLogic.enemy_level_up()

        # Restore mana to max if they are a mage and then give rewards for winning the fight.
        if game.gameData.player['class'] == 'mage':
            game.gameData.player['stats']['mana'] = game.gameData.player['stats']['max_mana']
        game.gameData.player['bag']['gold'] += game.gameData.enemy['drops']['gold']
        game.gameData.player['level']['exp'] += game.gameData.enemy['level']['exp']
        game.draw_line()
        print('you gained {} smeckles! and {} EXP'.format(
            game.gameData.enemy['drops']['gold'], game.gameData.enemy['level']['exp']
        )
        )
    else:
        print('you use {} on {} and deal {}'.format(game.gameData.player['magic_slots']['slot_{}'.format(ans)]['name'],
                                                    game.gameData.enemy['name'], dmg
                                                    ))


if __name__ == '__main__':
    exit('Please run main.py')
