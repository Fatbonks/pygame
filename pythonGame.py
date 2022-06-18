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
        self.health = 0.0
        self.damage = 0.0
        self.name = ''
        self.exp = 0


# player_class #
class Player:
    def __int__(self):
        self.name = ''
        self.hp = 0
        self.damage = 0
        self.effects = []
        self.exp = 0


enemy = Enemy()
zone_map = ZoneMap()
my_player = Player()
my_player.damage = 1.0
my_player.hp = 10.0


# spawns enemy with a name #
def spawn_enemy():
    enemy_names = ['goblin', 'troll', 'wolf']
    enemy.name = random.choice(enemy_names)
    if enemy.name == 'goblin':
        enemy.health = 10.0
        enemy.damage = 1.0
    if enemy.name == 'wolf':
        enemy.health = 5.0
        enemy.damage = 1.0
    if enemy.name == 'troll':
        enemy.health = 15.0
        enemy.damage = 1.5


# run this to start the game #
def start_game():
    wall_left = False
    wall_right = False
    game_is_running = True
    while game_is_running:
        move = input("> ").lower()
        if move == 'up':
            print("You move forward, in the deep dark")
            choice = random.randint(1, 2)
            if choice == 2:
                combat()
        elif move == 'left' and wall_left is True:
            print(move)
        elif move == 'left' and wall_left is False:
            print("There is a wall blocking your path")

        elif move == 'right' and wall_right is True:
            print(move)
        elif move == 'right' and wall_right is False:
            print("there is a wall blocking your path")
        elif move == 'down':
            print("You move backwards, in the deep dark")


# plays the combat of the game #
def combat():
    global action
    combat_true = True
    spawn_enemy()
    speak("An enemy has appeared!\n")
    speak("Its a {}!".format(enemy.name))
    print("\n##############")
    print("1: attack\n2: ranged attack\n3: run\n")
    print("What will you do?\n")
    while combat_true is True:
        try:
            action = int(input("> "))
            if action == 1:
                random.seed()
                crit = random.randrange(1, 5)
                if crit == 3:
                    my_player.damage = my_player.damage * 2
                else:
                    my_player.damage = 1
                enemy.health = enemy.health - my_player.damage
                print("you did {} HP of damage and the health of the {} is {}".format(my_player.damage, enemy.name,
                                                                                      enemy.health))
                my_player.hp = my_player.hp - enemy.damage
                print("you took {} damage by the {}, you have {} health left".format(enemy.damage, enemy.name,
                                                                                     my_player.hp))
            if action == 2:
                pass
            if action == 3:
                pass
        except ValueError:
            print("That is not what you can do!")
        if enemy.health <= 0:
            combat_true = False
            print("\n You have killed the {}".format(enemy.name))
            start_game()
        if my_player.hp <= 0:
            speak("You have Died!")
            sys.exit()


# input anything into speech, and it will be slowly typed #
def speak(speech):
    for char in speech:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)


speak("Hello there welcome to rpg game\n")
speak("Enter your name\n")
my_player.name = input('> ')
speak("nice name {}\n".format(my_player.name))
speak("are you ready to play the game {}?".format(my_player.name))
print("\nyes / no")
answer = input("> ".lower().strip())
if answer == "yes":
    start_game()
if answer == "no":
    print("\nok bye")
    sys.exit()

