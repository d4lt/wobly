import pygame
from pygame import Surface
import time
import random
from threading import Thread

pygame.init()

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
    for offset in range(2, 500):
        # time.sleep(0.2)
        new_gap = 10 - offset * 0.15

        draw_circunference(win, pos, initial_radius + offset, gap=new_gap)
        pygame.display.update()

    win.fill(BLACK)

def spawn_wave(win: Surface, pos, max_radius):
    new_thread = Thread(target=draw_wave, args=(win, pos, max_radius))
    new_thread.start()


def main(win):

    running = True
    win.fill(BLACK)

    while (running):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if pygame.mouse.get_pressed()[0]:
                mouse_pos = list(pygame.mouse.get_pos())
                max_radius = random.randint(200, 550)

                spawn_wave(win, mouse_pos, max_radius)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    win.fill(BLACK)

        pygame.display.update()

window.fill((255, 255, 255))

main(window)

pygame.quit()
