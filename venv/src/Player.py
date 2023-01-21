import time
import pygame

# 0/1 idle 1 and 2
# 2 work
# 3/4 left
# 5/6 right
# 7/8 up
# 9/10 down

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

    def left(self):
        if skin != 3 and timePlayer % 2 <= 0.5:
            skin = 3
            timePlayer = time.time()
        else:
            skin = 4
            timePlayer = time.time()

    def right(self):
        if skin != 5 and timePlayer % 2 <= 0.5:
            skin = 5
            timePlayer = time.time()
        else:
            skin = 6
            timePlayer = time.time()

    def up(self):
        if skin != 7 and timePlayer % 2 <= 0.5:
            skin = 7
            timePlayer = time.time()
        else:
            skin = 8
            timePlayer = time.time()

    def down(self):
        if skin != 9 and timePlayer % 2 <= 0.5:
            skin = 9
            timePlayer = time.time()
        else:
            skin = 10
            timePlayer = time.time()

    def update(self):
        if (skin != 0) and timePlayer + 1 < time.time():
            skin = 0
            timePlayer = time.time()
        if (skin == 0) and timePlayer + 1 < time.time():
            skin = 1
            timePlayer = time.time()





