# main

import pygame
import numpy as np

pygame.init()

win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Complex Map")

num_lines = 30
density = 400
bound = 5
zoom = 256
jump = .0005

def f(z):
    return (z.imag + z.real) / 2 + (z.imag - z.real) * 0.5j

def convolute(a, b):
    return a * (1-t) + b * t

def convolute2(a, b):
    return np.power(a, 1-t) * np.power(b, t)

points = np.array([np.linspace(-1 * bound, bound, density) + (-1 * bound + (2 * bound) * i / num_lines) * 1j for i in range(num_lines)] + [np.linspace(-1 * bound, bound, density) * 1j + (-1 * bound + (2 * bound) * i / num_lines) for i in range(num_lines)])
triangle = np.linspace(0.01, 1, 20) + 3j * np.linspace(0.01, 1, 20)
triangle = np.append(triangle, np.linspace(1, 2, 20) + 1j * (4 - np.linspace(1, 2, 20)))
triangle = np.append(triangle, np.linspace(0.01, 2, 20) + 1j *  np.linspace(0.01, 2, 20))
mapped_triangle = f(triangle)
mapped_points = f(points)

t = 0

print(triangle)


running = True
while running:
    win.fill((0, 0, 0))
    """for p1, line in enumerate(points):
        mapped_line = mapped_points[p1]
        for p2, point in enumerate(line):
            mapped_point = mapped_line[p2]
            pygame.draw.circle(win, (255, 164, 0), (convolute(point, mapped_point).real * zoom + 400, convolute(point, mapped_point).imag * zoom + 400), 1)"""

    for p1, point in enumerate(triangle):
        mapped_point = mapped_triangle[p1]

        pygame.draw.circle(win, (255, 164, 0), (convolute(point, mapped_point).real * zoom + 400, -1 * convolute(point, mapped_point).imag * zoom + 400), 1)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                zoom *= 2
            elif event.key == pygame.K_DOWN:
                zoom /= 2
    keys = pygame.key.get_pressed()
    t += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * jump
    if t < 0: t = 0
    if t > 1: t = 1

    pygame.display.flip()
