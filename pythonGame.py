import random


# import time
# import sys
# import os


# map #
class ZoneMap:
    def __int__(self):
        self.left = False
        self.right = False
        self.down = True


zone_map = ZoneMap()


# enemy_class #
class Enemy:
    def __int__(self):
        self.health = 0
        self.damage = 0
        self.name = ''


enemy = Enemy()


# player_class #
class Player:
    def __int__(self):
        self.name = ''
        self.hp = 10
        self.damage = 1
        self.effects = []


my_player = Player()


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


def start_game():
    wall = False
    game_is_running = True
    while game_is_running:
        move = input("> ").lower()
        if move == 'up':
            print(move)
        if move == 'left' and wall == True:
            print(move)
        elif move == 'left' and wall == False:
            print("There is a wall blocking your path")

        if move == 'right':
            print(move)
        if move == 'down':
            print(move)


# print("What is your name?")

# my_player.name = input('> ')

# print("Ah, i see {}. What a nice name!".format(my_player.name))

start_game()
