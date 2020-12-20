import board
import neopixel

print("displaying...")

NUM_LEDS = 150
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS)

red = 0
green = 255
blue = 0
move = -1
while True:
pixels.fill((red, green, blue))
green += move
if green == 255:
    move = -1
elif green == 0:
    move = 1
pixels.show()