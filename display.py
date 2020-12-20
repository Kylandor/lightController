import board
import neopixel

print("displaying...")

NUM_LEDS = 150
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS)

while True:
    pixels.fill((0, 0, 255))
    pixels.show()