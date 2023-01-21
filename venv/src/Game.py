import numpy as np
import random

class Game:

    def __init__(self, player):
        self._tiles = np.zeros((100, 100))
        self._player = player

    @property
    def tiles(self):
        return self._tiles

    @tiles.setter
    def tiles(self, tiles):
        self._tiles = tiles

    def upgradeTile(self, pos):
        self._tiles[pos].condition += 1

    def harvestTile(self, pos):
        self._tiles[pos].condition = 0

        return self._tiles[pos].yields

    def generateWeather(self):
        # rainy or sunny
        randValue = random.uniform(0, 1)

        if (randValue > 0.1):
            return "sunny"
        return "rainy"