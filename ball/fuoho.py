import pygame
from pygame.locals import *

size = 640, 280
width, height = size
GREEN = (150, 255, 150)
RED = (255,0, 0)
CYAN = (0, 150, 150)
background = (CYAN)

running = True
pygame.init()
screen = pygame.display.set_mode(size)
screen.fill(background)

pygame.draw.rect(screen, RED, (50, 20, 120, 100))
pygame.draw.rect(screen, GREEN, (150, 150, 220, 100),10)
pygame.draw.rect(screen, RED, (50, 20, 120, 100))
pygame.draw.rect(screen, GREEN, (100, 60, 120, 100))
pygame.draw.rect(screen, BLUE, (150, 100, 120, 100))
pygame.draw.rect(screen, RED, (350, 20, 120, 100), 1)
pygame.draw.rect(screen, GREEN, (400, 60, 120, 100), 4)
pygame.draw.rect(screen, BLUE, (450, 100, 120, 100), 8)
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False