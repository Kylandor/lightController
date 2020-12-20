import board
import neopixel
import atexit
from random import randrange

def exit_handler():
    pixels.fill((0, 0, 0))
    pixels.show()

atexit.register(exit_handler)

print("displaying...")

ORDER = neopixel.GRB
NUM_LEDS = 150

pixels = neopixel.NeoPixel(
    board.D18, NUM_LEDS, brightness=0.8, auto_write=False, pixel_order=ORDER
)

r = 100
g = 100
b = 100
add = 1
while True:
    pixels.fill((r, b, g))
    rRand = randrange(2)
    gRand = randrange(2)
    bRand = randrange(2)
    if rRand:
        r +=1
    else:
        r -=1
    if gRand:
        g +=1
    else:
        g -=1
    if bRand:
        b +=1
    else:
        b -=1
    pixels.show()