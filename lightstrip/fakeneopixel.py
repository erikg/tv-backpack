#!/usr/bin/env python3

import pygame
import random

RGB=0
GRB=0

class NeoPixel(object):
    def __init__(self, pin, num, freq_hz=800000, dma=10, invert=False, brightness=255, channel=0, auto_write=True, pixel_order=0):
        pygame.init()
        self.pixelCount = num
        self.scale = 7
        self.arr = [(0,0,0)]*self.pixelCount
        self.display = pygame.display.set_mode((self.pixelCount * self.scale, self.scale))

    def __getitem__(self, key):
        return self.arr[key]

    def __setitem__(self, key, value):
        self.arr[key] = value

    def show(self):
        scale = self.scale
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        for i, a in enumerate(self.arr):
            pygame.draw.rect(self.display, a, pygame.Rect(i * scale, 0, scale, scale))
        pygame.display.update()
