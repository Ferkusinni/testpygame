#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random
import sys

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

pygame.font.init()
pygame.init()

font = pygame.font.Font(None, 25)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((400, 700))
pygame.display.set_caption('test')

# class Ship():
#     image = pygame.image.load('ship.png')
#     speed = 1
#     hp = 20

#Основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()

    clock.tick(20)#Фпс

pygame.quit()
