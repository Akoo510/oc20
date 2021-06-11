import pygame, sys, os
from pygame.locals import *
import random

pygame.init()

CLOCK = pygame.time.Clock()

W = 700
H = 550
x = 50
y = 440
z = 0
width = 40
height = 60
vel = 5
FPS = 90
i = 0
frame = 0

x_speed, y_speed = 5, 4

other_rect = pygame.Rect(300, 600, 200, 100)
other_speed = 2

player_pos = [130, 285, 420]
number = 1

# Sound & Music

fire_sound = pygame.mixer.Sound("Sound_effect/Gunshot_2.mpeg")
pygame.mixer.music.load("Ambiant_music/Techno.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

# Setting Background & Icon

pygame.display.set_caption("Space Defense")
pygame.display.set_icon(pygame.image.load("Icone.png"))
screen = pygame.display.set_mode((W, H))
background = pygame.image.load("background.png").convert_alpha()

# Function to load images

def load_images(folder):
    """return a list of images in the specified folder"""
    files = os.listdir(folder)
    files.sort()
    images = []
    for file in files:
        img = pygame.image.load(folder + '/' + file)
        images.append(img)
    return images


# Ennemies
mecha_walk = load_images('Mecha_img')
gunman_walk = load_images('Gunman_img')
cyborg_walk = load_images('Cyborg_img')

# Class

# Player

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
        self.pv = 1000
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        #self.hitbox = (self.pos_x + 20, self.pos_y, 28, 60)
        self.i = 0
        
    def update(self):
        if frame % 10 == 0:
            self.i = (self.i + 1) % len(self.sprites)
            self.image = self.sprites[self.i]
#         self.current_sprite += 0.1
#         
#         if self.current_sprite >= len(self.sprites):
#             self.current_sprite = 0
#         
#         self.image = self.sprites[int(self.current_sprite)]


    
class Ennemi:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.stepIndex = 0
        
    def step(self):
        if self.stepIndex >= 80:
            self.stepIndex = 0

# Mecha

class Mecha(Ennemi):
    def __init__(self, x, y):
        Ennemi.__init__(self, x, y)
        self.sprites = load_images('Mecha_img')
        self.pv = 2000
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
#     def __init__(self, x, y):
#         Ennemi.__init__(self, x, y)
#         self.pv = 200
#         
#     def draw(self, screen):
#         self.step()
#         screen.blit(mecha_walk[self.stepIndex // 10], (self.x, self.y))
#         self.stepIndex += 1
#         
#     def move(self):
#         self.x -= 0.3

# Gunman

class Gunman(Ennemi):
    def __init__(self, x, y):
        Ennemi.__init__(self, x, y)
        self.sprites = load_images('Gunman_img')
        self.pv = 750
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
#     def __init__(self, x, y):
#         Ennemi.__init__(self, x, y)
#         self.pv = 50
#         self.moving_rect = pygame.Rect(self.x, self.y, 60, 60)
#         self.x_speed = 1
#         self.y_speed = 2
# 
#     def draw(self, screen):
#         global x_speed, y_speed
#         self.step()
#         screen.blit(gunman_walk[self.stepIndex // 10], (self.x, self.y))
#         self.stepIndex += 1
#         self.moving_rect.x += self.x_speed
#         self.moving_rect.y += self.y_speed
#         pygame.draw.rect(screen, (255, 255, 255), self.moving_rect)
#         if self.moving_rect.right >= W or self.moving_rect.left <= 0:
#             self.x_speed *= -1
#         if self.moving_rect.bottom >= H or self.moving_rect.top <= 0:
#             self.y_speed *= -1
#         
#     def move(self):
#         self.x -= 0.6

# Cyborg

class Cyborg(Ennemi):
    def __init__(self, x, y):
        Ennemi.__init__(self, x, y)
        self.sprites = load_images('Cyborg_img')
        self.pv = 1250
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
#     def __init__(self, x, y):
#         Ennemi.__init__(self, x, y)
#         self.pv = 100
#         
#     def draw(self, screen):
#         self.step()
#         screen.blit(cyborg_walk[self.stepIndex // 10], (self.x, self.y))
#         self.stepIndex += 1
#         
#     def move(self):
#         self.x -= 0.3
        
# Bullet

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos=(100, 300)):
        pygame.sprite.Sprite.__init__(self)
        speed=[3,0]
        self.img = pygame.image.load('Bullet_img/Bullet_img_02.png')
        self.rect = self.img.get_rect()
        self.rect.center = pos
        self.speed = speed
        self.damage = 250
        
    def move(self):
        self.rect.move_ip(self.speed)
        if self.rect.colliderect(mechas[0].rect):
            mechas.pop()
        elif self.rect.colliderect(gunmans[0].rect):
            gunmans.pop()
        elif self.rect.colliderect(cyborgs[0].rect):
            cyborgs.pop()
        
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
lane = 1

# Main Loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            if event.key == K_w:
                if lane == 1 or lane == 0: 
                    player.rect.move_ip(0, -140)
                    lane +=1
            elif event.key == K_s:
                if lane == 1 or lane == 2:
                    player.rect.move_ip(0, 140)
                    lane -=1
                    
                
            elif event.key == K_f:
                fire_sound.play()
                group.add(Bullet(player.rect.center))
    
    rel_z = z % background.get_rect().width
    screen.blit(background, (rel_z - background.get_rect().width, 0))
    if rel_z < W:
        screen.blit(background, (rel_z, 0))
    z -= 1

    for bullet in group.sprites():
        bullet.move()
        screen.blit(bullet.img,bullet.rect)
        
    # Mecha
    if len(mechas) == 1:
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