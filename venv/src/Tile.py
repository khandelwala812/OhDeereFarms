import datetime

CONDITIONS = ["empty", "tilled", "seed", "seedling", "hapling", "harvest"]


class Tile:
    def __init__(self, crop):
        self._crop = crop
        self._cropHarvests = {}
        self._growthTime = crop.growthTime
        self._condition = 0
        self._fertilizerLevel = 0
        self._tillage = 0
        self._firstTilled = None

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
        oldCondition = self._condition
        self._condition = condition

        cropType = self._crop.type
        if (oldCondition == len(CONDITIONS) - 1 and condition == 0):
            if (cropType in self._cropHarvests):
                self._cropHarvests[cropType] += 1
            else:
                self._cropHarvests[cropType] = 1

        if (condition == 1):
            if (self._tillage == 0):
                now = datetime.datetime.now()
                self._firstTilled = now.strftime("%H:%M")
            self._tillage += 1

    @property
    def fertilizerLevel(self):
        return self._fertilizerLevel

    @fertilizerLevel.setter
    def fertilizerLevel(self, level):
        self._fertilizerLevel = level
