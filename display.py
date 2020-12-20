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

firstLine = True
data = []
f = open("data.txt" , "r")
for x in f:
    data.append(x)
while True:
    if firstLine:
        cur = data[0]
    if not firstLine:
        cur = data[1]

    for ind, i in enumerate(cur):
        if i == "0":
            pixels[ind] = Color(0, 255, 0)
        elif i == "1":
            pixels[ind] = Color(255, 0, 0)
        
    pixels.show()
    firstLine = not firstLine
    
