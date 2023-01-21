import asyncio
import threading

class Thread(threading.Thread):
    def run(self):
        r, g, b = 160, 0, 0
        while True:
            await asyncio.sleep(0.005)
            if b == 0:
                if r == 160 and g < 160:
                    g += 1
                elif r > 0 and g == 160:
                    r -= 1
            elif r == 0:
                if g == 160 and b < 160:
                    b += 1
                elif g > 0 and b == 160:
                    g -= 1
            elif g == 0:
                if b == 160 and r < 160:
                    r += 1
                elif b > 0 and r == 160:
                    b -= 1
            #160,0,0
            #while R = 160, G increase
            #if R & G = 160, R decrease
            #0,160,0
            #while G = 160, B increase
            #if G & B = 160, G decrease
            #0,0,160
            #while B = 160, R increase
            #if B & R = 160, B decrease