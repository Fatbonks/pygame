import Pipe as game


def gods_healing():
    if game.gameData.player['bag']['gold'] >= 10:
        print("You use 10 smeckles to call god to give you drugs!")
        gold = 10
        game.gameData.player['bag']['gold'] -= gold
        rand = game.ran.random()
        if rand < 0.5:
            game.gameData.has_healed = True
            game.gameData.player['stats']['health'] += round(game.gameData.player['stats']['max_health'] / 2)
            print(
                "God responds and heals you for {} HP".format(round(game.gameData.player['stats']['max_health'] / 2))
            )
            if game.gameData.player['stats']['health'] > game.gameData.player['stats']['max_health']:
                game.gameData.player['stats']['health'] = game.gameData.player['stats']['max_health']
        elif rand > 0.5:
            print("God does not respond you lose {} smeckles".format(gold))
    else:
        print('You dont have enough smeckles to buy gods grace')


def drugs_healing():
    if game.gameData.player['bag']['Drugs'] > 0:
        game.gameData.player['bag']['Drugs'] -= 1
        health = game.gameData.player['stats']['max_health'] // 2
        game.gameData.player['stats']['health'] += health
        if game.gameData.player['stats']['health'] > game.gameData.player['stats']['max_health']:
            game.gameData.player['stats']['health'] = game.gameData.player['stats']['max_health']
        print('You have healed, You have {} drugs left'.format(game.gameData.player['bag']['Drugs']))
    else:
        print('you dont have any Drugs!')
        input('press enter to leave')


if __name__ == '__main__':
    exit('Please run main.py')
