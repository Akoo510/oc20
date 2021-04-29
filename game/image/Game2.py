import pygame
import sys
from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))

background = pygame.image.load('background.png')
background_pos = background.get_rect()

class spritesheet(object):
    def __init__(self, filename):
        pass
    def image_at(self, rectangle, colorkey = None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
    

class SpriteStripAnim(object):
    """sprite strip animator
    
    This class provides an iterator (iter() and next() methods), and a
    __add__() method for joining strips which comes in handy when a
    strip wraps to the next row.
    """
    def __init__(self, filename, rect, count, colorkey=None, loop=False, frames=1):
        """construct a SpriteStripAnim
        
        filename, rect, count, and colorkey are the same arguments used
        by spritesheet.load_strip.
        
        loop is a boolean that, when True, causes the next() method to
        loop. If False, the terminal case raises StopIteration.
        
        frames is the number of ticks to return the same image before
        the iterator advances to the next image.
        """
        self.filename = filename
        ss = spritesheet.spritesheet(filename)
        self.images = ss.load_strip(rect, count, colorkey)
        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames
    def iter(self):
        self.i = 0
        self.f = self.frames
        return self
    def next(self):
        if self.i >= len(self.images):
            if not self.loop:
                raise StopIteration
            else:
                self.i = 0
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return image
    def __add__(self, ss):
        self.images.extend(ss.images)
        return self

frames = 10
strips = [
    SpriteStripAnim('Soldier.png', (0, 0, 16, 16), 8, 1, True, frames),
# # # # # # # #     
]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    player = pygame.image.load('player.png')
    player_pos = player.get_rect()
    
    rapido = pygame.image.load('rapido.png')
    rapido_pos = rapido.get_rect()
    
    tankos = pygame.image.load('tankos.png')
    tankos_pos = tankos.get_rect()
    
    ff = pygame.image.load('ff.png')
    ff_pos = ff.get_rect()
            
    screen.blit(background, background_pos)
    screen.blit(player, player_pos)
    screen.blit(rapido, rapido_pos)
    screen.blit(tankos, tankos_pos)
    screen.blit(ff, ff_pos)