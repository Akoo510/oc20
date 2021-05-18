import pygame
import math, sys, os
from pygame.locals import *
import time

pygame.init()

W, H = 700, 550
HW, HH = W / 2, H / 2
PX, PY = 55, 300
AREA = W * H

CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Background animation + player")
FPS = 10

# Icône
pygame.display.set_icon(pygame.image.load("Icone.png"))


WHITE = (255, 255, 255)
RED = (255, 0, 0)


CENTER_HANDLE = 4

Index = 0

background = pygame.image.load("background.png").convert_alpha()
x = 0

class Spritesheet:
    def __init__(self, filename, cols, rows):
        self.filename = filename
        self.sheet = pygame.image.load(self.filename).convert_alpha()
        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols * rows
        
        self.rect = self.sheet.get_rect()
        w = self.cellWidth = int(self.rect.width / cols)
        h = self.cellHeight = int(self.rect.height / rows)
        hw,hh = self.cellCenter = (int(w / 2), int(h / 2))
        
        self.cells = list([(Index % cols * w, int(Index / cols) * h, w, h) for Index in range(self.totalCellCount)])
        self.handle = list([
            (0, 0), (-hw, 0), (-w, 0),
            (0, -hh), (-hw, -hh), (-w, -hh),
            (0, -h), (-hw, -h), (-w, -h),])
        
    def draw(self, surface, cellIndex, x, y, handle = 0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])
        

Player_PosY = list([
    (190), (305), (462)])

number = 1
    

s = Spritesheet("GreenPlayerRun.png", 8, 1)
b = Spritesheet("Ball.png", 3, 1)

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        position=[PX + 40,Player_PosY[number]]
        speed=[10,0]
        self.img=pygame.image.load('Ball.png')
        self.rect=self.img.get_rect()
        self.rect.center=position
        self.speed=speed
    def move(self):
        self.rect=self.rect.move(self.speed)
# Loop
group=pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            
            if event.key == K_s or event.key == K_DOWN:
                if number < 2:
                    number += 1
                if number == 2:
                    number = 2
            
            if event.key == K_w or event.key == K_UP:
                if number > 0:
                    number -= 1
                if number == 0:
                    number = 0
        
    rel_x = x % background.get_rect().width
    
    DS.blit(background, (rel_x - background.get_rect().width, 0))
    if rel_x < W:
        DS.blit(background, (rel_x, 0))
    x -= 10
    
    s.draw(DS, Index % s.totalCellCount, PX, Player_PosY[number], CENTER_HANDLE)
    Index += 1
    
    #b.draw(DS, Index % b.totalCellCount, PX, Player_PosY[number], CENTER_HANDLE)
    
    
    key=pygame.key.get_pressed()
    if key[K_f]:
        #fire_sound.play(loops=0)
        group.add(Bullet())
        continue
    

    for bullet in group.sprites():
        bullet.move()
        DS.blit(bullet.img,bullet.rect)
    
    pygame.display.update()
    CLOCK.tick(FPS)