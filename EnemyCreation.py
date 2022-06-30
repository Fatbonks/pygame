import Pipe as game

enemy_names = [
    'jeff the angry miller', 'joe the angry butcher', 'bobenstein', 'hobgoblin', 'lost Leo', 'Cody, the elf',
    'dog', 'slime, the god destroyer', 'old man ', 'smith, the smithing smither', 'smeckle man',
    'bob the horse', 'Milf destroyer 3000'
               ]
min_health = 5
max_health = 13
number_1_min_damage = 1
number_1_max_damage = 2
number_2_max_damage = 5
number_2_min_damage = 3
min_speed = 1
max_speed = 4
min_exp = 4
max_exp = 13
min_gold = 2
max_gold = 14
# 'stats': {'health': 0.0, 'damage': {'min_damage': 0.0, 'max_damage': 0.0}, 'speed': 0},

# 'level': {'level': 0, 'exp': 0}, 'drops': {'gold': 0}


def random_enemy():
    health = game.ran.randint(min_health, max_health)
    p_min_damage = game.ran.randint(number_1_min_damage, number_1_max_damage)
    p_max_damage = game.ran.randint(number_2_min_damage, number_2_max_damage)
    speed = game.ran.randint(min_speed, max_speed)
    exp = game.ran.randint(min_exp, max_exp)
    gold = game.ran.randint(min_gold, max_gold)
    game.gameData.enemies['enemy']['name'] = game.ran.choice(enemy_names)
    game.gameData.enemies['enemy']['stats']['health'] = health
    game.gameData.enemies['enemy']['stats']['damage']['min_damage'] = p_min_damage
    game.gameData.enemies['enemy']['stats']['damage']['max_damage'] = p_max_damage
    game.gameData.enemies['enemy']['stats']['speed'] = speed
    game.gameData.enemies['enemy']['level']['exp'] = exp
    game.gameData.enemies['enemy']['drops']['gold'] = gold
    game.gameData.enemy = game.gameData.enemies['enemy']


if __name__ == '__main__':
    exit('Please run main.py')
