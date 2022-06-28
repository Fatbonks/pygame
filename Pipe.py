from GameData import GameData
import EnemyCreation as enemyCreation
import PlayerCreation as playerCreation
import LevelLogic as levelLogic
import MagicLogic as magicLogic
import CombatLogic as combatLogic
import HealingLogic as healingLogic
import random as ran
import time
import sys


def get_integer_input(question, acceptable_high, acceptable_low):
    while True:
        try:
            output = int(input(question))
        except ValueError:
            pass
        if acceptable_high >= output >= acceptable_low:
            return output


def print_dialogue(dialogue):
    dialogue = list(dialogue)
    for dial in dialogue:
        sys.stdout.write(dial)
        sys.stdout.flush()
        time.sleep(1 / 65)
    sys.stdout.write('\n')
    sys.stdout.flush()


if __name__ == '__main__':
    exit('Please run main.py')
else:
    gameData = GameData()
