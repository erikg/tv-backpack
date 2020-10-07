#!/usr/bin/env python3

import fakeboard as board
import fakeneopixel as neopixel

pixelCount = 144
black = (0, 0, 0)

# update the colors for one "click"
def update(pixels):
    for x in range(pixelCount):
        pixels[x] = black

## the main loop
def main():
    pixels = neopixel.NeoPixel(board.D18, pixelCount, brightness=0.0, auto_write=False, pixel_order=neopixel.GRB)
    update(pixels)
    pixels.show()

if __name__ == "__main__":
    main()
