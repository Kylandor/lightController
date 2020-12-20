import board
import neopixel

print("displaying...")

NUM_LEDS = 150
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS)

pixels.fill((0, 255, 0))
pixels.show()