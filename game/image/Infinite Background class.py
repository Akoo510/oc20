import pygame
import math, sys, os
from pygame.locals import *

W, H = 700, 550
HW, HH = W / 2, H / 2
AREA = W * H

pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Background animation")
FPS = 120

background = pygame.image.load("background.png").convert_alpha()
x = 0

# Loop

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
    rel_x = x % background.get_rect().width
    
    DS.blit(background, (rel_x - background.get_rect().width, 0))
    if rel_x < W:
        DS.blit(background, (rel_x, 0))
    x -= 1
    
    pygame.display.update()
    CLOCK.tick(FPS)