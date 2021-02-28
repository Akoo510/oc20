import pygame
from pygame.locals import *

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (127, 127, 127)

pygame.init()
screen = pygame.display.set_mode((640, 240))

start = (0, 0)
size = (0, 0)
drawing = False
color = RED
width = 1
type_ = 'r'
shapes = []

# définir une classe de formes (shape) avec rectangle, couleur, épaisseur
# type_ 'r' = rectangle, type_ 'e' = elipse
class Shape:
    def __init__(self, rect, color=RED, width=1, type_ = 'r'):
        self.rect = rect
        self.color = color
        self.width = width
        self.type = type_
        
    def draw(self):
        if self.type == 'r':
            pygame.draw.rect(screen, self.color, self.rect, self.width)
        elif self.type == 'e':
            pygame.draw.ellipse(screen, self.color, self.rect, self.width)

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_0:
                width = 0
            elif event.key == K_1:
                width = 1
            elif event.key == K_2:
                width = 3
        
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
            
            shapes[-1].width = width
            shapes[-1].color = color
            shapes[-1].type = type_
            
        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            s = Shape(Rect(start, (0, 0)), color, width)
            shapes.append(s)
            drawing = True
            
        elif event.type == MOUSEBUTTONUP:
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0]-start[0], end[1]-start[1]
            shapes[-1].rect.size = size

    screen.fill(GRAY)
    for s in shapes:
        s.draw()    
    pygame.display.update()

pygame.quit()