import pygame
import math, sys, os
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
tool = 0
type_ = tool
shapes = []
width1 = 1
(Dx, Dy) = (0, 0)
(Fx, Fy) = (0, 0)

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
    Rectangle(0, 65, 30, 30)]

class Shape:
    def __init__(self, rect, color=RED, width1=1, type_ = 0, start_pos = (Dx, Dy), end_pos = (Fx, Fy)):
        self.rect = rect
        self.color = color
        self.width = width1
        self.type = type_
        self.start_pos = (Dx, Dy)
        self.end_pos = (Fx, Fy)
        self.tool = None
        
    def draw(self):
        if self.tool == 0:
            pygame.draw.rect(screen, self.color, self.rect, self.width)
        elif self.tool == 1:
            pygame.draw.ellipse(screen, self.color, self.rect, self.width)
        elif self.tool == 2:
            pygame.draw.line(screen, self.color, self.start_pos, self.rect.bottomright, self.width)

# # image
answer = input('Voulez-vous utiliser des images (Oui / Non) ? ')

if 'Oui' == answer:
    img0 = pygame.image.load("ball.gif")
    img0.convert()
    rect0 = img0.get_rect()
    pygame.draw.rect(img0, GREEN, rect0, 1)
    
    center = size[0]/2, size[1]/2
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
<<<<<<< HEAD
        if event.type == MOUSEBUTTONDOWN:
            for obj in objects:
                if obj.rect.collidepoint(event.pos):
                    print(obj)
                    obj.width = 0
#                 if not obj.rect.collidepoint(event.pos):
#                     obj.width = 2
                    
        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]
            if 'Oui' == answer2:   
                if event.key == K_ESCAPE:
                    if len(points) > 0:
                        points.pop()
=======
>>>>>>> d325c852f7208103a2c18d42a9936ee3cd6b0725
        
        if answer != 'Oui':    
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
        if answer != 'Oui':            
            if event.type == KEYDOWN:
                if event.key in key_dict:
                    background = key_dict[event.key]
                if event.key == K_BACKSPACE:
                    shapes.pop()
              
        if answer != 'Oui':
            if tool == 1 or tool == 0 or tool == 2:
                if event.type == KEYDOWN:
                    if event.mod & KMOD_ALT:
                        if event.key == K_0:
                            width1 = 0
                        elif event.key == K_1:
                            width1 = 1
                        elif event.key == K_2:
                            width1 = 3
                        elif event.key == K_3:
                            width1 = 5
                        elif event.key == K_4:
                            width1 = 7
                
                    if event.key == K_r:
                        color = RED
                    elif event.key == K_g:
                        color = GREEN
                    elif event.key == K_b:
                        color = BLUE
                    elif event.key == K_k:
                        color = BLACK
                    elif event.key == K_y:
                        color = YELLOW
                    elif event.key == K_n:
                        color = CYAN
                    elif event.key == K_m:
                        color = MAGENTA
                    elif event.key == K_w:
                        color = WHITE
                    elif event.key == K_q:
                        color = GRAY
                    
                    shapes[-1].width = width1
                    shapes[-1].color = color
                    shapes[-1].type = type_
                
                elif event.type == MOUSEBUTTONDOWN:
                    start = event.pos
                    (Dx, Dy) = pygame.mouse.get_pos()
                    s = Shape(Rect(start, (0, 0)), color, width1)
                    s.tool = tool
                    shapes.append(s)
                    drawing = True
                
                elif event.type == MOUSEBUTTONUP:
                    drawing = False

                elif event.type == MOUSEMOTION and drawing:
                    end = event.pos
                    size = end[0]-start[0], end[1]-start[1]
                    shapes[-1].rect.size = size

        if 'Oui' == answer:
            if event.type == KEYDOWN:  
                if event.key == K_a:
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
            elif event.type == MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    moving1 = True
            elif event.type == MOUSEBUTTONUP:
                moving1 = False
            elif event.type == MOUSEMOTION and moving1:
                rect.move_ip(event.rel)
                        
        if answer != 'Oui':
            if tool == 0 or tool == 1:   
                if event.type == MOUSEBUTTONUP:
                    end = event.pos
                    if tool == 0:   
                        size1 = end[0] - start[0], end[1] - start[1]
                        rect = pygame.Rect(start, size1)
                        rect_list.append(rect)
                        drawing = False
        
        if answer != 'Oui':
            if tool == 0:
                hat = drawing
 
    screen.fill(GRAY)
    
    for obj in objects:
        obj.draw()
    pygame.draw.rect(screen, WHITE, (4, 10, 20, 20), 2)
    pygame.draw.ellipse(screen, WHITE, (4, 40, 20, 20), 2)
    pygame.draw.line(screen, WHITE, (4, 70), (24, 90), 2)

    for s in shapes[1:]:
            s.draw()

    if 'Oui' == answer:
        screen.blit(img, rect)
        pygame.draw.rect(screen, RED, rect, 1)  
    
    pygame.display.update()

pygame.quit()