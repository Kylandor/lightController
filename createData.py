import array
import math
import random

# An python array is like a restricted python list 
# for storing binary data.
#
data = array.array('B')  # create array of bytes.

def makePacket(colors):
    data = array.array('B')
    uniqueColors = []
    for c in colors:
        if c not in uniqueColors:
            uniqueColors.append(c)

    numColors = len(uniqueColors)
    pixels = [0] * len(colors)
    for i, p in enumerate(colors):
        pixels[i] = uniqueColors.index(p)

    data.append(numColors)

    for c in uniqueColors:
        for k in c:
            data.append(k)
        
    pixelString = ""
    dataLength = math.ceil(math.log2(numColors + 1))

    for p in pixels:
        curInd = bin(p+1)[2:]
        if len(curInd) < dataLength:
            curInd = '0' * (dataLength - len(curInd)) + curInd
        pixelString += curInd
    
    while len(pixelString) != 0:
        if len(pixelString) > 8:
            data.append(int(pixelString[:8], 2))
            pixelString = pixelString[8:]
        else:
            modifided = pixelString + '0' * (8 - len(pixelString))
            data.append(int(modifided, 2))
            pixelString = ''
    data.append(0)
    return data


        
colorArray = []
for i in range(150):
    colorArray.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

data = (makePacket(colorArray))


print(data)

# Write the array at once to a file
#
f = open('frames', 'wb')
data.tofile(f)
f.close()

