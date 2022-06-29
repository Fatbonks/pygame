import Pipe as game


def healing_drugs():
    game.print_dialogue("You use 10 smeckles to call god to give you drugs!")
    gold = 10
    game.gameData.player['bag']['gold'] -= gold
    rand = game.ran.random()
    if rand < 0.5:
        game.gameData.has_healed = True
        game.gameData.player['stats']['health'] += round(game.gameData.player['stats']['max_health'] / 2)
        game.print_dialogue(
            "god responds and heals you for {} HP".format(round(game.gameData.player['stats']['max_health'] / 2))
        )
        if game.gameData.player['stats']['health'] > game.gameData.player['stats']['max_health']:
            game.gameData.player['stats']['health'] = game.gameData.player['stats']['max_health']
    elif rand > 0.5:
        game.print_dialogue("god does not respond you lose {} smeckles".format(gold))
