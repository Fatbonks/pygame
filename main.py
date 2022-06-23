import random as ran
import time


class GameLogic:
    # Declare all global variables 
    def __init__(self):
        self.player = {
            'name': 'john',
            'class': '',
            'race': 'Human',
            'stats': {'max_health': 13.0, 'health': 13.0, 'mana': 5.0, 'damage': {'min_damage': 1.0, 'max_damage': 5.0},
                      'speed': 1.0, 'dodge': 25},
            'level': {'level': 1, 'level_next': 25, 'exp': 0},
            'bag': {'gold': 50},
            'magic_slots': {'slot_1', 'slot_2', 'slot_3', 'slot_4'}
        }

        self.enemy = {

        }

        self.enemies = {
            'troll': {
                'name': 'troll',
                'race': 'big green boi',
                'stats': {'health': 13.0, 'damage': {'min_damage': 1.0, 'max_damage': 5.0}, 'speed': 1},
                'level': {'level': 0, 'exp': 15}, 'drops': {'gold': 4}
            },

            'skeleton': {
                'name': 'skeleton',
                'race': 'leo',
                'stats': {'health': 13.0, 'damage': {'min_damage': 1.0, 'max_damage': 5.0}, 'speed': 1},
                'level': {'level': 0, 'exp': 10}, 'drops': {'gold': 1}
            },

            'orc': {
                'name': 'orc',
                'race': 'fat green boi',
                'stats': {'health': 13.0, 'damage': {'min_damage': 1.0, 'max_damage': 5.0}, 'speed': 1},
                'level': {'level': 0, 'exp': 13}, 'drops': {'gold': 3}
            },

            'elf': {
                'name': 'elf',
                'race': 'ear',
                'stats': {'health': 13.0, 'damage': {'min_damage': 1.0, 'max_damage': 5.0}, 'speed': 2},
                'level': {'level': 0, 'exp': 8}, 'drops': {'gold': 10}
            }
        }

        self.magic = {
            'fire': {'small_fireball': {'mana_cost': 1.5, 'damage': {'min_damage': 3.0, 'max_damage': 7.0}}},
            'water': {},
            'air': {},
            'earth': {}
        }

    # The character selection process at the start of the game
    def player_class(self):
        print("Pick your class\n1: warrior\n2: mage\n3: archer\n4: thief")
        while True:
            try:
                act = int(input("> ").lower().strip())
                if act == 1:
                    self.player['class'] = 'warrior'
                    break
                elif act == 2:
                    self.player['class'] = 'mage'
                    self.player['stats']['health'] = 5.0
                    self.player['stats']['mana'] = 13.0
                    self.player['stats']['speed'] = 2.0
                    break
                elif act == 3:
                    self.player['class'] = 'archer'
                    self.player['stats']['health'] = 10.0
                    self.player['stats']['mana'] = 5.0
                    self.player['stats']['speed'] = 4.0
                    break
                elif act == 4:
                    self.player['class'] = 'thief'
                    self.player['stats']['health'] = 8.0
                    self.player['stats']['mana'] = 5.0
                    self.player['stats']['speed'] = 3.0
                    self.player['stats']['dodge'] = 95
                    break
                print("Please input a valid number!")
            except ValueError:
                print("Please input a valid number!")

        # Welcome text
        print("------------")
        print("Welcome to {RPGName}")
        if input("What would you like to name yourself?\n> ") != "":
            print("Stupid! a baby can't name itself!")
        print("You're name is now {}".format(self.player['name']))

    # Levels up the player
    def level_up(self):
        l_health, l_damage = 0.0, 0.0
        while self.player['level']['exp'] >= self.player['level']['level_next']:
            self.player['level']['level'] += 1
            self.player['level']['exp'] = self.player['level']['exp'] - self.player['level']['level_next']
            self.player['level']['level_next'] = round(self.player['level']['level_next'] * 1.2)
            l_health += 0.5
            l_damage += 0.5
            print("----------------------")
            print("Level: {}".format(self.player['level']['level']))
            print("EXP: {}".format(self.player['level']['exp']))
            print("Next Level: {}".format(self.player['level']['level_next']))
            hold_health = self.player['stats']['health']
            hold_min_damage = self.player['stats']['damage']['min_damage']
            hold_max_damage = self.player['stats']['damage']['max_damage']
            self.player['stats']['max_health'] += l_health
            self.player['stats']['damage']['min_damage'] += l_damage
            self.player['stats']['damage']['max_damage'] += l_damage
            print("-------------------")
            print("{} max health --> {}  max health".format(self.player['stats']['max_health'] - l_health,
                                                            self.player['stats']['max_health']))
            print(
                "{} min damage, {} max damage --> {} min damage, {} max damage"
                .format(hold_min_damage, hold_max_damage, self.player['stats']['damage']['min_damage'],
                        self.player['stats']['damage']['max_damage']))

    # Enemy takes damage from the player
    def do_damage(self):
        dmg = ran.randint(int(self.player['stats']['damage']['min_damage']),
                          int(self.player['stats']['damage']['max_damage']))
        self.enemy['stats']['health'] -= dmg

        if self.player['stats']['health'] <= 0:
            self.enemy['stats']['health'] += dmg
        elif self.enemy['stats']['health'] <= 0:
            print("------------------")
            print("{} has been slain by {}".format(self.enemy['name'], self.player['name']))
            print("{} has {} health left".format(self.player['name'], self.player['stats']['health']))
            self.player['bag']['gold'] += self.enemy['drops']['gold']
            self.player['level']['exp'] += self.enemy['level']['exp']
            print('you gained {} gold!'.format(self.enemy['drops']['gold']))
        else:
            print("------------------")
            print("{} takes {} damage".format(self.enemy['name'], dmg))
            print("{} health is {}\nThe {} health is {}".format(self.player['name'], self.player['stats']['health'],
                                                                self.enemy['name'], self.enemy['stats']['health']))

    # Player takes damage from the enemy
    def take_damage(self):
        dmg = ran.randint(int(self.enemy['stats']['damage']['min_damage']),
                          int(self.enemy['stats']['damage']['max_damage']))
        self.player['stats']['health'] -= dmg
        if self.enemy['stats']['health'] <= 0:
            self.player['stats']['health'] += dmg
        elif self.player['stats']['health'] <= 0:
            print("{} has been slain by {}".format(self.player['name'], self.enemy['name']))
            input('press any key to leave')
            exit(0)
        else:
            print("------------------")
            print("{} takes {} damage".format(self.player['name'], dmg))
            print("{} health is {}\nThe {} health is {}".format(self.player['name'], self.player['stats']['health'],
                                                                self.enemy['name'], self.enemy['stats']['health']))

    def random_enemy(self):
        self.enemy = self.enemies[ran.choice(list(self.enemies))]

    def event_picker(self):
        if ran.random() < 0.1:
            pass
        if ran.random() < 0.2:
            pass


if __name__ == '__main__':
    game = GameLogic()

    # Runs at the start of the game
    game.player_class()
    # Main game loop
    while True:
        option = ['up', 'left', 'right', 'stats', 'exit']
        print('----------------------------')
        print("Up: Move up\nStats: Shows your stats\nExit: To leave the game")
        answer = input("> ").lower().strip()
        if answer in option:
            # up is debug command to trigger combat
            if answer == 'up':
                # Roll a 100% chance to get into a fight
                if ran.random() < 1:
                    game.random_enemy()
                    while game.enemy['stats']['health'] > 0 < game.enemy['stats']['health']:
                        if game.player['stats']['speed'] >= game.enemy['stats']['speed']:
                            game.do_damage()
                            if game.player['stats']['dodge'] / 100 > ran.random():
                                print("{} dodged the enemies attack".format(game.player['name']))
                            else:
                                game.take_damage()
                        else:
                            if game.player['stats']['dodge'] / 100 > ran.random():
                                print("{} dodged the enemies attack".format(game.player['name']))
                            else:
                                game.take_damage()
                            game.do_damage()
                        time.sleep(2.5)
                    game.level_up()
            elif answer == 'stats':
                print("----------------------------")
                print(
                    "Level: {}\nMax health: {}\nHealth: {}\nMana: {}\nDamage: {} Min damage {} Max damage\nEXP: {}\n"
                    "Speed: {}\nDodge: {}\nLevel next: {}\n".format(
                        game.player['level']['level'],
                        game.player['stats']['max_health'],
                        game.player['stats']['health'],
                        game.player['stats']['mana'],
                        game.player['stats']['damage']['min_damage'],
                        game.player['stats']['damage']['max_damage'],
                        game.player['level']['exp'],
                        game.player['stats']['speed'],
                        game.player['stats']['dodge'],
                        game.player['level']['level_next']
                    ))
                time.sleep(5)
            elif answer == 'exit':
                exit(0)
        else:
            print('please use an word to select your choices')
