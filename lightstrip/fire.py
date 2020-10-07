#!/usr/bin/env python3
import time
import random

import fakeboard as board
import fakeneopixel as neopixel

pixelCount = 144

# update the colors for one "click"
def update(pixels):
    global pixelCount
    for x in range(pixelCount):
        pixels[x] = (random.randint(16,64), 32, 16)

## the main loop
def main():
    global pixelCount
    pixels = neopixel.NeoPixel(board.D18, pixelCount)
    while True:
        update(pixels)
        pixels.show()
        time.sleep(0.1)
    return

if __name__ == "__main__":
    main()
