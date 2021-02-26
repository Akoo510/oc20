import pygame
from pygame.locals import *
from rect import *
pygame.init()

size = (500, 500)

screen = pygame.display.set_mode(size)

background = (50, 50, 50)
screen.fill(background)
running = True
moving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        x,y = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
                
        elif event.type == MOUSEBUTTONUP:
            moving = False
            
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
  
pygame.display.update()
print (x,y)
pygame.quit()