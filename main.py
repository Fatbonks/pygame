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
                      'speed': 1.0, 'dodge': 10},
            'level': {'level': 1, 'level_next': 25, 'exp': 0},
            'bag': {'gold': 50},
            'magic_slots':
                {
                    'slot_1': {'name': 'slot_1', 'mana_cost': 0.0, 'damage': {'min_damage': 0.0, 'max_damage': 0.0},
                               'proficiency': 0.0, 'proficiency_level_up': 25.0
                               },
                    'slot_2': {'name': 'slot_2', 'mana_cost': 0.0, 'damage': {'min_damage': 0.0, 'max_damage': 0.0},
                               'proficiency': 0.0, 'proficiency_level_up': 25.0
                               },
                    'slot_3': {'name': 'slot_3', 'mana_cost': 0.0, 'damage': {'min_damage': 0.0, 'max_damage': 0.0},
                               'proficiency': 0.0, 'proficiency_level_up': 25.0
                               },
                    'slot_4': {'name': 'slot_4', 'mana_cost': 0.0, 'damage': {'min_damage': 0.0, 'max_damage': 0.0},
                               'proficiency': 0.0, 'proficiency_level_up': 25.0
                               }
                }
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
            'fire': {
                'fireball':
                    {'name': 'fireball', 'mana_cost': 3.5, 'damage': {'min_damage': 0.0, 'max_damage': 20.0},
                     'proficiency': 0.0, 'proficiency_level_up': 25.0

                     }
            },
            'water': {
                'water_whip': {
                    'name': 'water whip', 'mana_cost': 3.5, 'damage': {'min_damage': 0.0, 'max_damage': 20.0},
                    'proficiency': 0.0, 'proficiency_level_up': 25.0
                }
            },
            'air': {
                'air_blades': {
                    'name': 'air blades', 'mana_cost': 3.5, 'damage': {'min_damage': 0.0, 'max_damage': 20.0},
                    'proficiency': 0.0, 'proficiency_level_up': 25.0
                }
            },
            'earth': {
                'earthquake': {
                    'name': 'earthquake', 'mana_cost': 3.5, 'damage': {'min_damage': 0.0, 'max_damage': 20.0},
                    'proficiency': 0.0, 'proficiency_level_up': 25.0
                }
            }
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
                    print('what ability would you like?\n1: Fireball\n2: Water whip\n3: Air blades\n4: earthquake')
                    ans = int(input('> ').lower().strip())
                    if ans == 1:
                        magic = self.magic['fire']['fireball']
                    if ans == 2:
                        magic = self.magic['water']['water_whip']
                    if ans == 3:
                        magic = self.magic['air']['air_blades']
                    if ans == 4:
                        magic = self.magic['earth']['earthquake']
                    print('what slot would you like to assign it to\n1: slot 1\n2: slot 2\n3: slot 3\n4: slot 4')
                    ans2 = int(input('> ').lower().strip())
                    self.magic_slot_adder(magic, ans2)
                    print(game.player['magic_slots']['slot_1'])
                    print(game.player['magic_slots']['slot_2'])
                    print(game.player['magic_slots']['slot_3'])
                    print(game.player['magic_slots']['slot_4'])
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

    def do_magical_damage(self, ans):
        if ans == 1:
            dmg = ran.randint(int(self.player['magic_slots']['slot_1']['damage']['min_damage']),
                              int(self.player['magic_slots']['slot_1']['damage']['max_damage']))
        elif ans == 2:
            dmg = ran.randint(int(self.player['magic_slots']['slot_2']['damage']['min_damage']),
                              int(self.player['magic_slots']['slot_2']['damage']['max_damage']))
        elif ans == 3:
            dmg = ran.randint(int(self.player['magic_slots']['slot_3']['damage']['min_damage']),
                              int(self.player['magic_slots']['slot_3']['damage']['max_damage']))
        elif ans == 4:
            dmg = ran.randint(int(self.player['magic_slots']['slot_4']['damage']['min_damage']),
                              int(self.player['magic_slots']['slot_4']['damage']['max_damage']))
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

    # picks an event to happen each time the player moves
    def event_picker(self):
        if ran.random() < 1:
            self.random_enemy()
            print("------------------")
            print("You have encountered an enemy, I hope you can win!")
            while self.enemy['stats']['health'] > 0 < self.enemy['stats']['health']:
                print("------------------")
                print("1: Attack\n2: Magic attack\n3: Run")
                try:
                    ans = int(input("> "))
                    if ans == 1:
                        while self.enemy['stats']['health'] > 0 < self.enemy['stats']['health']:
                            if self.player['stats']['speed'] >= self.enemy['stats']['speed']:
                                self.do_damage()
                                if self.player['stats']['dodge'] / 100 > ran.random():
                                    print("{} dodged the enemies attack".format(self.player['name']))
                                else:
                                    self.take_damage()
                            else:
                                if self.player['stats']['dodge'] / 100 > ran.random():
                                    print("{} dodged the enemies attack".format(self.player['name']))
                                else:
                                    self.take_damage()
                                self.do_damage()
                            time.sleep(2.5)
                        self.level_up()
                    if ans == 2:
                        print('your mana is {}'.format(self.player['stats']['mana']))
                        print('1: {}\n2: {}\n3: {}\n4: {}\n'.format(
                            self.player['magic_slots']['slot_1']['name'], self.player['magic_slots']['slot_2']['name'],
                            self.player['magic_slots']['slot_3']['name'], self.player['magic_slots']['slot_4']['name']
                        )
                        )
                        ans_magic_slot = int(input('> ').lower().strip())
                        if ans_magic_slot == 1 and self.player['magic_slots']['slot_1']['name'] != 'slot_1':
                            if self.player['stats']['mana'] >= self.player['magic_slots']['slot_1']['mana_cost']:
                                self.magic_attacking(ans_magic_slot)
                                self.player['stats']['mana'] -= self.player['magic_slots']['slot_1']['mana_cost']
                            else:
                                print(
                                    'you dont have enough mana you have {} mana left'.format(
                                        self.player['stats']['mana']
                                    )
                                )
                        elif ans_magic_slot == 2 and self.player['magic_slots']['slot_2']['name'] != 'slot_2':
                            if self.player['stats']['mana'] >= self.player['magic_slots']['slot_2']['mana_cost']:
                                self.magic_attacking(ans_magic_slot)
                                self.player['stats']['mana'] -= self.player['magic_slots']['slot_1']['mana_cost']
                            else:
                                print(
                                    'you dont have enough mana you have {} mana left'.format(
                                        self.player['stats']['mana']
                                    )
                                )
                        elif ans_magic_slot == 3 and self.player['magic_slots']['slot_3']['name'] != 'slot_3':
                            if self.player['stats']['mana'] >= self.player['magic_slots']['slot_3']['mana_cost']:
                                self.magic_attacking(ans_magic_slot)
                                self.player['stats']['mana'] -= self.player['magic_slots']['slot_3']['mana_cost']
                            else:
                                print(
                                    'you dont have enough mana you have {} mana left'.format(
                                        self.player['stats']['mana']
                                    )
                                )
                        elif ans_magic_slot == 4 and self.player['magic_slots']['slot_4']['name'] != 'slot_4':
                            if self.player['stats']['mana'] >= self.player['magic_slots']['slot_4']['mana_cost']:
                                self.magic_attacking(ans_magic_slot)
                                self.player['stats']['mana'] -= self.player['magic_slots']['slot_4']['mana_cost']
                            else:
                                print(
                                    'you dont have enough mana you have {} mana left'.format(
                                        self.player['stats']['mana']
                                    )
                                )
                        else:
                            print('That slot does not have an ability please use one that does have an a ability')
                except ValueError:
                    print('please use the number beside the thing you want to do!')

    def magic_attacking(self, ans):
        if self.player['stats']['speed'] >= self.enemy['stats']['speed']:
            self.do_magical_damage(ans)
            if self.player['stats']['dodge'] / 100 > ran.random():
                print("{} dodged the enemies attack".format(self.player['name']))
            else:
                self.take_damage()
        else:
            if self.player['stats']['dodge'] / 100 > ran.random():
                print("{} dodged the enemies attack".format(self.player['name']))
            else:
                self.take_damage()
            self.do_magical_damage(ans)
        time.sleep(2.5)
        self.level_up()

    def magic_slot_adder(self, magic, ans):
        if ans == 1:
            self.player['magic_slots']['slot_1'] = magic
        elif ans == 2:
            self.player['magic_slots']['slot_2'] = magic
        elif ans == 3:
            self.player['magic_slots']['slot_3'] = magic
        elif ans == 4:
            self.player['magic_slots']['slot_4'] = magic


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
                game.event_picker()
                old_mana = game.player['stats']['mana']
                game.player['stats']['mana'] = old_mana

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
            elif answer == 'exit':
                exit(0)
        else:
            print('please use an word to select your choices')
