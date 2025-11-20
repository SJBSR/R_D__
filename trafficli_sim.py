# Simulating traffic light behavior
import time
from itertools import cycle

lights = [
    ('Green', 2.0),
    ('Yellow', 0.5),
    ('Red', 2.0)
    ]
#Theres always a better way
    #i = 0
    #while True:
        #c,s = lights[i]
        #print(c)
        #time.sleep(s)
        #if i == len(lights) - 1:
            #i = 0
        #else:
            #i += 1
colors = cycle(lights)
while True:
        c,s = next(colors)
        print(c)
        time.sleep(s)