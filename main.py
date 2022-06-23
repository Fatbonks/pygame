import random as ran


class GameLogic:
    # Declare all global variables 
    def __init__(self):
        self.player = {
            'name': '',
            'class': '',
            'race': 'Human',
            'stats': {'health': 13.0, 'mana': 5.0, 'damage': {'min_damage': 1.0, 'max_damage': 5.0},
                      'speed': 1.0, 'dodge': 0.0},
            'level': {'level': 1, 'level_next': 25, 'exp': 0}
        }

        self.enemy = {

        }

        self.enemies = {
            'troll': {
                'name': 'troll',
                'race': 'big green boi',
                'stats': {'health': 13.0, 'damage': {'min_damage': 1.0, 'max_damage': 5.0}},
                'level': {'level': 0, 'exp': 15}, 'drops': {'gold': 5}
            },

            'skeleton': {
                'name': 'skeleton',
                'race': 'leo',
                'stats': {'health': 13.0, 'damage': {'min_damage': 1.0, 'max_damage': 5.0}},
                'level': {'level': 0, 'exp': 15}, 'drops': {'gold': 5}
            },

            'orc': {
                'name': 'orc',
                'race': 'fat green boi',
                'stats': {'health': 13.0, 'damage': {'min_damage': 1.0, 'max_damage': 5.0}},
                'level': {'level': 0, 'exp': 15}, 'drops': {'gold': 5}
            },

            'elf': {
                'name': 'elf',
                'race': 'ear',
                'stats': {'health': 13.0, 'damage': {'min_damage': 1.0, 'max_damage': 5.0}},
                'level': {'level': 0, 'exp': 15}, 'drops': {'gold': 5}
            }
        }

    # The character selection process at the start of the game
    def player_class(self):
        print("Pick your class\n1: warrior\n2: mage\n3: archer\n4: thief")
        try:
            act = int(input("> ").lower().strip())
            if act == 1:
                self.player['class'] = 'warrior'
            elif act == 2:
                self.player['class'] = 'mage'
                self.player['stats']['health'] = 5.0
                self.player['stats']['mana'] = 13.0
                self.player['stats']['speed'] = 2.0
            elif act == 3:
                self.player['class'] = 'archer'
                self.player['stats']['health'] = 10.0
                self.player['stats']['mana'] = 5.0
                self.player['stats']['speed'] = 4.0
            elif act == 4:
                self.player['class'] = 'thief'
                self.player['stats']['health'] = 8.0
                self.player['stats']['mana'] = 5.0
                self.player['stats']['speed'] = 3.0
                self.player['stats']['dodge'] = 100
        except ValueError:
            print("Please input a valid number!")

    # Combat between the player and the chosen enemy they are fighting.
    def take_damage(self):
        dmg = ran.randint(int(self.player['stats']['damage']['min_damage']),
                          int(self.player['stats']['damage']['max_damage']))
        self.enemy['stats']['health'] -= dmg
        if self.enemy['stats']['health'] <= 0:
            print("------------------")
            print("{} has been slain by {}".format(self.enemy['name'], self.player['name']))
            print("{} has {} health left".format(self.player['name'], self.player['stats']['health']))
            self.player['level']['exp'] += self.enemy['level']['exp']

        elif self.player['stats']['health'] <= 0:
            print('you have died')
            input('press any key to leave')
            exit(0)

        else:
            print("------------------")
            print("{} takes {} damage".format(self.enemy['name'], dmg))
            print("{} health is {}\nThe {} health is {}".format(self.player['name'], self.player['stats']['health'],
                                                                self.enemy['name'], self.enemy['stats']['health']))

    def level_up(self):
        print("----------------------")
        print("Level: {}".format(player.level))
        print("EXP: {}".format(player.exp))
        print("Next Level: {}".format(player.level_next))
        print("----------------------")
        l_health, l_damage = 0.0, 0.0
        while player.exp >= player.level_next:
            player.level += 1
            player.exp = player.exp - player.level_next
            player.level_next = round(player.level_next * 1.2)
            l_health += 0.5
            l_damage += 0.5
            print("----------------------")
            print("Level: {}".format(player.level))
            print("EXP: {}".format(player.exp))
            print("Next Level: {}".format(player.level_next))
            hold_health = player.health
            hold_min_damage = player.damage['min_damage']
            hold_max_damage = player.damage['max_damage']
            player.health += l_health
            player.damage['min_damage'] += l_damage
            player.damage['max_damage'] += l_damage
            print("-------------------")
            print("{} health --> {} health".format(hold_health, player.health))
            print(
                "{} min damage, {} max damage --> {} min damage, {} max damage".format(hold_min_damage, hold_max_damage,
                                                                                       player.damage['min_damage'],
                                                                                       player.damage['min_damage']))


if __name__ == '__main__':
    game = GameLogic()

    # Runs at the start of the game
    game.player_class()

    # Main game loop
    while True:
        pass
