import pygame
import math, random, sys
from pygame.locals import *

i = 0

W, H = 1000,1000
HW, HH = W/2, H/2
AREA = W*H

CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Sprite Sheets - Akoo")
FPS = 5

BLACK = (0, 0,0)
WHITE = (255, 255, 255)

class spritesheet:
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

s = spritesheet("GreenPlayerRun.png", 8, 1)

CENTER_HANDLE = 4



def principal():
    pygame.init()
    #pygame.mixer.init()
    screen = pygame.display.set_mode((1000, 1000))
    # pygame.mixer.music.load('nom')
    # pygame.mixer.music.set_volume(0.2)
    # pygame.mixer.music.play(loops=-1)
    # tir_sound=pygame.mixer.Sound('son')
    # tir_sound.set_volume(0.2)

    background = pygame.image.load('background.png')
    background_pos = background.get_rect()

    pygame.display.set_caption('nom')
    group = pygame.sprite.Group()
    
    running = True
    
    Index = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            s.draw(DS, Index % s.totalCellCount, HW, HH, CENTER_HANDLE)
            Index += 1
        
        
            pygame.display.update()
            CLOCK.tick(FPS)    
        
        player = s
        
        player_pos = s.sheet.get_rect().center = 40,150
        screen.blit(background, player_pos)
        
#         rapido = pygame.image.load('rapido.png')
#         rapido_pos = rapido.get_rect()
#         screen.blit(rapido, rapido_pos)
#         
#         tankos = pygame.image.load('tankos.png')
#         tankos_pos = tankos.get_rect()
#         screen.blit(tankos, tankos_pos)
#         
#         ff = pygame.image.load('ff.png')
#         ff_pos = ff.get_rect()
#         screen.blit(ff, ff_pos)
                
         screen.blit(background, background_pos)
        
        key = pygame.key.get_pressed()
        if key[K_f]:
            #fire_sound.play(loops=0)
            group.add(Projectile())
            continue
        
        for projectile in group.sprites():
            projectile.move()
            screen.blt(projectile.img, projectile.rect)
        pygame.display.flip()
        pygame.time.Clock().tick(60)
    
class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        position = [122, 185]
        speed = [3, 0]
        self.img = pygame.image.load('nom')
        self.rect = self.img.get_rect()
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)

principal()