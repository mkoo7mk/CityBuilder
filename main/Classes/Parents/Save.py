import pickle
from os.path import exists

from .Map import Map
from .Game import Game


class Save(object):
    def __init__(self, map: Map, game: Game):
        self.__map = map
        self.__game = game

    def get_map(self) -> Map:
        return self.__map

    def get_game(self) -> Game:
        return self.__game

    def save(self):
        with open('./Saves/save1.pickle', 'wb') as handle:
            pickle.dump(self, handle)
