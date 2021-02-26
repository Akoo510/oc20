import pygame
from pygame.locals import *
from rect import *

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

key_dict = {K_k:BLACK, K_o:RED, K_g:GREEN, K_b:BLUE,
    K_y:YELLOW, K_a:CYAN, K_m:MAGENTA, K_w:WHITE, K_q:GRAY}

size = 640, 320

rect = Rect(50, 60, 200, 80)
moving = False

background = GRAY
screen = pygame.display.set_mode(size)
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        if event.type == KEYDOWN:
            if event.key == K_r:
                if event.type == MOUSEBUTTONDOWN:
                    if rect.collidepoint(event.pos):
                        moving = True
                elif event.type == MOUSEBUTTONUP:
                    moving = False
                elif event.type == MOUSEMOTION and moving:
                    rect.move_ip(event.rel)
                pygame.draw.rect(screen, RED, rect)
                if moving:
                    pygame.draw.rect(screen, BLUE, rect, 4)
                
            
            
            

    
    pygame.display.flip()        
    screen.fill(background)
    pygame.display.update()

pygame.quit()