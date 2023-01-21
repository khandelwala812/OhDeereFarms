class Crop:

    def __init__(self, type, cost, yields, growthTime):
        self._type = type
        self._cost = cost
        self._yields = yields
        self._growthTime = growthTime

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = cost

    @property
    def growthTime(self):
        return self._growthTime

    @growthTime.setter
    def growthTime(self, time):
        self._growthTime = time

    @property
    def yields(self):
        return self._yields

    @yields.setter
    def yields(self, yields):
        self._yields = yields
