#!/usr/bin/env python3

import time

import fakeboard as board
import fakeneopixel as neopixel

pixelCount = 144

black = (0, 0, 0)
red = (255, 0, 0)

# update the colors for one "click"
curOffset=0
curDir=1
def update(pixels):
    global curOffset, curDir
    curOffset += curDir
    if curOffset <= 0:
        curDir = 1
    if curOffset >= 143:
        curDir = -1
    for x in range(pixelCount):
        pixels[x] = black
    pixels[curOffset] = red

## the main loop
def main():
    pixels = neopixel.NeoPixel(board.D18, pixelCount)
    while True:
        update(pixels)
        pixels.show()
        time.sleep(0.1/30)
    return

if __name__ == "__main__":
    main()
