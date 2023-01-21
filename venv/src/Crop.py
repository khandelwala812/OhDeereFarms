class Crop:

    def __int__(self, type, growthTime):
        self._type = type
        self._growthTime = growthTime

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def growthTime(self):
        return self._growthTime

    @growthTime.setter
    def growthTime(self, time):
        self._growthTime = time
