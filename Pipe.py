# import select

from GameData import GameData
import json
import EnemyCreation
import PlayerCreation
import LevelLogic
import MagicLogic
import CombatLogic
import HealingLogic
import physical_skills
import SavedGame
import random
import time
import sys
import os


def get_input(question):
    sys.stdout.write(question)
    sys.stdout.flush()

    print_dialogue("\n> ")
    return sys.stdin.readline().replace("\n", "")


def print_dialogue(dialogue):
    dialogue = list(dialogue)
    for dial in dialogue:
        sys.stdout.write(dial)
        sys.stdout.flush()
        time.sleep(1 / 64)
    sys.stdout.write('\n')
    sys.stdout.flush()


def draw_line():
    print('##----------------------------------------##')


def clear():
    os.system('cls')


if __name__ == '__main__':
    exit('Please run main.py')
else:
    gameData = GameData()
    enemyCreation = EnemyCreation
    playerCreation = PlayerCreation
    levelLogic = LevelLogic
    magicLogic = MagicLogic
    combatLogic = CombatLogic
    healingLogic = HealingLogic
    physical_skill = physical_skills
    SavedGame = SavedGame
    ran = random


