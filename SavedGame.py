import Pipe as game
import pickle

import main


def save_game():
    with open('saved_game.pkl', 'wb') as saved_game:
        pickle.dump(game.gameData, saved_game)


def load_game():
    try:
        with open('saved_game.pkl', 'rb') as loaded_game:
            game.gameData = pickle.load(loaded_game)
            game.gameData.has_loaded = True
    except:
        print('no saved game found')
