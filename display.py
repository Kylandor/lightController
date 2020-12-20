import board
import neopixel
import atexit

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

val = 0
add = 1
while True:
    pixels.fill((0, 0, val))
    val += add
    if val == 255:
        add = -1
    if val ==0:
        add = 1
    pixels.show()