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

while True:
    pixels.fill((0, 0, 255))
    pixels.show()