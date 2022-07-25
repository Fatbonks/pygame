import Pipe as game


def do_damage(bonus_damage, slot):
    dmg = game.ran.randint(int(game.gameData.player['stats']['damage']['min_damage']),
                           int(game.gameData.player['stats']['damage']['max_damage']))
    dmg += bonus_damage
    game.gameData.enemy['stats']['health'] -= dmg

    if game.gameData.player['stats']['health'] <= 0:
        game.gameData.enemy['stats']['health'] += dmg
    elif game.gameData.enemy['stats']['health'] <= 0:
        game.draw_line()
        print("{} has been slain by {}".format(game.gameData.enemy['name'], game.gameData.player['name']))
        game.gameData.has_healed = False
        if game.gameData.player['stats']['health'] > game.gameData.player['stats']['max_health']:
            game.gameData.player['stats']['health'] = game.gameData.player['stats']['max_health']
        game.gameData.player['stats']['stamina'] = game.gameData.player['stats']['max_stamina']
        game.gameData.player['bag']['gold'] += game.gameData.enemy['drops']['gold']
        game.gameData.player['level']['exp'] += game.gameData.enemy['level']['exp']
        game.draw_line()
        print('you gained {} smeckles! and {} EXP'.format(
            game.gameData.enemy['drops']['gold'], game.gameData.enemy['level']['exp']
        )
        )
        game.levelLogic.physical_skill_level_up()
        game.gameData.player_skills['physical_skills']['slot_1']['skill_used'] = False
        game.gameData.player_skills['physical_skills']['slot_2']['skill_used'] = False
        game.gameData.player_skills['physical_skills']['slot_3']['skill_used'] = False
        game.gameData.player_skills['physical_skills']['slot_4']['skill_used'] = False
        game.levelLogic.level_up()
        game.levelLogic.enemy_level_up()
    else:
        print('you uses {} on {} and deal {}'.format(
                                        game.gameData.player_skills['physical_skills']['slot_{}'.format(slot)]['name'],
                                        game.gameData.enemy['name'], dmg
                                        ))
        game.draw_line()


def take_damage():
    dmg = game.ran.randint(int(game.gameData.enemy['stats']['damage']['min_damage']),
                           int(game.gameData.enemy['stats']['damage']['max_damage']))
    game.gameData.player['stats']['health'] -= dmg
    if game.gameData.enemy['stats']['health'] <= 0:
        game.gameData.player['stats']['health'] += dmg
    elif game.gameData.player['stats']['health'] <= 0:
        print("{} has been slain by {}".format(game.gameData.player['name'], game.gameData.enemy['name']))
        game.draw_line()
        input('press enter to leave')
        exit(0)
    else:
        print('{} attacks and deals {} damage to you'.format(game.gameData.enemy['name'], dmg))
        game.draw_line()


def combat_attacking(bonus_damage, acc, slot):
    if game.gameData.player['stats']['speed'] >= game.gameData.enemy['stats']['speed']:
        if acc > game.ran.random():
            do_damage(bonus_damage, slot)
            if game.gameData.player['stats']['dodge'] / 100 > game.ran.random():
                if game.gameData.enemy['stats']['health'] > 0:
                    print("{} dodged the enemies attack".format(game.gameData.player['name']))
                    if game.gameData.player['class'] == 'thief':
                        do_damage(bonus_damage, slot)
            else:
                take_damage()
        else:
            print('you missed you attack')
            take_damage()
    else:
        if game.gameData.player['stats']['dodge'] / 100 > game.ran.random():
            if game.gameData.enemy['stats']['health'] > 0:
                print("{} dodged the enemies attack".format(game.gameData.player['name']))
                if acc > game.ran.random():
                    do_damage(bonus_damage, slot)
                else:
                    print('but you missed your attack')
        else:
            take_damage()
            if acc > game.ran.random():
                do_damage(bonus_damage, slot)
            else:
                print('you missed your attack')


def display_stats(enemy_health):
    game.clear()
    game.draw_line()
    print('Defeat {} {}!'.format(game.gameData.enemy['name'], game.gameData.enemy['title']))
    game.draw_line()
    print("{}'s HP: {}/{}".format(game.gameData.enemy['name'], game.gameData.enemy['stats']['health'], enemy_health))
    print("{}'s ATK: {} - {}".format(
        game.gameData.enemy['name'], game.gameData.enemy['stats']['damage']['min_damage'],
        game.gameData.enemy['stats']['damage']['max_damage']
    )
    )
    print("{}'s SPD: {}".format(game.gameData.enemy['name'], game.gameData.enemy['stats']['speed']))
    game.draw_line()
    print("{}'s HP: {}/{}".format(
        game.gameData.player['name'], game.gameData.player['stats']['health'],
        game.gameData.player['stats']['max_health']
    )
    )
    print("{}'s SP: {}/{}".format(
        game.gameData.player['name'], game.gameData.player['stats']['stamina'],
        game.gameData.player['stats']['max_stamina']
    )
    )
    print("{}'s MP: {}/{}".format(
        game.gameData.player['name'], game.gameData.player['stats']['mana'],
        game.gameData.player['stats']['max_mana']
    )
    )
    print("{}'s ATK: {} - {}".format(
        game.gameData.player['name'], game.gameData.player['stats']['damage']['min_damage'],
        game.gameData.player['stats']['damage']['max_damage']
    )
    )
    print("{}'s SPD: {}".format(
        game.gameData.player['name'], game.gameData.player['stats']['speed']
    )
    )
    print("{}'s SMECKLES: {}".format(game.gameData.player['name'], game.gameData.player['bag']['gold']))
    game.draw_line()


def display_option():
    game.time.sleep(1.5)
    print('1 - Physical ATK\n2 - Use spells\n3 - Run\n4 - Bag')
    game.draw_line()


def combat_display():
    game.enemyCreation.random_enemy()
    enemy_health = game.gameData.enemy['stats']['health']
    while game.gameData.player['stats']['health'] > 0 and game.gameData.enemy['stats']['health'] > 0:
        try:
            display_stats(enemy_health)
            display_option()
            ans = int(input('> ').lower().strip())
            if ans == 1:
                game.draw_line()
                if game.gameData.player_skills['physical_skills']['slot_1']['name'] != '':
                    print('1 - {} (ACC: {:.0f} | Bonus DMG {} | SP cost: {})'.format(
                        game.gameData.player_skills['physical_skills']['slot_1']['name'],
                        game.gameData.player_skills['physical_skills']['slot_1']['accuracy'] * 100,
                        game.gameData.player_skills['physical_skills']['slot_1']['damage']['bonus_damage'],
                        game.gameData.player_skills['physical_skills']['slot_1']['stamina_cost']
                                                                  )
                          )
                else:
                    print('1 -')
                if game.gameData.player_skills['physical_skills']['slot_2']['name'] != '':
                    print('2 - {} (ACC: {:.0f} | Bonus DMG {} | SP cost: {})'.format(
                        game.gameData.player_skills['physical_skills']['slot_2']['name'],
                        game.gameData.player_skills['physical_skills']['slot_2']['accuracy'] * 100,
                        game.gameData.player_skills['physical_skills']['slot_2']['damage']['bonus_damage'],
                        game.gameData.player_skills['physical_skills']['slot_2']['stamina_cost']
                                                                  )
                          )
                else:
                    print('2 -')
                if game.gameData.player_skills['physical_skills']['slot_3']['name'] != '':
                    print('3 - {} (ACC: {:.0f} | Bonus DMG {} | SP cost: {})'.format(
                        game.gameData.player_skills['physical_skills']['slot_3']['name'],
                        game.gameData.player_skills['physical_skills']['slot_3']['accuracy'] * 100,
                        game.gameData.player_skills['physical_skills']['slot_3']['damage']['bonus_damage'],
                        game.gameData.player_skills['physical_skills']['slot_3']['stamina_cost']
                    )
                          )
                else:
                    print('3 -')
                if game.gameData.player_skills['physical_skills']['slot_4']['name'] != '':
                    print('4 - {} (ACC: {:.0f} | Bonus DMG {} | SP cost: {})'.format(
                        game.gameData.player_skills['physical_skills']['slot_4']['name'],
                        game.gameData.player_skills['physical_skills']['slot_4']['accuracy'] * 100,
                        game.gameData.player_skills['physical_skills']['slot_4']['damage']['bonus_damage'],
                        game.gameData.player_skills['physical_skills']['slot_4']['stamina_cost']
                    )
                          )
                else:
                    print('4 -')
                print('5: Back')
                ans_skill_slot = int(input('> ').lower().strip())
                if ans_skill_slot <= 0:
                    print('Please pick a number between 1 - 5')
                    input('press enter to leave')
                elif ans_skill_slot >= 6:
                    print('Please pick a number between 1 - 5')
                    input('press enter to leave')
                elif ans_skill_slot == 5:
                    pass
                elif len(game.gameData.player_skills['physical_skills']) >= ans >= 1:
                    if game.gameData.player_skills['physical_skills']['slot_{}'.format(ans_skill_slot)]['name'] != '':
                        if game.gameData.player['stats']['stamina'] >= \
                                game.gameData.player_skills['physical_skills']['slot_{}'.format(ans_skill_slot)][
                                    'stamina_cost']:
                            display_stats(enemy_health)
                            game.combatLogic.combat_attacking(game.gameData.player_skills
                                                              ['physical_skills']['slot_{}'.format(ans_skill_slot)]
                                                              ['damage']['bonus_damage'], game.gameData.player_skills
                                                              ['physical_skills']['slot_{}'.format(ans_skill_slot)]
                                                              ['accuracy'], ans_skill_slot
                                                              )
                            input('press enter to leave')
                            if game.gameData.enemy['stats']['health'] <= 0:
                                game.clear()
                                break
                            game.gameData.player['stats']['stamina'] -= \
                                game.gameData.player_skills['physical_skills']['slot_{}'.format(ans_skill_slot)][
                                    'stamina_cost']
                        else:
                            print(
                                'You dont have enough mana you have {} SP left'.format(
                                    game.gameData.player['stats']['stamina']
                                )
                            )
                            input('press enter')
                    else:
                        print(
                            'That slot does not have an ability please use one that does have a ability')
                        input('press enter to leave')
                else:
                    print('That slot is invalid please choose again')
                    input('press enter to leave')
            elif ans == 2:
                game.draw_line()
                print('1 - {}\n2 - {}\n3 - {}\n4 - {}'.format(
                    game.gameData.player['magic_slots']['slot_1']['name'],
                    game.gameData.player['magic_slots']['slot_2']['name'],
                    game.gameData.player['magic_slots']['slot_3']['name'],
                    game.gameData.player['magic_slots']['slot_4']['name']
                )
                )
                print('5: Back')
                ans_magic_slot = int(input('> ').lower().strip())
                if ans_magic_slot <= 0:
                    print('Please pick a number between 1 - 5')
                    input('press enter to leave')
                elif ans_magic_slot >= 6:
                    print('Please pick a number between 1 - 5')
                    input('press enter to leave')
                elif ans_magic_slot == 5:
                    pass
                elif len(game.gameData.player['magic_slots']) >= ans >= 1:
                    if game.gameData.player['magic_slots']['slot_{}'.format(ans_magic_slot)]['name'] != '':
                        if game.gameData.player['stats']['mana'] >= \
                                game.gameData.player['magic_slots']['slot_{}'.format(ans_magic_slot)]['mana_cost']:
                            display_stats(enemy_health)
                            game.magicLogic.magic_attacking(ans_magic_slot)
                            input('press enter to leave')
                            if game.gameData.enemy['stats']['health'] <= 0:
                                game.clear()
                                break
                            game.gameData.player['stats']['mana'] -= \
                                game.gameData.player['magic_slots']['slot_{}'.format(ans_magic_slot)]['mana_cost']
                        else:
                            print(
                                'you dont have enough mana you have {} mana left'.format(
                                    game.gameData.player['stats']['mana']
                                )
                            )
                            input('press enter')
                    else:
                        print(
                            'That slot does not have an ability please use one that does have a ability')
                        input()
                else:
                    print('That slot is invalid please choose again')
                    input('press enter to leave')
            elif ans == 3:
                if game.ran.random() < 0.5:
                    print('You ran away!')
                    game.clear()
                    break
                else:
                    print(
                        'The {} did not let you escape and he attacked you'.format(game.gameData.enemy['name']))
                    take_damage()
                    input('press enter to leave')
            elif ans == 4:
                print('1 - Health potions: {}\n2 - Drugs: {}'.format(
                    game.gameData.player['bag']['health_potion'], game.gameData.player['bag']['Drugs'])
                )
                try:
                    ans_2 = int(input('>'))
                    if ans_2 == 1:
                        if game.gameData.player['bag']['health_potion'] > 0:
                            pass
                        else:
                            print('you dont have any health potions')
                            input('press enter')
                    if ans_2 == 2:
                        if game.gameData.player['bag']['Drugs'] > 0:
                            game.healingLogic.drugs_healing()
                        else:
                            print('you dont have any drugs')
                            input('press enter')
                except ValueError:
                    pass

        except ValueError:
            print('please use a number')


if __name__ == '__main__':
    exit('Please run main.py')
