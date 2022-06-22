class GameLogic:
    # Declare all global variables 
    def __init__(self):
        self.name = ''
        self.player = {'class': {'warrior': {'stats': {'health': 13.0, 'mana': 5.0,
                                                       'damage': {'min_damage': 1.0, 'max_damage': 5.0},
                                                       'speed': 1, 'dodge': 0},
                                             'level': {'level': 1, 'level_next': 25, 'exp': 0}},
                                 'mage': {'stats': {'health': 5.0, 'mana': 5.0,
                                                    'damage': {'min_damage': 1, 'max_damage': 3},
                                                    'speed': 2, 'dodge': 0},
                                          'level': {'level': 1, 'level_next': 25, 'exp': 0}},
                                 'archer': {'stats': {'health': 13.0, 'mana': 5.0,
                                                      'damage': {'min_damage': 1.0, 'max_damage': 5.0},
                                                      'speed': 4, 'dodge': 0},
                                            'level': {'level': 1, 'level_next': 25, 'exp': 0}},
                                 'thief': {'stats': {'health': 13.0, 'mana': 5.0,
                                                     'damage': {'min_damage': 1.0, 'max_damage': 5.0},
                                                     'speed': 3, 'dodge': 25},
                                           'level': {'level': 1, 'level_next': 25, 'exp': 0}}}}

    def add_one(self):
        print(self.player['class']['warrior'])


if __name__ == '__main__':
    game = GameLogic()
    game.add_one()
    # Main game loop
    while True:
        pass


