import numpy as np
import random

class Game:

    def __init__(self, player):
        self._tiles = np.zeros((100, 100))
        self._player = player

    def upgradeTile(self, pos):
        self._tiles[pos].condition += 1

    def harvestTile(self, pos):
        self._tiles[pos].condition = 1

        return self._tiles[pos].yields

    def generateWeather(self):
        # rainy or sunny
        randValue = random.uniform(0, 1)

        if (randValue > 0.1):
            return "sunny"
        return "rainy"