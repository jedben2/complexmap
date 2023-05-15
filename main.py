# main

import pygame
import numpy as np

pygame.init()

win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Complex Map")

num_lines = 100
density = 100
bound = -100

def f(z):
    return np.power(z, -1)

def convolute(a, b):
    return a * (1-t) + b * t

points = np.array([np.linspace(-1 * bound, bound, density) + (-1 * bound + (2 * bound) * i / num_lines) * 1j for i in range(num_lines)] + [np.linspace(-1 * bound, bound, density) * 1j + (-1 * bound + (2 * bound) * i / num_lines) for i in range(num_lines)])

mapped_points = f(points)

t = 0

running = True
anim = 1
while running:
    win.fill((0, 0, 0))
    for p1, line in enumerate(points):
        mapped_line = mapped_points[p1]
        for p2, point in enumerate(line):
            mapped_point = mapped_line[p2]
            pygame.draw.circle(win, (255, 255, 255), (convolute(point, mapped_point).real * 8 + 400, convolute(point, mapped_point).imag* 8 + 400), 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    if anim:
        if t >= 1: t = 1
        else: t += 0.005