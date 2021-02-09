import pygame
from pygame.locals import *

SIZE = 500, 500
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode(SIZE)

img0 = pygame.image.load(path)
img0.convert()

rect0 = img0.get_rect()
pygame.draw.rect(img0, GREEN, rect0, 1)

img = pygame.image.load('bird.png')
img.convert()

center = 250, 250
img = img0
rect = img.get_rect()
rect.center = center

angle = 0
scale = 1

running = True
moving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key = K_r:
                if event.mod and KMOD_SHIFT:
                    
    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect, 2)
    screen.blit(img, rect)
    pygame.display.flip()
    
pygame.quit()