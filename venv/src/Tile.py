import time

CONDITIONS = ["empty", "tilled", "seed", "seedling", "hapling", "harvest"]


class Tile:
    def __init__(self, crop=None):
        self._crop = crop
        self._lastCrop = None
        self._sameCrop = 0

        if crop is None:
            self._growthTime = 0
        else:
            self._growthTime = crop.growthTime

        self._condition = 0
        self._fertilizerLevel = 0
        self._tillage = 0
        self._timeTilled = (0, 0)

    @property
    def sameCrop(self):
        return self._sameCrop

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

        if (oldCondition == len(CONDITIONS) - 1 and condition == 0):
            if self._crop is not None and self._crop.type == self._lastCrop:
                self._sameCrop += 1
            else:
                self._sameCrop = 0

        if (condition == 1):
            now = int(round(time.time()))

            if (self._timeTilled[0] == 0):
                self._timeTilled = now, 0
            else:
                prevTime = self._timeTilled[0]
                self._timeTilled = now, prevTime
        self._tillage += 1

    @property
    def fertilizerLevel(self):
        return self._fertilizerLevel

    @fertilizerLevel.setter
    def fertilizerLevel(self, level):
        self._fertilizerLevel = level

    @property
    def tillage(self):
        return self._tillage

    @tillage.setter
    def tillage(self, tillage):
        self._tillage = tillage

    @property
    def firstTilled(self):
        return self._firstTilled

    @firstTilled.setter
    def firstTilled(self, firstTilled):
        self._firstTilled = firstTilled

    def __isOverTilled(self):
        recent, prev = self._timeTilled
        limit = self._growthTime * 60

        if (recent == 0):
            return False

        # replace 60 with meaningful variable
        now = int(round(time.time()))
        return (prev != 0 and recent - prev < limit) or (now - recent < limit)

    def isOverTilled(self):
        return 1 if self.__isOverTilled() else 0

