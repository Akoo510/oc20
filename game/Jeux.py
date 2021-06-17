import pygame
import sys, os, time, random
from pygame.locals import *

pygame.init()   
score = 0
b = 0

# Source:
# https://pygame.readthedocs.io/en/latest/5_app/app.html

class Text:
    """The Text class creates a text objet. """

    def __init__(self, text='Text', pos=(0, 0), **options):
        self.pos = pos
        self.fontname = None
        self.fontsize = 18
        self.fontcolor = Color('black')
        self.set_font()
        self.set_text(text)

    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def set_pos(self, pos):
        self.pos = pos
        self.rect.topleft = pos

    def set_text(self, text):
        """render the text."""
        self.text = text
        self.image = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        Game.screen.blit(self.image, self.rect)      
    

class AnimatedSprite(pygame.sprite.Sprite):
    """The AnimatedSprite class creates an animated sprite. 
    The attributes are:
    - folder: containing image files in the correct order
    - images: a list of images
    - image: the current image
    - rect: the current rectangle (of the image)
    - speed: moving spped of the sprite
    - label: text label attached to sprite (eg. display life value)

    The Rect object has several virtual attributes 
    which can be used to move and align the Rect:
        x, y
        top, left, bottom, right
        topleft, bottomleft, topright, bottomright
        midtop, midleft, midbottom, midright
        center, centerx, centery
        size, width, height
        w, h
    Source: https://www.pygame.org/docs/ref/rect.html
    """

    def __init__(self, folder, pv=0):
        super().__init__()
        self.folder = folder
        self.load_images(folder)
        self.index = 0        # current index in the 'images' list
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.speed = [0, 0]   # moving speed of the sprite

        self.pv0 = pv   # original life value
        self.pv = pv    # current life value
        self.label = Text()
        self.label.rect = self.rect
        self.label.set_text(str(self.pv))  
        
        # advance animation every x frames
        self.animation_step = 5   

    def set_pv(self, pv):
        self.pv = pv      
        self.label.set_text(str(self.pv))

    def load_images(self, folder):
        # load images from a folder
        files = os.listdir(folder)
        files.sort()
        self.images = []
        for file in files:
            image = pygame.image.load(folder + '/' + file)
            self.images.append(image)
        
    def update(self):
        # updage the sprite animation every x steps
        if Game.frame % self.animation_step == 0:
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def move(self):
        # update the sprite position
        self.rect.move_ip(self.speed)

    def draw(self):
        # draw the sprite to the game screen
        Game.screen.blit(self.image, self.rect)
        Game.screen.blit(self.label.image, self.rect)

    def __str__(self):
        return f'AnimatedSprite size {self.rect.size} at {self.rect.topleft}'


class Player(AnimatedSprite):
    """The Player class creates a player which 
    - has a life value (pv=1000)
    - does know how to react to key events
        - W/S to move up/down
        - F to fire a bullet
    """

    def __init__(self, folder, pv=1000):
        super().__init__(folder, pv)
        self.lane = 1
        self.player_pos = [130, 285, 420]
        self.rect.x = 50 
        self.rect.y = self.player_pos[1]
        self.pv = pv

    def keydown(self, event):
        """The player knows how to react to keys."""
        if event.key == K_w or event.key == K_UP:
            if self.lane == 1 or self.lane == 0: 
                self.rect.move_ip(0, -140)
                self.lane +=1

        elif event.key == K_s or event.key == K_DOWN:
            if self.lane == 1 or self.lane == 2:
                self.rect.move_ip(0, 140)
                self.lane -=1

        elif event.key == K_f:
            Bullet.fire_sound.play()
            Bullet.bullets.add(Bullet(self.rect.center))


class Enemy(AnimatedSprite):
    """The Enemy class creates an enemy which:
    - starts at left border, in one of the 3 lanes
    - moves to the left
    - returns to the origin when reaching the left border
    """
    enemies = pygame.sprite.Group()

    def __init__(self, folder, pv=1000, speed = [-1, 0]):
        super().__init__(folder, pv)
        self.speed = speed
        self.set_init_pos()
        self.damage = 100

    def set_init_pos(self):
        self.set_pv(self.pv0)   # reset to original value
        self.rect.x = 1.2 * Game.W    # reset x position
        self.rect.y = random.choice([130, 260, 420])

    def move(self):
        # update the sprite position
        self.rect.move_ip(self.speed)

        # when reaching the left border, 
        # it returns to the original position
        if self.rect.x < -self.rect.width:
            self.set_init_pos()
            game.player.pv -= 100
            game.player.label.set_text(str(game.player.pv))

class Bullet(pygame.sprite.Sprite):
    """The Bullet class creates bullet objects, which
    - move to the right
    - disappear at the right border
    - disappear when hitting an enemy
    """
    fire_sound = pygame.mixer.Sound("Sound_effect/Gunshot_2.mpeg")
    impact_sound = pygame.mixer.Sound("Sound_effect/Impact")
    bullets = pygame.sprite.Group()

    def __init__(self, pos=(100, 300)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Bullet_img/Bullet_img_02.png')
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = [3, 0]
        self.damage = 250
        
    def move(self):
        global score
        global b
        self.rect.move_ip(self.speed)
        if self.rect.x > Game.W:
            Bullet.bullets.remove(self)

        for enemy in Enemy.enemies:
            if self.rect.colliderect(enemy.rect):
                Bullet.impact_sound.play()
                Bullet.bullets.remove(self)
                enemy.pv -= self.damage
                enemy.label.set_text(str(enemy.pv))
                if enemy.pv <= 0:
                    enemy.set_init_pos()
                    score += 100
                    b = 0


# Class documentation
print()
print(AnimatedSprite.__doc__)
print(Player.__doc__)
print(Enemy.__doc__)
print(Bullet.__doc__)

class Game:
    W = 700
    H = 550
    FPS = 60
    screen = pygame.display.set_mode((W, H))
    frame = 0

    def __init__(self):

        pygame.init()
        self.is_playing = False
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Space Defense")
        pygame.display.set_icon(pygame.image.load("Icone.png"))
        self.frame = 0
        self.z = 0
        self.stopping = False
        #banner
        self.banner = pygame.image.load('banner.png')
        self.banner = pygame.transform.scale(self.banner, (700, 550))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.x = 0
        self.banner_rect.y = 0
        #button play
        self.play_button = pygame.image.load('play_button.png')
        self.play_button = pygame.transform.scale(self.play_button, (100, 40))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = self.screen.get_width() / 2.45
        self.play_button_rect.y = self.screen.get_height() / 1.5
        #gameover
        self.gameover = pygame.image.load('Game_over.png')
        self.gameover = pygame.transform.scale(self.gameover, (700, 550))
        self.gameover_rect = self.gameover.get_rect()
        self.gameover_rect.x = 0
        self.gameover_rect.y = 0
        
        #music
        pygame.mixer.music.load(random.choice(["Ambiant_music/Techno.mp3", "Ambiant_music/Bass.flac", "Ambiant_music/Metalophone.wav", "Ambiant_music/Speed.mp3"]))
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

        self.background = pygame.image.load("background.png").convert_alpha()

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        self.player = Player('Player_img')

        Enemy.enemies.add(Enemy('Mecha_img', 1500))
        Enemy.enemies.add(Enemy('Gunman_img', 500, [-3, 0]))
        Enemy.enemies.add(Enemy('Cyborg_img', 750, [-2, 0]))

        self.label_frame = Text('frame', pos=(10,10))
        self.label_time = Text('time', pos=(10, 30))
        self.label_FPS = Text('FPS', pos=(10, 50))
        self.label_score = Text('SCORE', pos=(325, 20))
        self.label_final_score = Text('FINAL SCORE', pos=(300, 300))
        self.label_quote1 = Text('WAKE UP !', pos=(315, 500))
        self.label_quote2 = Text('NICE TRY !', pos=(325, 500))
        self.label_quote3 = Text('WHAT A PERFORMANCE !', pos=(285, 500))
        self.label_quote4 = Text('YOU\'RE A MONSTER !', pos=(295, 500))

        self.t0 = time.time()
    
    def update(self):     
        self.clock.tick(Game.FPS)
        rel_z = self.z % self.background.get_rect().width
        self.screen.blit(self.background, (rel_z - self.background.get_rect().width, 0))
        if rel_z < Game.W:
            self.screen.blit(self.background, (rel_z, 0))

        if not self.stopping:
            self.player.update()

            for bullet in Bullet.bullets:
                bullet.move()

            for enemy in Enemy.enemies:
                enemy.update()
                enemy.move()

            self.z -= 1
            
            global b
            if score % 1000 == 0 and score != 0 and b == 0:    
                for i in range(1):
                    Enemy.enemies.add(random.choice([Enemy('Mecha_img', 1500), Enemy('Gunman_img', 500, [-3, 0]), Enemy('Cyborg_img', 750, [-2, 0])]))
                b = 1
                
    def draw(self, screen):
        self.statistics()
        self.player.draw()
        Bullet.bullets.draw(Game.screen)
#         pygame.display.flip()
        for enemy in Enemy.enemies:
                enemy.draw()
    
    def run(self):
        running = True
        # running the game loop
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    self.player.keydown(event)
                    if event.key == K_SPACE:
                        self.stopping = not self.stopping
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(event.pos):
                        game.is_playing = True
#             self.screen.blit(self.background, (0, 0))
            if game.player.pv <= 0:
                game.is_playing = False
                self.screen.blit(self.gameover, self.gameover_rect)
                self.label_final_score.set_text('FINAL SCORE: ' + str(score))
                self.label_final_score.draw()
                if score < 4000:
                    self.label_quote1.set_text('WAKE UP !')
                    self.label_quote1.draw()
                elif score > 4000 and score < 8000:
                    self.label_quote2.set_text('NICE TRY !')
                    self.label_quote2.draw()
                elif score > 8000 and score < 13000:
                    self.label_quote3.set_text('WHAT A PERFORMANCE !')
                    self.label_quote3.draw()
                elif score > 13000:
                    self.label_quote4.set_text('YOU\'RE A MONSTER !')
                    self.label_quote4.draw()
            elif game.is_playing:
                game.update()
                game.draw(self.screen)
            else:
                self.screen.blit(self.banner, self.banner_rect)
                self.screen.blit(self.play_button, self.play_button_rect)
            pygame.display.flip()
                    
    def statistics(self):
        # calculate game statistics
        Game.frame += 1
        self.t = time.time() - self.t0
        self.fpg = Game.frame / self.t

        self.label_frame.set_text('frame: ' + str(Game.frame))
        self.label_time.set_text(f'time: {self.t:.1f}')
        self.label_FPS.set_text(f'FPS: {Game.frame/self.t:.1f}')
        self.label_score.set_text('SCORE: ' + str(score))
        

        self.label_frame.draw()
        self.label_time.draw()
        self.label_FPS.draw()
        self.label_score.draw()

game = Game()
game.run()