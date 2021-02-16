import pygame
from pygame.locals import *
import time
 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

pygame.init()
screen = pygame.display.set_mode((640, 240))

running = True
background = GRAY

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
      
      
    screen.fill(background)
    pygame.display.update()

pygame.quit()