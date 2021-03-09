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
    K_y:YELLOW, K_n:CYAN, K_m:MAGENTA, K_w:WHITE, K_q:GRAY}

size = 1000, 600
start = (0, 0)
size1 = (0, 0)
drawing = False
rect_list = []
rect = Rect(50, 60, 200, 80)
moving = False
moving1 = False
points = []
width, height = size
hat = drawing
color = RED
type_ ='r'
shapes = []
width1 = 1


pygame.init()

#########################################################################

class Rectangle:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.width = 2
        self.color = BLACK
        
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, self.width)
        
        
objects = [
    Rectangle(0, 5, 30, 30),
    Rectangle(0, 35, 30, 30),
    Rectangle(0, 65, 30, 30),
    Rectangle(0, 95, 30, 30),
    Rectangle(0, 125, 30, 30)]

class Shape:
    def __init__(self, rect, color=RED, width1=1, type_ = 'r'):
        self.rect = rect
        self.color = color
        self.width = width1
        self.type = type_
        
    def draw(self):
        if self.type == 'r':
            pygame.draw.rect(screen, self.color, self.rect, self.width)
        elif self.type == 'e':
            pygame.draw.ellipse(screen, self.color, self.rect, self.width)
            
#  sers pour l'image, à remettre dans boucle si possible

# if 'Oui' == answer:
#     img0 = pygame.image.load("ball.gif")
#     img0.convert()
#     rect0 = img0.get_rect()
#     pygame.draw.rect(img0, GREEN, rect0, 1)
#     
#     center = size[0]/2, size[1]/2
#     img = img0
#     rect = img.get_rect()
#     rect.center = center
#     
#     angle = 0
#     scale = 1
#     
#     mouse = pygame.mouse.get_pos()


img1 = pygame.image.load("ball.gif")
img1.convert()
img1 = pygame.transform.scale(img1, (25, 25))
rect1 = img1.get_rect()
rect1.center = 15, 110

move = pygame.image.load("move2.png")
move.convert_alpha()
move = pygame.transform.scale(move, (45, 45))
rect = move.get_rect()
rect.center = 15, 140

tool = 0

    
background = GRAY
screen = pygame.display.set_mode(size)
running = True
dessine_rectangle = False
dessine_cercle = False
dessine_ligne = False
bouge_forme = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False    
        if event.type == MOUSEBUTTONDOWN:
            i = 0
            for obj in objects:
                if obj.rect.collidepoint(event.pos):
                    print(obj)
                    obj.width = 0
                    tool = i
                else:
                    if tool != i:
                        obj.width = 2
                i += 1
            print('tool =', tool)
                    
                    
        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]
            if 'Oui' == answer2:   
                if event.key == K_ESCAPE:
                    if len(points) > 0:
                        points.pop()
        
        while dessine_rectangle or dessine_cercle:
            if event.type == KEYDOWN:
                if event.mod & KMOD_ALT:
                    if event.key == K_0:
                        width1 = 0
                    elif event.key == K_1:
                        width1 = 1
                    elif event.key == K_2:
                        width1 = 3
            
                elif event.key == K_r:
                    color = RED
                elif event.key == K_g:
                    color = GREEN
                elif event.key == K_b:
                    color = BLUE
                elif event.key == K_e:
                    type_ = 'e'
                elif event.key == K_f:
                    type_ = 'r'
                
                shapes[-1].width = width1
                shapes[-1].color = color
                shapes[-1].type = type_
            
            elif event.type == MOUSEBUTTONDOWN:
                start = event.pos
                s = Shape(Rect(start, (0, 0)), color, width1)
                shapes.append(s)
                drawing = True
            
            elif event.type == MOUSEBUTTONUP:
                drawing = False

            elif event.type == MOUSEMOTION and drawing:
                end = event.pos
                size = end[0]-start[0], end[1]-start[1]
                shapes[-1].rect.size = size
        
# pour image, à revoir

#         if 'Oui' == answer:
#             if event.type == KEYDOWN:  
#                 if event.key == K_a:
#                     if event.mod & KMOD_SHIFT:
#                         angle -= 10
#                     else:
#                         angle += 10
#                     img = pygame.transform.rotozoom(img0, angle, scale)
# 
#                 elif event.key == K_s:
#                     if event.mod & KMOD_SHIFT:
#                         scale /= 1.1
#                     else:
#                         scale *= 1.1
#                     img = pygame.transform.rotozoom(img0, angle, scale)
# 
#                 elif event.key == K_o:
#                     img = img0
#                     angle = 0
#                     scale = 1
# 
#                 elif event.key == K_h:
#                     img = pygame.transform.flip(img, True, False)
#             
#                 elif event.key == K_v:
#                     img = pygame.transform.flip(img, False, True)
# 
#                 elif event.key == K_l:
#                     img = pygame.transform.laplacian(img)
# 
#                 elif event.key == K_2:
#                     img = pygame.transform.scale2x(img)
# 
#                 rect = img.get_rect()
#                 rect.center = center
#             elif event.type == MOUSEBUTTONDOWN:
#                 if rect.collidepoint(event.pos):
#                     moving1 = True
#             elif event.type == MOUSEBUTTONUP:
#                 moving1 = False
#             elif event.type == MOUSEMOTION and moving1:
#                 rect.move_ip(event.rel)
#              
#         while dessine_rectangle or dessine_cercle:        
#             if event.type == MOUSEBUTTONDOWN:
#                 points.append(event.pos)
#                 if 'Oui' == answer3:    
#                     start = event.pos
#                     size1 = 0, 0
#                     drawing = True
#                     if 'Oui' == answer4:    
#                         if rect.collidepoint(event.pos):
#                             moving = True
                        
        
        while dessine_rectangle or dessine_cercle or bouge_forme:   
            if event.type == MOUSEBUTTONUP:
                end = event.pos
                while dessine_rectangle:   
                    size1 = end[0] - start[0], end[1] - start[1]
                    rect = pygame.Rect(start, size1)
                    rect_list.append(rect)
                    drawing = False
                while bouge_forme:
                    moving = False
                        
     
     # Si l'on veut dessiner des rectangles, remplacer le "moving" par "drawing"
        while dessine_rectangle:
            while bouge_forme:
                hat = moving
            else:
                hat = drawing
            if event.type == MOUSEMOTION and hat:
                points[-1] = event.pos
                while bouge_forme:
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

        
        
    screen.fill(GRAY)
    
    for obj in objects:
        obj.draw()
    pygame.draw.rect(screen, WHITE, (4, 10, 20, 20), 2)
    pygame.draw.ellipse(screen, WHITE, (4, 40, 20, 20), 2)
    pygame.draw.line(screen, WHITE, (4, 70), (24, 90), 2)
    screen.blit(move, rect)
    screen.blit(img1, rect1)

    while dessine_rectangle:
        pygame.draw.rect(screen, RED, (50, 50, 30, 30), 3)
    for s in shapes:
            s.draw()    
    while dessine_rectangle:
        if len(points)>1:
            rect = pygame.draw.lines(screen, RED, True, points, 3)
            pygame.draw.rect(screen, GREEN, rect, 1)

    #Dessiner un rectangle autour de l'image et la faire apparaître.        
#  image, à revoir

#     if 'Oui' == answer:
#         screen.blit(img, rect)
#         pygame.draw.rect(screen, RED, rect, 1)  
    while bouge_forme:     
        pygame.draw.rect(screen, RED, rect)
        if moving:
            pygame.draw.rect(screen, BLUE, rect, 4)
        pygame.display.flip()
    pygame.display.update()

pygame.quit()