import pygame
import math, sys, os
from pygame.locals import *
from rect import *

# = Charger une image
## = Créer des polygones
### Créer des rectangles
#### Déplacer des rectangles

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,
    K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE, K_q:GRAY}

size = 640, 320
start = (0, 0)
size1 = (0, 0)
drawing = False
rect_list = []
rect = Rect(50, 60, 200, 80)
moving = False
points = []
width, height = size
hat = drawing

pygame.init()

#Ici, nous avons la possibilité de charger une image ainsi que de lui attribuer une vitesse.

answer = input('Voulez-vous utiliser un image ? (Oui/Non) : ')
if 'Oui' != answer:
    answer2 = input('Voulez-vous créer des polygones / rectangles ? (Oui/Non) : ')
    answer3 = input('Voulez-vous créer des rectangles ? (Oui/Non) : ')
    if 'Oui' == answer3:
        answer4 = input('Voulez-vous déplacer des rectangles ? (Oui/Non) : ')
    else:
        answer4 = 'Non'
else:
    answer2 = 'Non'
    answer3 = 'Non'
    answer4 = 'Non'

if 'Oui' == answer:
    img0 = pygame.image.load("ball.gif")
    img0.convert()
    rect0 = img0.get_rect()
    pygame.draw.rect(img0, GREEN, rect0, 1)
    
    center = 640/2, 320/2
    img = img0
    rect = img.get_rect()
    rect.center = center
    
    angle = 0
    scale = 1

    mouse = pygame.mouse.get_pos()

    

background = GRAY
screen = pygame.display.set_mode(size)
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]
            if 'Oui' == answer2:   
                if event.key == K_ESCAPE:
                    if len(points) > 0:
                        points.pop()
        
        if 'Oui' == answer:
          if event.type == KEYDOWN:  
            if event.key == K_r:
                if event.mod & KMOD_SHIFT:
                    angle -= 10
                else:
                    angle += 10
                img = pygame.transform.rotozoom(img0, angle, scale)

            elif event.key == K_s:
                if event.mod & KMOD_SHIFT:
                    scale /= 1.1
                else:
                    scale *= 1.1
                img = pygame.transform.rotozoom(img0, angle, scale)

            elif event.key == K_o:
                img = img0
                angle = 0
                scale = 1

            elif event.key == K_h:
                img = pygame.transform.flip(img, True, False)
            
            elif event.key == K_v:
                img = pygame.transform.flip(img, False, True)

            elif event.key == K_l:
                img = pygame.transform.laplacian(img)

            elif event.key == K_2:
                img = pygame.transform.scale2x(img)

            rect = img.get_rect()
            rect.center = center
            
        if 'Oui' == answer:
            if event.type == MOUSEMOTION:
                mouse = event.pos
                x = mouse[0] - center[0]
                y = mouse[1] - center[1]
                d = math.sqrt(x ** 2 + y ** 2)

                angle = math.degrees(-math.atan2(y, x))
                scale = abs(5 * d / 240)
                img = pygame.transform.rotozoom(img0, angle, scale)
                rect = img.get_rect()
                rect.center = center
            
        
        if 'Oui' == answer2:        
            if event.type == MOUSEBUTTONDOWN:
                points.append(event.pos)
                if 'Oui' == answer3:    
                    start = event.pos
                    size1 = 0, 0
                    drawing = True
                    if 'Oui' == answer4:    
                        if rect.collidepoint(event.pos):
                            moving = True
        
        if 'Oui' == answer2:    
            if event.type == MOUSEBUTTONUP:
                end = event.pos
                if 'Oui' == answer3 and 'Non' == answer4:     
                    size1 = end[0] - start[0], end[1] - start[1]
                    rect = pygame.Rect(start, size1)
                    rect_list.append(rect)
                    drawing = False
                    if 'Oui' == answer4:    
                        moving = False
     
     # Si l'on veut dessiner des rectangles, remplacer le "moving" par "drawing"
        if 'Oui' == answer2:    
            if 'Oui' == answer3 and answer4 :
                hat = moving
            else:
                hat = drawing
            if event.type == MOUSEMOTION and hat:
                points[-1] = event.pos
                if 'Oui' == answer3:     
                    end = event.pos
                    size1 = end[0] - start[0], end[1] - start[1]
                    rect.move_ip(event.rel)    
    
    #Vitesse de l'image
#     if 'Oui' == answer:
#         rect = rect.move(speed)
#         if rect.left < 0 or rect.right > width:
#             speed[0] = -speed[0]
#         if rect.top < 0 or rect.bottom > height:
#             speed[1] = -speed[1]

        
        
    screen.fill(background)
    if 'Oui' == answer2 and 'Non' == answer3:    
        if len(points)>1:
            rect = pygame.draw.lines(screen, RED, True, points, 3)
            pygame.draw.rect(screen, GREEN, rect, 1)
    if 'Oui' == answer3:     
        for rect in rect_list:
            pygame.draw.rect(screen, RED, rect, 3)
        pygame.draw.rect(screen, RED, (start, size1), 1)
    #Dessiner un rectangle autour de l'image et la faire apparaître.        
    if 'Oui' == answer:
        screen.blit(img, rect)
        pygame.draw.rect(screen, RED, rect, 1)
        pygame.draw.line(screen, GREEN, center, mouse, 1)
        pygame.draw.circle(screen, RED, center, 6, 1)
        pygame.draw.circle(screen, RED, mouse, 6, 1)   
    if 'Oui' == answer4:     
        pygame.draw.rect(screen, RED, rect)
        if moving:
            pygame.draw.rect(screen, BLUE, rect, 4)
        pygame.display.flip()
    pygame.display.update()

pygame.quit()