import random

from HeatMap import heatmap


class Game:

    def __init__(self):
        pass

    def generateWeather(self, tiles):
        isRaining = random.uniform(0, 1) < 0.1

        if isRaining:
            fertilizerVal = heatmap(tiles, "f")
            tillageVal = heatmap(tiles, "t")
            sameCropVal = heatmap(tiles, "s")

            weatherVal = int(round((fertilizerVal + tillageVal + sameCropVal) / 3))
            offset = 10
            return random.randint(weatherVal, weatherVal + offset)

        return 0
