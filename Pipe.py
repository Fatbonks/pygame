import select

from GameData import GameData
import EnemyCreation as enemyCreation
import PlayerCreation as playerCreation
import LevelLogic as levelLogic
import MagicLogic as magicLogic
import CombatLogic as combatLogic
import HealingLogic as healingLogic
import physical_skills as physical_skill
import random as ran
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
        time.sleep(1 / 160)
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
