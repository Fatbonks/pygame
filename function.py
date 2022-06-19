import random
import sys
import time
import classes


# the player class(aka the stats of the player) that the player can pick #
def player_class():
    print("Pick your class\n1: warrior\n2: mage\n3: archer\n4: thief")
    true = True
    while true:
        try:
            answer = int(input("> "))
            if answer == "1":
                classes.my_player.hp = 13.0
                classes.my_player.damage = 3.0
                classes.my_player.mana = 3.0
                classes.my_player.speed = 1.0
                classes.my_player.level = 1
            if answer == "2":
                classes.my_player.hp = 6.0
                classes.my_player.damage = 2.5
                classes.my_player.mana = 15.0
                classes.my_player.speed = 2.0
                classes.my_player.level = 1
            if answer == "3":
                classes.my_player.hp = 8.0
                classes.my_player.damage = 1.5
                classes.my_player.mana = 6.0
                classes.my_player.speed = 4.0
                classes.my_player.level = 1
            if answer == "4":
                classes.my_player.hp = 10.0
                classes.my_player.damage = 1
                classes.my_player.mana = 5.0
                classes.my_player.speed = 3.0
                classes.my_player.dodge = 5.0
                classes.my_player.level = 1
            true = False
        except ValueError:
            print("That's not what you can pick")


# spawns enemy with a name #
def spawn_enemy():
    enemy_names = ['goblin', 'troll', 'wolf']
    classes.enemy.name = random.choice(enemy_names)
    if classes.enemy.name == 'goblin':
        classes.enemy.health = 10.0
        classes.enemy.damage = 1.0
    if classes.enemy.name == 'wolf':
        classes.enemy.health = 5.0
        classes.enemy.damage = 1.0
    if classes.enemy.name == 'troll':
        classes.enemy.health = 15.0
        classes.enemy.damage = 1.5


# run this to start the game #
def start_game():
    classes.zone_map.wall_left = False
    classes.zone_map.wall_right = False
    game_is_running = True
    while game_is_running:
        move = input("> ").lower()
        if move == 'up':
            print("You move forward, in the deep dark")
            choice = random.randint(1, 2)
            if choice == 2:
                combat()
        elif move == 'left' and classes.zone_map.wall_left is True:
            print(move)
        elif move == 'left' and classes.zone_map.wall_left is False:
            print("There is a wall blocking your path")

        elif move == 'right' and classes.zone_map.wall_right is True:
            print(move)
        elif move == 'right' and classes.zone_map.wall_right is False:
            print("there is a wall blocking your path")
        elif move == 'down':
            print("You move backwards, in the deep dark")


# plays the combat of the game #
def combat():
    global action
    combat_true = True
    spawn_enemy()
    speak("An enemy has appeared!\n")
    speak("Its a {}!".format(classes.enemy.name))
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
                    classes.my_player.damage = classes.my_player.damage * 2
                else:
                    classes.my_player.damage = 1
                classes.enemy.health = classes.enemy.health - classes.my_player.damage
                print("you did {} HP of damage and the health of the {} is {}".format(classes.my_player.damage,
                                                                                      classes.enemy.name,
                                                                                      classes.enemy.health))
                classes.my_player.hp = classes.my_player.hp - classes.enemy.damage
                print("you took {} damage by the {}, you have {} health left".format(classes.enemy.damage,
                                                                                     classes.enemy.name,
                                                                                     classes.my_player.hp))
            if action == 2:
                pass
            if action == 3:
                pass
        except ValueError:
            print("That is not what you can do!")
        if classes.enemy.health <= 0:
            combat_true = False
            print("\n You have killed the {}".format(classes.enemy.name))
            start_game()
        if classes.my_player.hp <= 0:
            speak("You have Died!")
            sys.exit()


def create_armor():
    if classes.my_player.level > 0:
        pass


# input anything into speech, and it will be slowly typed #
def speak(speech):
    for char in speech:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)
