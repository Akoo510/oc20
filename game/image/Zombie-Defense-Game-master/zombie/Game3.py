import pygame
import sys
from pygame.locals import *
import random

i = 0

def principal():
    pygame.init()
    #pygame.mixer.init()
    screen = pygame.display.set_mode((800, 602))
    # pygame.mixer.music.load('nom')
    # pygame.mixer.music.set_volume(0.2)
    # pygame.mixer.music.play(loops=-1)
    # tir_sound=pygame.mixer.Sound('son')
    # tir_sound.set_volume(0.2)

    background = pygame.image.load('background.png')
    background_pos = background.get_rect()

    #pygame.display.set_caption('Plants Vs Zombies ! ')
    group = pygame.sprite.Group()

    while True:
        
        player = pygame.image.load('SnowPea.gif')
        player_pos = player.get_rect().center = 40,150
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
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
#                 
        screen.blit(background, background_pos)
        screen.blit(player, player_pos)
        
        key = pygame.key.get_pressed()
        if key[K_f]:
            #fire_sound.play(loops=0)
            group.add(Projectile())
            continue
        
        for projectile in group.sprites():
            projectile.move()
            screen.blit(projectile.img, projectile.rect)
        pygame.display.flip()
        pygame.time.Clock().tick(60)
    
class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        position = [100, 160]
        speed = [3, 0]
        self.img = pygame.image.load('SnowPeashooterBullet.gif')
        self.rect = self.img.get_rect()
        self.rect.center = position
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
        
principal()