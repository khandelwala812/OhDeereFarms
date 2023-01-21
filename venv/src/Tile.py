CONDITIONS = ["empty", "tilled", "seed", "seedling", "hapling", "harvest"]


class Tile:
    def __init__(self, crop):
        self._crop = crop
        self._growthTime = crop.growthTime
        self._condition = 0
        self._fertilizerLevel = 0

    @property
    def growthTime(self):
        return self._growthTime * (1 - self._fertilizerLevel)

    @growthTime.setter
    def growthTime(self, time):
        self._growthTime = time

    @property
    def condition(self):
        return CONDITIONS[self._condition]

    @condition.setter
    def condition(self, condition):
        self._condition = condition

    @property
    def fertilizerLevel(self):
        return self._fertilizerLevel

    @fertilizerLevel.setter
    def fertilizerLevel(self, level):
        self._fertilizerLevel = level
