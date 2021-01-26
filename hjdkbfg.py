"""Place a rectangle with the mouse."""

# 1) ajouter un KEYDOWN : RGM -> change color
# 2) ajouter KEYDOWN : 01234 -> change épaisseur

import pygame
from pygame.locals import *

RED = (255, 0, 0)
GRAY = (127, 127, 127)
WHITE = (150,150, 150)
GREEN = (0, 150, 150)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

coulor = WHITE
thickness = 2

key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,
    K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}

key_dict2 = {K_0:0, K_1:1, K_2:2, K_3:3, K_4:4}

pygame.init()
screen = pygame.display.set_mode((640, 240))

start = (0, 0)
size = (0, 0)
drawing = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            size = 0, 0
            drawing = True
            
        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
        
        elif event.type == KEYDOWN:
            if event.key in key_dict:
                coulor = key_dict[event.key]
            if event.key in key_dict2:
                thickness = key_dict2[event.key]
            

    screen.fill(WHITE)
    pygame.draw.rect(screen, coulor, (start, size), thickness)
    pygame.display.update()

pygame.quit()