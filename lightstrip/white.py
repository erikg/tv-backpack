#!/usr/bin/env python3

import fakeboard as board
import fakeneopixel as neopixel

def main():
    pixelCount = 144
    white = (255, 255, 255)
    pixels = neopixel.NeoPixel(board.D18, pixelCount, brightness=1.0, auto_write=False, pixel_order=neopixel.GRB)
    for i in range(pixelCount):
        pixels[i] = white
    pixels.show()

if __name__ == "__main__":
    main()
