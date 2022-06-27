import time

import Pipe as game


def level_up():
    l_health, l_damage = 0.0, 0.0
    while game.gameData.player['level']['exp'] >= game.gameData.player['level']['level_next']:
        game.gameData.player['level']['level'] += 1
        game.gameData.player['level']['exp'] = game.gameData.player['level']['exp'] - \
                                               game.gameData.playerr['level']['level_next']
        game.gameData.player['level']['level_next'] = round(game.gameData.player['level']['level_next'] * 1.2)
        l_health += 1
        l_damage += 1
        print("----------------------")
        print("Level: {}".format(game.gameData.player['level']['level']))
        print("EXP: {}".format(game.gameData.player['level']['exp']))
        print("Next Level: {}".format(game.gameData.player['level']['level_next']))
        time.sleep(2.5)
        hold_health = game.gameData.player['stats']['health']
        hold_min_damage = game.gameData.player['stats']['damage']['min_damage']
        hold_max_damage = game.gameData.player['stats']['damage']['max_damage']
        game.gameData.player['stats']['max_health'] += l_health
        game.gameData.player['stats']['damage']['min_damage'] += l_damage
        game.gameData.player['stats']['damage']['max_damage'] += l_damage
        print("-------------------")
        print("{} max health --> {}  max health".format(game.gameData.player['stats']['max_health'] - l_health,
                                                        game.gameData.player['stats']['max_health']))
        print(
            "{} min damage, {} max damage --> {} min damage, {} max damage"
            .format(hold_min_damage, hold_max_damage, game.gameData.player['stats']['damage']['min_damage'],
                    game.gameData.player['stats']['damage']['max_damage']))


if __name__ == '__main__':
    exit('Please run main.py')
