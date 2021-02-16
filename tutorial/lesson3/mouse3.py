"""Place multiple rectangles with the mouse."""

import pygame
from pygame.locals import *

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (127, 127, 127)

pygame.init()
screen = pygame.display.set_mode((640, 240))

start = (0, 0)
size = (0, 0)
drawing = False
shape_list = []

class Shape:
    def __init__(self, rect, color = RED, width = 1):
        self.rect = rect
        self.color = color
        self.width = width

current_shape = Shape(pygame.Rect(10, 10, 100, 50))

print('rect =', current_shape.rect)
print('couleur =', current_shape.color)
print('épaisseur =', current_shape
      .width)

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        if event.type == KEYDOWN:
            if event.key == K_0:
                current_shape.width = 0
            if event.key == K_1:
                current_shape.width = 1
            if event.key == K_2:
                current_shape.width = 3
                
            if event.key == K_r:
                current_shape.color = RED
            if event.key == K_g:
                current_shape.color = GREEN
            if event.key == K_b:
                current_shape.color = BLUE

        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            size = 0, 0
            drawing = True
            current_shape = Shape(pygame.Rect(start, size))
            
        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            size = end[0]-start[0], end[1]-start[1]
            rect = pygame.Rect(start, size)
            
            current_shape.rect = rect
            
            
            shape_list.append(current_shape)
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0]-start[0], end[1]-start[1]

    screen.fill(GRAY)
    for s in shape_list:
        pygame.draw.rect(screen, s.color, s.rect, s.width)
    pygame.draw.rect(screen, BLUE, current_shape.rect, current_shape.width)
    pygame.display.update()

pygame.quit()