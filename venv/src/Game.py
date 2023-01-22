import random

import numpy as np
from HeatMap import heatmap


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
        isRaining = random.uniform(0, 1) < 0.1

        if isRaining:
            fertilizerVal = heatmap(self._tiles, "f")
            tillageVal = heatmap(self._tiles, "t")
            sameCropVal = heatmap(self._tiles, "s")

            weatherVal = int(round((fertilizerVal + tillageVal + sameCropVal) / 3))
            offset = 10
            return random.randint(weatherVal, weatherVal + offset)

        return 0
