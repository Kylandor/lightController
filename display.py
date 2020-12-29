import board
import neopixel
import atexit
import time
import sys
import array
import math
import requests
from random import randrange

def exit_handler():
    pixels.fill((0, 0, 0))
    pixels.show()

#atexit.register(exit_handler)

print("displaying...")

ORDER = neopixel.GRB
NUM_LEDS = 150

pixels = neopixel.NeoPixel(
    board.D18, NUM_LEDS, brightness=0.8, auto_write=False, pixel_order=ORDER
)

def readFrame(data):
    global pixels
    numColors = data[0]
    allColors  = []
    sizeOfInd = math.ceil(math.log2(numColors + 1))
    for i in range(numColors):
        allColors.append((data[1 + i * 3 + 0], data[1 + i * 3 + 1], data[1 + i * 3 + 2]))
    bits = ""
    curInd = 1 + (3*numColors) 
    while True:
        curItem = data[curInd]
        if curItem == 0:
            break
        cur = bin(curItem)[2:]
        if len(cur) != 8:
            cur = "0" * (8-len(cur)) + cur
        bits += cur
        curInd += 1
    ledInd = 0
    while len(bits) != 0:
        ledColorIndex = bits[:sizeOfInd]
        ledColorIndex = int(ledColorIndex, 2) -1
        if ledColorIndex != -1:
             pixels[ledInd] = allColors[ledColorIndex]
        ledInd +=1
        bits = bits[sizeOfInd:]
    findArray = data[1 + (3 * numColors):]
    findInd = findArray.index(0)
    data = data[(2 + (3 * numColors) + findInd):]
    pixels.show()
    return data

url = "http://192.168.1.38:5000/getFrames"
r = requests.get(url, allow_redirects=True)
open('frames', 'wb').write(r.content)
f =  open('frames', 'rb')
readData = []
byte = f.read(1)
while byte:
    readData.append(int.from_bytes(byte, "big"))
    byte = f.read(1)
while len(readData) != 0: 
    start = time.time()
    readData = readFrame(readData)
    if float(sys.argv[1]) - (time.time()-start) > 0:
        time.sleep(float(sys.argv[1]) - (time.time()-start))
    else:
        print("late")
f.close()
    
