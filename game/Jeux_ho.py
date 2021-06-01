import pygame, sys, os
from pygame.locals import *
import random

pygame.init()

CLOCK = pygame.time.Clock()

W = 700
H = 550
x = 50
y = 440
width = 40
height = 60
vel = 5
FPS = 90
i = 0
frame = 0

x_speed, y_speed = 5, 4

other_rect = pygame.Rect(300, 600, 200, 100)
other_speed = 2

player_pos = [130, 275, 420]
number = 1
fire_sound = pygame.mixer.Sound("Sound_effect/Gunshot.wav")

pygame.display.set_caption("Alien Defense")
pygame.display.set_icon(pygame.image.load("Icone.png"))
screen = pygame.display.set_mode((W, H))
background = pygame.image.load("background.png").convert_alpha()
z = 0
# Ennemy : Mecha
# mecha_walk = [pygame.image.load('Mecha_img/Mecha_walk_01.png'),
#               pygame.image.load('Mecha_img/Mecha_walk_02.png'),
#               pygame.image.load('Mecha_img/Mecha_walk_03.png'),
#               pygame.image.load('Mecha_img/Mecha_walk_04.png'),
#               pygame.image.load('Mecha_img/Mecha_walk_05.png'),
#               pygame.image.load('Mecha_img/Mecha_walk_06.png'),
#               pygame.image.load('Mecha_img/Mecha_walk_07.png'),
#               pygame.image.load('Mecha_img/Mecha_walk_08.png')
#               ]

# Ennemy : Gunman
# gunman_walk = [pygame.image.load('Gunman_img/Gunman_img_01.png'),
#               pygame.image.load('Gunman_img/Gunman_img_02.png'),
#               pygame.image.load('Gunman_img/Gunman_img_03.png'),
#               pygame.image.load('Gunman_img/Gunman_img_04.png'),
#               pygame.image.load('Gunman_img/Gunman_img_05.png'),
#               pygame.image.load('Gunman_img/Gunman_img_06.png'),
#               pygame.image.load('Gunman_img/Gunman_img_07.png'),
#               pygame.image.load('Gunman_img/Gunman_img_08.png')
#               ]

# Ennemy : Cyborg
# cyborg_walk = [pygame.image.load('Cyborg_img/Cyborg_img_01.png'),
#               pygame.image.load('Cyborg_img/Cyborg_img_02.png'),
#               pygame.image.load('Cyborg_img/Cyborg_img_03.png'),
#               pygame.image.load('Cyborg_img/Cyborg_img_04.png'),
#               pygame.image.load('Cyborg_img/Cyborg_img_05.png'),
#               pygame.image.load('Cyborg_img/Cyborg_img_06.png'),
#               pygame.image.load('Cyborg_img/Cyborg_img_07.png'),
#               pygame.image.load('Cyborg_img/Cyborg_img_08.png'),
#               pygame.image.load('Cyborg_img/Cyborg_img_09.png')
#               ]

def load_images(folder):
    """return a list of images in the specified folder"""
    files = os.listdir(folder)
    files.sort()
    images = []
    for file in files:
        img = pygame.image.load(folder + '/' + file)
        images.append(img)
    return images

mecha_walk = load_images('Mecha_img')
gunman_walk = load_images('Gunman_img')
cyborg_walk = load_images('Cyborg_img')


# Class

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.sprites = load_images('Player_img')
#         self.sprites.append(pygame.image.load('Player_img/Player1.png'))
#         self.sprites.append(pygame.image.load('Player_img/Player2.png'))
#         self.sprites.append(pygame.image.load('Player_img/Player3.png'))
#         self.sprites.append(pygame.image.load('Player_img/Player4.png'))
#         self.sprites.append(pygame.image.load('Player_img/Player5.png'))
#         self.sprites.append(pygame.image.load('Player_img/Player6.png'))
#         self.sprites.append(pygame.image.load('Player_img/Player7.png'))
#         self.sprites.append(pygame.image.load('Player_img/Player8.png'))
#         self.current_sprite = 0
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        #self.hitbox = (self.pos_x + 20, self.pos_y, 28, 60)
        self.i = 0
        
    def update(self):
#         self.current_sprite += 0.1
#         
#         if self.current_sprite >= len(self.sprites):
#             self.current_sprite = 0
#         
#         self.image = self.sprites[int(self.current_sprite)]
        if frame % 10 == 0:
            self.i = (self.i + 1) % len(self.sprites)
            self.image = self.sprites[self.i]
        
        
    
class Ennemi(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.stepIndex = 0
        
    def step(self):
        if self.stepIndex >= 80:
            self.stepIndex = 0

class Mecha(Ennemi):
    def __init__(self, x, y):
        Ennemi.__init__(self, x, y)
        self.sprites = load_images('Mecha_img')
        self.pv = 200
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.i = 0
        self.speed = [-1, 0]
        
    def update(self):
        if frame % 10 == 0:
            self.i = (self.i + 1) % len(self.sprites)
            self.image = self.sprites[self.i]
                 
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.move_ip(self.speed)
   
        
class Gunman(Ennemi):
    def __init__(self, x, y):
        Ennemi.__init__(self, x, y)
        self.pv = 50
        self.moving_rect = pygame.Rect(self.x, self.y, 60, 60)
        self.x_speed = 1
        self.y_speed = 2

    def draw(self, screen):
        global x_speed, y_speed
        self.step()
        screen.blit(gunman_walk[self.stepIndex // 10], (self.x, self.y))
        self.stepIndex += 1
        self.moving_rect.x += self.x_speed
        self.moving_rect.y += self.y_speed
        pygame.draw.rect(screen, (255, 255, 255), self.moving_rect)
        if self.moving_rect.right >= W or self.moving_rect.left <= 0:
            self.x_speed *= -1
        if self.moving_rect.bottom >= H or self.moving_rect.top <= 0:
            self.y_speed *= -1
        
    def move(self):
        self.x -= 0.6
        
class Cyborg(Ennemi):
    def __init__(self, x, y):
        Ennemi.__init__(self, x, y)
        self.pv = 100
        
    def draw(self, screen):
        self.step()
        screen.blit(cyborg_walk[self.stepIndex // 10], (self.x, self.y))
        self.stepIndex += 1
        
    def move(self):
        self.x -= 0.3
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos=(100, 300)):
        pygame.sprite.Sprite.__init__(self)
        self.speed = [3, 0]
        self.img = pygame.image.load('Bullet_img/Bullet_img_02.png')
        self.rect = self.img.get_rect()
        self.rect.center = pos
        self.damage = 25
        
    def move(self):
        self.rect.move_ip(self.speed)
        if self.rect.colliderect(mechas[0].rect):
            mechas.pop()
        
group = pygame.sprite.Group()

# Sprites
        
moving_sprites = pygame.sprite.Group()
player = Player(50, player_pos[number])
moving_sprites.add(player)

# Instances
mechas = []
gunmans = []
cyborgs = []
bullets = []

# Loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            if event.key == K_w:
                player.rect.move_ip(0, -120)
            elif event.key == K_s:
                player.rect.move_ip(0, 120)
#             elif event.key == K_d:
#                 player.rect.move_ip(120, 0)    
#             elif event.key == K_a:
#                 player.rect.move_ip(-120, 0)
                
            elif event.key == K_f:
                fire_sound.play()
                group.add(Bullet(player.rect.center))
            
            elif event.key == K_k:
                mechas.pop()

#             if event.key == K_w:
#                 if number < 2:
#                     number += 1
#                 if number == 2:
#                     number = 2
#                     
#             if event.key == K_s:
#                 if number > 0:
#                     number -=1
#                 if number == 0:
#                     number = 0
    
    rel_z = z % background.get_rect().width
    screen.blit(background, (rel_z - background.get_rect().width, 0))
    if rel_z < W:
        screen.blit(background, (rel_z, 0))
    z -= 1
    
#     key = pygame.key.get_pressed()
#     if key[K_f]:
#         fire_sound.play(loops=0)
#         group.add(Bullet())
#         continue

    for bullet in group.sprites():
        bullet.move()
        screen.blit(bullet.img,bullet.rect)
        
    # Mecha
    if len(mechas) == 0:
        mecha = Mecha(570, random.choice([130, 260, 420]))
        mechas.append(mecha)
        
    for mecha in mechas:
        mecha.move()
        
    #if mecha.off_screen():
        #mechas.remove(mecha)
        
    # Gunman
    if len(gunmans) == 0:
        gunman = Gunman(570, random.choice([130, 260, 420]))
        gunmans.append(gunman)
        
    for gunman in gunmans:
        gunman.move()
        
    # Cyborg
    if len(cyborgs) == 0:
        cyborg = Cyborg(570, random.choice([130, 260, 420]))
        cyborgs.append(cyborg)
        
    for cyborg in cyborgs:
        cyborg.move()
        
    # Draw
    for mecha in mechas:
        mecha.draw(screen)
        
    for gunman in gunmans:
        gunman.draw(screen)
        
    for cyborg in cyborgs:
        cyborg.draw(screen)

    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    CLOCK.tick(FPS)
    frame += 1