import pygame
from pygame.locals import *

size = 7000, 600
width, height = size
GREEN = (150, 255, 150)
RED = (255,0, 0)
CYAN = (0, 150, 150)

pygame.init()
screen = pygame.display.set_mode(size)
running = True

ball = pygame.image.load('ball.gif')
rect = ball.get_rect()
speed = [100, 100]

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > height:
        speed[1] = -speed[1]
    
    screen.fill(CYAN)
    pygame.draw.rect(screen, RED, rect, 1)
    screen.blit(ball, rect)
    pygame.display.update()
            
pygame.quit()