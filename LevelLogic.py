import Pipe as game


def level_up():
    l_health, l_damage, l_mana = 0.0, 0.0, 1
    l_health += 1
    l_damage += 1
    while game.gameData.player['level']['exp'] >= game.gameData.player['level']['level_next']:
        game.draw_line()
        game.gameData.player['level']['level'] += 1
        game.gameData.player['level']['exp'] = game.gameData.player['level']['exp'] - \
                                               game.gameData.player['level']['level_next']
        game.gameData.player['level']['level_next'] = round(game.gameData.player['level']['level_next'] * 1.2)
        game.draw_line()
        print("Level: {}".format(game.gameData.player['level']['level']))
        print("EXP: {}".format(game.gameData.player['level']['exp']))
        print("Next Level: {}".format(game.gameData.player['level']['level_next']))
        hold_min_damage = game.gameData.player['stats']['damage']['min_damage']
        hold_max_damage = game.gameData.player['stats']['damage']['max_damage']
        game.gameData.player['stats']['max_health'] += l_health
        game.gameData.player['stats']['max_mana'] += l_mana
        game.gameData.player['stats']['damage']['min_damage'] += l_damage
        game.gameData.player['stats']['damage']['max_damage'] += l_damage
        old_stamina = game.gameData.player['stats']['max_stamina']
        game.gameData.player['stats']['max_stamina'] += 10
        game.draw_line()
        print(
            "{} max health --> {}  max health".format(game.gameData.player['stats']['max_health'] - l_health,
                                                      game.gameData.player['stats']['max_health']))
        print(
            "{} max mana --> {}  max mana".format(
                game.gameData.player['stats']['max_mana'] - l_mana,
                game.gameData.player['stats']['max_mana']
            )

        )
        print(
            "{} min damage, {} max damage --> {} min damage, {} max damage"
            .format(hold_min_damage, hold_max_damage, game.gameData.player['stats']['damage']['min_damage'],
                    game.gameData.player['stats']['damage']['max_damage']))

        print('Max SP {} --> {}'.format(old_stamina, game.gameData.player['stats']['max_stamina']))


def enemy_level_up():
    l_health, l_min_damage, l_max_damage, l_gold, l_exp = 3, 2, 3, 4, 4
    while game.gameData.player['level']['level'] >= game.gameData.world['world_level']:
        game.draw_line()
        game.gameData.world['world_level'] = round(game.gameData.world['world_level'] * 2)
        game.gameData.enemy_stat_ranges['enemy']['stats']['low_health'] += l_health
        game.gameData.enemy_stat_ranges['enemy']['stats']['max_health'] += l_health
        game.gameData.enemy_stat_ranges['enemy']['stats']['number_1_min_damage'] += l_min_damage
        game.gameData.enemy_stat_ranges['enemy']['stats']['number_1_max_damage'] += l_min_damage
        game.gameData.enemy_stat_ranges['enemy']['stats']['number_2_min_damage'] += l_max_damage
        game.gameData.enemy_stat_ranges['enemy']['stats']['number_2_max_damage'] += l_max_damage
        game.gameData.enemy_stat_ranges['enemy']['stats']['min_exp'] += l_exp
        game.gameData.enemy_stat_ranges['enemy']['stats']['max_exp'] += l_exp
        game.gameData.enemy_stat_ranges['enemy']['stats']['min_gold'] += l_gold
        game.gameData.enemy_stat_ranges['enemy']['stats']['max_gold'] += l_gold
        print('The enemies have gotten stronger be careful...')


def spell_level_up():
    l_min_damage, l_max_damage = 2, 4
    old_min_damage, old_max_damage = 0, 0
    old_mana_cost = 0
    l_mana_cost = 1
    for spell_slot in range(1, len(game.gameData.player['magic_slots']) + 1):
        if game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['name'] != '' and \
                game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['spell_used'] is True:
            game.draw_line()
            game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['proficiency'] += 1
            if game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['proficiency'] >= \
                    game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['proficiency_level_up']:
                game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['proficiency'] = \
                    game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['proficiency'] - \
                    game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['proficiency_level_up']

                game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['proficiency_level_up'] = \
                    round(game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['proficiency_level_up'] * 2)

                old_min_damage = game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['damage'][
                    'min_damage']
                old_max_damage = game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['damage'][
                    'max_damage']

                game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['damage'][
                    'min_damage'] += l_min_damage
                game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['damage'][
                    'max_damage'] += l_max_damage
                old_mana_cost = game.gameData.player_['magic_slots']['slot_{}'.format(spell_slot)]['mana_cost']
                game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['mana_cost'] += 2
                print("{} has leveled up".format(
                    game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)]['name']))
                print("min ATK spell {} --> {}".format(old_min_damage,
                                                       game.gameData.player['magic_slots'][
                                                           'slot_{}'.format(spell_slot)]['damage']['min_damage']))
                print("max ATK spell {} --> {}".format(old_max_damage,
                                                       game.gameData.player['magic_slots'][
                                                           'slot_{}'.format(spell_slot)]['damage']['max_damage']))
                print('mana cost {} --> {}'.format(old_mana_cost,
                                                   game.gameData.player['magic_slots']['slot_{}'.format(spell_slot)][
                                                       'mana_cost']))
                game.draw_line()


def physical_skill_level_up():
    l_bonus = 1
    old_bonus_damage = 0
    l_stamina_cost = 1
    old_stamina_cost = 0
    for physical_skill in range(1, len(game.gameData.player_skills['physical_skills']) + 1):
        if game.gameData.player_skills['physical_skills']['slot_{}'.format(physical_skill)]['name'] != '' and \
                game.gameData.player_skills['physical_skills']['slot_{}'.format(physical_skill)]['skill_used'] is True:
            game.draw_line()
            game.gameData.player_skills['physical_skills']['slot_{}'.format(physical_skill)]['proficiency'] += 1
            if game.gameData.player_skills['physical_skills']['slot_{}'.format(physical_skill)]['proficiency'] >= \
                    game.gameData.player_skills['physical_skills']['slot_{}'.format(physical_skill)][
                        'proficiency_level_up']:
                game.gameData.player_skills['physical_skills']['slot_{}'.format(physical_skill)]['proficiency'] = \
                    game.gameData.player_skills['physical_skills']['slot_{}'.format(physical_skill)]['proficiency'] - \
                    game.gameData.player_skills['physical_skills']['slot_{}'.format(physical_skill)][
                        'proficiency_level_up']

                game.gameData.player_skills['physical_skills']['slot_{}'.format(physical_skill)][
                    'proficiency_level_up'] = \
                    round(game.gameData.player_skills['physical_skills']['slot_{}'.format(physical_skill)][
                              'proficiency_level_up'] * 2)

                old_bonus_damage = game.gameData.player_skills['physical_skills'][
                    'slot_{}'.format(physical_skill)]['damage']['bonus_damage']
                game.gameData.player_skills['physical_skills'][
                    'slot_{}'.format(physical_skill)]['damage']['bonus_damage'] += l_bonus

                game.gameData.player_skills['physical_skills']['slot_{}'.format(physical_skill)]['stamina_cost'] += \
                    l_stamina_cost
                old_stamina_cost = \
                    game.gameData.player_skills['physical_skills']['slot_{}'.format(physical_skill)]['stamina_cost']

                print('bonus ATK {} ---> {}'.format(old_bonus_damage, game.gameData.player_skills['physical_skills'][
                    'slot_{}'.format(physical_skill)]['damage']['bonus_damage']))
                print('SP cost {} ---> {}'.format(old_stamina_cost, game.gameData.player_skills['physical_skills']
                ['slot_{}'.format(physical_skill)]['stamina_cost']))
                game.draw_line()


if __name__ == '__main__':
    exit('Please run main.py')
