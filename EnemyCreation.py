import Pipe as game


# 'stats': {'health': 0.0, 'damage': {'min_damage': 0.0, 'max_damage': 0.0}, 'speed': 0},

# 'level': {'level': 0, 'exp': 0}, 'drops': {'gold': 0}


def random_enemy():
    game.gameData.blank_enemy['enemy']['stats']['health'] = game.ran.randint(game.gameData.enemy_stat_ranges['enemy']
                                                                             ['stats']['low_health'],
                                                                             game.gameData.enemy_stat_ranges['enemy']
                                                                             ['stats']['max_health'])
    game.gameData.blank_enemy['enemy']['stats']['damage']['min_damage'] = \
        game.ran.randint(
            game.gameData.enemy_stat_ranges['enemy']['stats']['number_1_min_damage'],
            game.gameData.enemy_stat_ranges['enemy']['stats']['number_1_max_damage']
                         )
    game.gameData.blank_enemy['enemy']['stats']['damage']['max_damage'] = \
        game.ran.randint(
            game.gameData.enemy_stat_ranges['enemy']['stats']['number_2_min_damage'],
            game.gameData.enemy_stat_ranges['enemy']['stats']['number_2_max_damage']
        )
    game.gameData.blank_enemy['enemy']['stats']['speed'] = \
        game.ran.randint(
            game.gameData.enemy_stat_ranges['enemy']['stats']['min_speed'],
            game.gameData.enemy_stat_ranges['enemy']['stats']['max_speed']
        )
    game.gameData.blank_enemy['enemy']['level']['exp'] = \
        game.ran.randint(
            game.gameData.enemy_stat_ranges['enemy']['stats']['min_exp'],
            game.gameData.enemy_stat_ranges['enemy']['stats']['max_exp']
        )
    game.gameData.blank_enemy['enemy']['drops']['gold'] = \
        game.ran.randint(
            game.gameData.enemy_stat_ranges['enemy']['stats']['min_gold'],
            game.gameData.enemy_stat_ranges['enemy']['stats']['max_gold']
        )
    game.gameData.blank_enemy['enemy']['name'] = game.ran.choice(game.gameData.enemy_names)
    game.gameData.enemy = game.gameData.blank_enemy['enemy']


if __name__ == '__main__':
    exit('Please run main.py')
