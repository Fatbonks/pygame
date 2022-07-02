import Pipe as game


def level_up():
    l_health, l_damage, l_mana = 0.0, 0.0, 1
    l_health += 1
    l_damage += 1
    while game.gameData.player['level']['exp'] >= game.gameData.player['level']['level_next']:
        game.gameData.player['level']['level'] += 1
        game.gameData.player['level']['exp'] = game.gameData.player['level']['exp'] - \
                                               game.gameData.player['level']['level_next']
        game.gameData.player['level']['level_next'] = round(game.gameData.player['level']['level_next'] * 1.2)
        game.print_dialogue("----------------------")
        game.print_dialogue("Level: {}".format(game.gameData.player['level']['level']))
        game.print_dialogue("EXP: {}".format(game.gameData.player['level']['exp']))
        game.print_dialogue("Next Level: {}".format(game.gameData.player['level']['level_next']))
        hold_min_damage = game.gameData.player['stats']['damage']['min_damage']
        hold_max_damage = game.gameData.player['stats']['damage']['max_damage']
        game.gameData.player['stats']['max_health'] += l_health
        game.gameData.player['stats']['max_mana'] += l_mana
        game.gameData.player['stats']['damage']['min_damage'] += l_damage
        game.gameData.player['stats']['damage']['max_damage'] += l_damage
        game.print_dialogue("-------------------")
        game.print_dialogue(
            "{} max health --> {}  max health".format(game.gameData.player['stats']['max_health'] - l_health,
                                                      game.gameData.player['stats']['max_health']))
        game.print_dialogue(
            "{} max mana --> {}  max mana".format(
                game.gameData.player['stats']['max_mana'] - l_mana,
                game.gameData.player['stats']['max_mana']
            )

        )
        game.print_dialogue(
            "{} min damage, {} max damage --> {} min damage, {} max damage"
            .format(hold_min_damage, hold_max_damage, game.gameData.player['stats']['damage']['min_damage'],
                    game.gameData.player['stats']['damage']['max_damage']))


def enemy_level_up():
    l_health, l_min_damage, l_max_damage, l_gold, l_exp = 3, 2, 3, 4, 4
    while game.gameData.player['level']['level'] >= game.gameData.world['world_level']:
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
        game.print_dialogue('The enemies have gotten stronger be careful...')


def spell_level_up():
    pass


if __name__ == '__main__':
    exit('Please run main.py')
