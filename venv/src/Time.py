from array import *
import time

def check_tiles():
    for i in tiles:
        for j in tiles[i]:
            timeVar = time.time()
            state = tiles[i][j].state
            if state >= 2 and state <= 4 and (tiles[i][j].crop.growthTime <= timeVar - tiles[i][j].growTime):
                tiles[i][j].update()


