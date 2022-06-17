import random
import sys
import time


# map #
class ZoneMap:
    def __int__(self):
        self.left = False
        self.right = False
        self.down = True


# enemy_class #
class Enemy:
    def __int__(self):
        self.health = 0
        self.damage = 0
        self.name = ''


# player_class #
class Player:
    def __int__(self):
        self.name = ''
        self.hp = 10
        self.damage = 1
        self.effects = []


enemy = Enemy()
zone_map = ZoneMap()
my_player = Player()


# spawns enemy with a name #
def spawn_enemy():
    enemy_names = ['goblin', 'troll', 'wolf']
    enemy.name = random.choice(enemy_names)
    if enemy.name == 'goblin':
        enemy.health = 10
        enemy.damage = 1
    if enemy.name == 'wolf':
        enemy.health = 5
        enemy.damage = 1
    if enemy.name == 'troll':
        enemy.health = 15
        enemy.damage = 2
    print(enemy.name)


# run this to start the game #
def start_game():
    wall_left = False
    wall_right = False
    game_is_running = True
    while game_is_running:
        move = input("> ").lower()
        if move == 'up':
            print("You move forward, in the deep dark")
        if move == 'left' and wall_left is True:
            print(move)
        elif move == 'left' and wall_left is False:
            print("There is a wall blocking your path")

        if move == 'right' and wall_right is True:
            print(move)
        elif move == 'right' and wall_right is False:
            print("there is a wall blocking your path")
        if move == 'down':
            print("You move backwards, in the deep dark")


# input anything into speech, and it will be slowly typed #
def speak(speech):
    for char in speech:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)

# speak("Hello there welcome to rpg game\n")
# speak("Enter your name\n")
# my_player.name = input('> ')

# speak("nice name {}\n".format(my_player.name))
