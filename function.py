import cmath
import pickle
import random as ran
# import sys
# import time
# import classes as cl
import pythonGame as py

player_cl = None
enemy_type = None


# the player class(aka the stats of the player) that the player can pick #
def player_class():
    global player_cl
    print("Pick your class\n1: warrior\n2: mage\n3: archer\n4: thief")
    true = True
    while true:
        try:
            act = int(input("> ").lower().strip())
            if act == 1:
                player_cl = py.warrior
                print(player_cl.class_type)
                true = False
            elif act == 2:
                player_cl = py.mage
                print(player_cl.class_type)
                true = False
            elif act == 3:
                player_cl = py.archer
                print(player_cl.class_type)
                true = False
            elif act == 4:
                player_cl = py.thief
                print(player_cl.class_type)
                true = False
        except ValueError:
            print("please input a valid number!")
    print("------------")
    print("are you ready to start Yes / No")
    ans = input("> ").lower()
    if ans == 'yes':
        game(player_cl)
    elif ans == 'no':
        exit(0)


def take_damage(attacker, defender):
    dmg = ran.randint(attacker.damage['min_damage'], attacker.damage['max_damage'])
    defender.health = defender.health - dmg
    if defender.health <= 0:
        print("------------------")
        print("{} has been slain by {}".format(defender.name, attacker.name))
        print("{} has {} health left".format(attacker.name, attacker.health))
        attacker.exp = attacker.exp + defender.exp
        level_up(player_cl)
        if player_cl.health <= 0:
            print("You have died")
            exit(0)
        else:
            game(player_cl)
    else:
        print("------------------")
        print("{} takes {} damage".format(defender.name, dmg))
        print("{} health is {}\nThe {} health is {}".format(attacker.name, attacker.health, defender.name,
                                                            defender.health))


def commands_for_combat(player, enemy):
    true = True
    while true:
        print("------------------")
        print("1: Attack\n2: Magic attack\n3: Run")
        try:
            act = int(input("> "))
            if act == 1:
                if player.speed >= enemy.speed:
                    take_damage(player, enemy)
                    take_damage(enemy, player)
                else:
                    take_damage(enemy, player)
                    take_damage(player, enemy)
            elif act == 2:
                pass
            elif act == 3:
                ran.seed()
                rand = ran.randint(0, 1)
                if rand == 0:
                    print("You have ran away!")
                    input("input any key to exit")
                    game(player_cl)
                elif rand == 1:
                    print("the enemy did not let you escape and took the chance to attack!")
                    take_damage(enemy, player)
        except ValueError:
            pass


def level_up(player):
    print("----------------------")
    print("Level: {}".format(player.level))
    print("EXP: {}".format(player.exp))
    print("Next Level: {}".format(player.level_next))
    print("----------------------")
    l_health, l_damage = 0.0, 0.0
    while player.exp >= player.level_next:
        player.level += 1
        player.exp = player.exp - player.level_next
        player.level_next = round(player.level_next * 1.2)
        l_health += 0.5
        l_damage += 0.5
        print("----------------------")
        print("Level: {}".format(player.level))
        print("EXP: {}".format(player.exp))
        print("Next Level: {}".format(player.level_next))
        hold_health = player.health
        hold_min_damage = player.damage['min_damage']
        hold_max_damage = player.damage['max_damage']
        player.health += l_health
        player.damage['min_damage'] += l_damage
        player.damage['max_damage'] += l_damage
        print("-------------------")
        print("{} health --> {} health".format(hold_health, player.health))
        print("{} min damage, {} max damage --> {} min damage, {} max damage".format(hold_min_damage, hold_max_damage,
                                                                                     player.damage['min_damage'],
                                                                                     player.damage['min_damage']))


def event():
    rand = ran.randrange(1, 2)
    if rand == 1:
        enemy_picker()
        print("You have encountered an {}".format(enemy_type.name))
        commands_for_combat(player_cl, enemy_type)

    elif rand == 2:
        pass


def game(player):
    option = ['up', 'left', 'right', 'stats', 'exit']
    while True:
        print("Up: Move up\nLeft: Move left\nRight: Move right\nStats: Shows your stats\nExit: To leave the game")
        answer = input("> ").lower().strip()
        if answer in option:
            if answer == 'up':
                event()
            elif answer == 'left':
                pass
            elif answer == 'right':
                pass
            elif answer == 'stats':
                print("Level: {}\nHealth: {}\nMana: {}\nDamage: {} Min damage {} Max damage\nEXP: {}\nSpeed: "
                      "{}\nDodge: {}\nLevel next: {}\n".format(player.level, player.health, player.mana,
                                                               player.damage['min_damage'],
                                                               player.damage['max_damage'],
                                                               player.exp, player.speed, player.dodge
                                                               , player.level_next))
            elif answer == 'exit':
                exit(0)
        else:
            pass


def enemy_picker():
    enemys = ['troll', 'wolf', 'zombie', 'skeleton']
    global enemy_type
    enemy = ran.choice(enemys)
    if enemy == 'troll':
        enemy_type = py.troll
    if enemy == 'wolf':
        enemy_type = py.wolf
    if enemy == 'zombie':
        enemy_type = py.zombie
    if enemy == 'skeleton':
        enemy_type = py.skeleton


player_class()


