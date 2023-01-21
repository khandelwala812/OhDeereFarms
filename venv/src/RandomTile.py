import random

CONDITIONS = ["pond_1", "pond_2", "pond_3", "grass_1", "grass_2", "grass_3", "grass_4", "grass_5"]


class RandomTile:
    def __init__(self):
        self._condition = random.randint(0, 7)

    @property
    def condition(self):
        return CONDITIONS[self._condition]
