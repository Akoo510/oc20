import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

background = BLUE

key_dict = {K_k:BLACK, K_r:RED, K_b:BLUE, K_y:YELLOW, K_g:GREEN}

pygame.init()

screen = pygame.display.set_mode((640,480))
screen.fill(background)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            print(event)
            if event.key in key_dict:
                background = key_dict[event.key]
            
                
            screen.fill(background)
            pygame.display.update()


pygame.quit()