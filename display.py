import board
import neopixel
import atexit

def exit_handler():
    pixels.fill((0, 0, 0))
    pixels.show()

atexit.register(exit_handler)

print("displaying...")

NUM_LEDS = 150
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, 0.8)

while True:
    pixels.fill((0, 0, 255))
    pixels.show()