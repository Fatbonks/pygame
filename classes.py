# map #
class ZoneMap:
    def __int__(self):
        self.wall_left = False
        self.wall_right = False


# enemy_class #
class Enemy:
    def __int__(self):
        self.health = 0.0
        self.damage = 0.0
        self.name = ''
        self.exp = 0
        self.speed = 0
        self.level = 0


# player_class #
class Player:
    def __int__(self):
        self.name = ''
        self.hp = 0.0
        self.mana = 0.0
        self.damage = 0.0
        self.effects = []
        self.exp = 0.0
        self.speed = 0.0
        self.dodge = 0.0
        self.level = 0


class ArmorHead:
    armor_head_level = 0
    increase_hp = 0.0
    increase_mana = 0.0
    increase_speed = 0.0
    increase_dodge = 0.0


class ArmorChest:
    armor_chest_level = 0
    increase_hp = 0.0
    increase_mana = 0.0
    increase_speed = 0.0
    increase_dodge = 0.0


class ArmorLegging:
    armor_legging_level = 0
    increase_hp = 0.0
    increase_mana = 0.0
    increase_speed = 0.0
    increase_dodge = 0.0


class ArmorBoots:
    armor_boots_level = 0
    increase_hp = 0.0
    increase_mana = 0.0
    increase_speed = 0.0
    increase_dodge = 0.0


# declaring class's into vars #
enemy = Enemy()
zone_map = ZoneMap()
my_player = Player()
