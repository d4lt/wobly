from math import log2
import pygame
from pygame import Surface
import time
import random
from grid import Grid

# pygame.init()

WIDTH = 1600
HEIGHT = WIDTH - 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
title = 'Wobly'
pygame.display.set_caption(title)
# TODO: Icon

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_circunference(win: Surface, pos: tuple, radius, gap=2.0):
    pygame.draw.circle(win, WHITE, pos, radius)
    pygame.draw.circle(win, BLACK, pos, (radius - gap))
    pygame.display.update()


def draw_wave(win: Surface, pos, max_radius):

    initial_radius = 5

    initial_gap = max_radius//20

    for radius in range(initial_radius, max_radius):
        new_gap = initial_gap - radius//20

        draw_circunference(win, pos, radius, gap=new_gap)
        pygame.display.update()

    win.fill(BLACK)


def main(win):
    grid = Grid(win, 50)
    grid_data = grid.make_grid()


    running = True
    win.fill(BLACK)

    while (running):
        grid.draw(grid_data)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if pygame.mouse.get_pressed()[0]:
                pass
                # mouse_pos = list(pygame.mouse.get_pos())
                # max_radius = random.randint(200, 550)
                #
                # draw_wave(win, mouse_pos, max_radius)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    win.fill(BLACK)

        pygame.display.update()

window.fill((255, 255, 255))

main(window)

pygame.quit()
