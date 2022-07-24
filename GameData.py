
class GameData:
    # Declare all global variables
    def __init__(self):
        # Dictionary for the player
        self.player = {
            'name': '',
            'class': '',
            'race': 'Human',
            'stats': {'max_health': 20, 'health': 20, 'max_mana': 5, 'mana': 5,
                      'damage': {'min_damage': 1, 'max_damage': 6},
                      'speed': 1, 'dodge': 10, 'stamina': 100, 'max_stamina': 100},
            'level': {'level': 1, 'level_next': 25, 'exp': 0},
            'bag': {'gold': 50, 'health_potion': 0, 'Drugs': 0},
            'magic_slots':
                {
                    'slot_1': {'name': '', 'mana_cost': 0, 'damage': {'min_damage': 0, 'max_damage': 0},
                               'proficiency': 0, 'proficiency_level_up': 25, 'spell_used': False
                               },
                    'slot_2': {'name': '', 'mana_cost': 0, 'damage': {'min_damage': 0, 'max_damage': 0},
                               'proficiency': 0, 'proficiency_level_up': 25, 'spell_used': False
                               },
                    'slot_3': {'name': '', 'mana_cost': 0, 'damage': {'min_damage': 0, 'max_damage': 0},
                               'proficiency': 0, 'proficiency_level_up': 25, 'spell_used': False
                               },
                    'slot_4': {'name': '', 'mana_cost': 0, 'damage': {'min_damage': 0, 'max_damage': 0},
                               'proficiency': 0, 'proficiency_level_up': 25, 'spell_used': False
                               }

                }
        }

        self.player_skills = {
            'physical_skills':
                {
                    'slot_1': {'name': '', 'stamina_cost': 0, 'damage': {'bonus_damage': 0},
                               'proficiency': 0, 'proficiency_level_up': 25, 'skill_used': False, 'accuracy': 0
                               },
                    'slot_2': {'name': '', 'stamina_cost': 0, 'damage': {'bonus_damage': 0},
                               'proficiency': 0, 'proficiency_level_up': 25, 'skill_used': False, 'accuracy': 0
                               },
                    'slot_3': {'name': '', 'stamina_cost': 0, 'damage': {'bonus_damage': 0},
                               'proficiency': 0, 'proficiency_level_up': 25, 'skill_used': False, 'accuracy': 0
                               },
                    'slot_4': {'name': '', 'stamina_cost': 0, 'damage': {'bonus_damage': 0},
                               'proficiency': 0, 'proficiency_level_up': 25, 'skill_used': False, 'accuracy': 0
                               }
                }}

        self.physical_skills = {
            'Big Swing': {'name': 'Big Swing', 'stamina_cost': 0, 'damage': {'bonus_damage': 0},
                          'proficiency': 0, 'proficiency_level_up': 25, 'skill_used': False, 'accuracy': 1
                          },
            'staff bash': {'name': 'Big Swing', 'stamina_cost': 0, 'damage': {'bonus_damage': 0},
                           'proficiency': 0, 'proficiency_level_up': 25, 'skill_used': False, 'accuracy': 1
                           },
            'spin attack': {'name': 'Spin attack', 'stamina_cost': 30, 'damage': {'bonus_damage': 4},
                            'proficiency': 0, 'proficiency_level_up': 25, 'skill_used': False, 'accuracy': 0.7
                            },
            'Sword swipe': {'name': 'Sword swipe', 'stamina_cost': 5, 'damage': {'bonus_damage': 1},
                            'proficiency': 0, 'proficiency_level_up': 25, 'skill_used': False, 'accuracy': 0.8
                            },
            'Stab': {'name': 'Stab', 'stamina_cost': 10, 'damage': {'bonus_damage': 2},
                     'proficiency': 0, 'proficiency_level_up': 25, 'skill_used': False, 'accuracy': 0.7
                     },
        }

        # Dictionary for the enemy the player is currently fighting
        self.enemy = {

        }

        # Dictionary for the enemies of the player
        self.blank_enemy = {
            'enemy': {
                'name': '',
                'title': '',
                'stats': {'health': 0.0, 'damage': {'min_damage': 0.0, 'max_damage': 0.0}, 'speed': 0},
                'level': {'level': 0, 'exp': 0}, 'drops': {'gold': 0}
            }
        }

        self.enemy_name = [
            'jeff', 'joe', 'bobenstein', 'hobgoblin', 'Leo', 'Cody, the elf',
            'dog', 'slime, the god destroyer', 'old man', 'smith', 'smeckle man',
            'bob, the undead horse', 'Milf destroyer 3000'
        ]
        self.enemy_names = {
            'jeff': {'name': 'jeff', 'title': 'the angry miller'},
            'joe': {'name': 'joe', 'title': 'the angry butcher'},
            'Leo': {'name': 'Leo', 'title': 'the lost adventurer'},
            'smith': {'name': 'Leo', 'title': 'the lost adventurer'}
        }

        self.enemy_stat_ranges = {
            'enemy': {
                'stats': {
                    'low_health': 5, 'max_health': 13, 'number_1_min_damage': 1, 'number_1_max_damage': 2,
                    'number_2_min_damage': 3, 'number_2_max_damage': 5, 'min_speed': 1, 'max_speed': 4, 'min_exp': 3,
                    'max_exp': 13, 'min_gold': 2, 'max_gold': 14
                }
            }
        }
        # world level so every thing won't be under power once the player starts to level up
        self.world = {
            'world_level': 5
        }
        # Dictionary of available spells for the player to learn
        self.magic = {
            'fire': {
                'fireball':
                    {'name': 'fireball', 'mana_cost': 3, 'damage': {'min_damage': 0, 'max_damage': 20},
                     'proficiency': 0, 'proficiency_level_up': 25, 'spell_used': False

                     }
            },
            'water': {
                'water_whip': {
                    'name': 'water whip', 'mana_cost': 3, 'damage': {'min_damage': 0, 'max_damage': 20},
                    'proficiency': 0, 'proficiency_level_up': 25, 'spell_used': False
                }
            },
            'air': {
                'air_blades': {
                    'name': 'air blades', 'mana_cost': 3, 'damage': {'min_damage': 0, 'max_damage': 20},
                    'proficiency': 0, 'proficiency_level_up': 25, 'spell_used': False
                }
            },
            'earth': {
                'earthquake': {
                    'name': 'earthquake', 'mana_cost': 3, 'damage': {'min_damage': 0, 'max_damage': 20},
                    'proficiency': 0, 'proficiency_level_up': 25, 'spell_used': False
                }
            }
        }

        # Array of possible player names
        # We will keep adding names as the game becomes more developed
        self.quest = {
            'description': '', 'Reward': 0
        }
        self.map = ''
        self.dungeon_map = []
        self.world_map = [['m', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm'],
                          ['m', 'd', 'V', 'P', 'F', 'F', 'm', 'm', 'm', 'D', 'F', 'F', 'm'],
                          ['m', 'm', 'm', 'P', 'F', 'F', 'm', 'd', 'm', 'm', 'm', 'F', 'm'],
                          ['m', 'm', 'm', 'P', 'P', 'P', 'V', 'P', 'P', 'P', 'P', 'F', 'm'],
                          ['m', 'm', 'm', 'm', 'm', 'F', 'm', 'F', 'F', 'm', 'P', 'F', 'm'],
                          ['m', 'm', 'm', 'm', 'm', 'F', 'F', 'F', 'F', 'm', 'P', 'F', 'm'],
                          ['m', 'm', 'm', 'D', 'F', 'F', 'T', 'F', 'F', 'F', 'V', 'F', 'm'],
                          ['m', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm']]
        self.dungeon_enemies = 0
        self.biome = {
            '#': {
                'biome': 'Wall', 'enemy_can_spawn': False, 'is_wall': True, 'can_explore': False, 'Intractable': False,
                'description': 'bruh how you should even be able to get here'
            },
            '█': {
                'biome': 'Starting room', 'enemy_can_spawn': False, 'is_wall': False, 'can_explore': False, 'Intractable': True,
                'description': "To exit and enter into the dungeon"
            },
            'H': {
                'biome': 'Hallway', 'enemy_can_spawn': True, 'is_wall': False, 'can_explore': False, 'Intractable': False,
                'description': 'A hallway ... could lead to a room or Death.'
            },
            '?': {
                'biome': 'Unexplored Room', 'enemy_can_spawn': False, 'is_wall': False, 'can_explore': False, 'Intractable': True,
                'description': 'An unexplored room could have valuable stuff or Death.'
            },
            'E': {
                'biome': 'Explored Room', 'enemy_can_spawn': True, 'is_wall': False, 'can_explore': True, 'Intractable': False,
                'description': 'An explored room everything good is gone. .....'
            },
            'T': {
                'biome': 'Treasure Room', 'enemy_can_spawn': False, 'is_wall': False, 'can_explore': True, 'Intractable': True,
                'description': 'Has one chest, should you open it. May has goods or danger'
            },
            'M': {
                'biome': 'Merchant', 'enemy_can_spawn': False, 'is_wall': False, 'can_explore': True, 'Intractable': True,
                'description': 'A merchant where you can buy potions'
            },
            'D': {
                'biome': 'Dead adventurer', 'enemy_can_spawn': False, 'is_wall': False, 'can_explore': True, 'Intractable': True,
                'description': 'A dead adventurer. Could have good loot....'
            },
            '@': {
                'biome': 'Breakable door', 'enemy_can_spawn': False, 'is_wall': False, 'can_explore': False, 'Intractable': True,
                'description': 'its possible to break.....'
            },
            'm': {
                'biome': 'Mountain', 'enemy_can_spawn': False, 'is_wall': True, 'can_explore': False, 'Intractable': False,
                'description': 'mount'
            },
            'P': {
                'biome': 'Pathway', 'enemy_can_spawn': True, 'is_wall': False, 'can_explore': False, 'Intractable': False,
                'description': 'Pathway that lead to Towns'
            },
            'F': {
                'biome': 'Forest', 'enemy_can_spawn': True, 'is_wall': False, 'can_explore': False, 'Intractable': False,
                'description': 'A Forest'
            },
            'V': {
                'biome': 'Village', 'enemy_can_spawn': False, 'is_wall': False, 'can_explore': False, 'Intractable': True,
                'description': 'A village, Used to buy equipment'
            },
            'd': {
                'biome': 'Dungeon Selector', 'enemy_can_spawn': False, 'is_wall': False, 'can_explore': False, 'Intractable': True,
                'description': 'To select what dungeon to play'
            },

        }

        self.room = []
        self.player_x_dungeon = 1
        self.player_y_dungeon = 1
        self.player_x_world = 2
        self.player_y_world = 1

        self.names = ['Bill', 'John', 'Dave', 'Cow', 'Tiffany', 'Tod', 'Elliot', 'Mexican jesus', 'cody']

        self.has_healed = False
        self.has_loaded = False


if __name__ == '__main__':
    exit('Please run main.py')
