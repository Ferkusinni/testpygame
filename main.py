#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys
import pygame
from pygame.locals import *

def init_window():
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('JFRPG')

def input(events):
    for event in events:
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit(0)
        else:
            pass

def action():
    while True:
        input(pygame.event.get())

def main():
    init_window()
    action()

if __name__ == '__main__': main()
