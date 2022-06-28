import Pipe as game


class GameData:
    # Declare all global variables
    def __init__(self):
        # Dictionary for the player
        self.player = {
            'name': '',
            'class': '',
            'race': 'Human',
            'stats': {'max_health': 20.0, 'health': 20.0, 'max_mana': 5.0, 'mana': 5.0,
                      'damage': {'min_damage': 1, 'max_damage': 6},
                      'speed': 1.0, 'dodge': 10},
            'level': {'level': 1, 'level_next': 25, 'exp': 0},
            'bag': {'gold': 50},
            'magic_slots':
                {
                    'slot_1': {'name': '', 'mana_cost': 0.0, 'damage': {'min_damage': 0.0, 'max_damage': 0.0},
                               'proficiency': 0.0, 'proficiency_level_up': 25.0
                               },
                    'slot_2': {'name': '', 'mana_cost': 0.0, 'damage': {'min_damage': 0.0, 'max_damage': 0.0},
                               'proficiency': 0.0, 'proficiency_level_up': 25.0
                               },
                    'slot_3': {'name': '', 'mana_cost': 0.0, 'damage': {'min_damage': 0.0, 'max_damage': 0.0},
                               'proficiency': 0.0, 'proficiency_level_up': 25.0
                               },
                    'slot_4': {'name': '', 'mana_cost': 0.0, 'damage': {'min_damage': 0.0, 'max_damage': 0.0},
                               'proficiency': 0.0, 'proficiency_level_up': 25.0
                               }
                }
        }

        # Dictionary for the enemy the player is currently fighting
        self.enemy = {

        }

        # Dictionary for the enemies of the player
        self.enemies = {
            'enemy': {
                'name': '',
                'stats': {'health': 0.0, 'damage': {'min_damage': 0.0, 'max_damage': 0.0}, 'speed': 0},
                'level': {'level': 0, 'exp': 0}, 'drops': {'gold': 0}
            }
        }

        # Dictionary of available spells for the player to learn
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

        # Array of possible player names
        # We will keep adding names as the game becomes more developed
        self.names = ['Bill', 'John', 'Dave', 'Cow', 'Tiffany', 'Tod', 'Elliot', 'Mexican jesus', 'cody']


if __name__ == '__main__':
    exit('Please run main.py')
