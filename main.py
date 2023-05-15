# main

import pygame
import numpy as np

pygame.init()

win = pygame.display.set_mode((800, 800))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()