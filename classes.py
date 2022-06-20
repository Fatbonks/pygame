# map #
class ZoneMap:
    def __init__(self):
        self.wall_left = False
        self.wall_right = False


# enemy_class #
class Enemy:
    def __init__(self, name, health, damage, exp, speed, dodge, level,):
        self.name = name
        self.health = health
        self.damage = damage
        self.exp = exp
        self.speed = speed
        self.dodge = dodge
        self.level = level


# player_class #
class Player:
    def __init__(self, name, health, mana, damage, exp, speed, dodge, level, level_next, class_type):
        self.name = name
        self.health = health
        self.mana = mana
        self.damage = damage
        self.exp = exp
        self.speed = speed
        self.dodge = dodge
        self.level = level
        self.level_next = level_next
        self.class_type = class_type
