import time
class Player:
    skin = 0 #standing_1
    timePlayer = time.time()

    def __init__(self):
        pass

    def till(self):
        skin = 2
        timePlayer = time.time()

    def plant(self):
        skin = 2
        timePlayer = time.time()

    def harvest(self):
        skin = 2
        timePlayer = time.time()

    def update(self):
        if (skin != 0) and timePlayer + 1 < time.time():
            skin = 0
            timePlayer = time.time()
        if (skin == 0) and timePlayer + 1 < time.time():
            skin = 1
            timePlayer = time.time()





