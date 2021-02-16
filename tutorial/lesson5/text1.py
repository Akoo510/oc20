import pygame
from pygame.locals import *
import time
 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

pygame.init()
screen = pygame.display.set_mode((640, 240))

sysfont = pygame.font.get_default_font()
print('system font :', sysfont)

t0 = time.time()
font = pygame.font.SysFont(None, 48)
print('time needed for Font creation :', time.time()-t0)

img = font.render(sysfont, True, RED)
rect = img.get_rect()
pygame.draw.rect(img, BLUE, rect, 1)

font1 = pygame.font.SysFont('chalkduster.ttf', 72)
img1 = font1.render('chalkduster.ttf', True, BLUE)

font2 = pygame.font.SysFont('didot.ttc', 72)
img2 = font2.render('didot.ttc', True, GREEN)

fonts = pygame.font.get_fonts()
print(len(fonts))
for i in range(7):
    print(fonts[i])
    
text = 'this text is editable'
font = pygame.font.SysFont(None, 48)
img = font.render(text, True, RED)

rect = img.get_rect()
rect.topleft = (20, 20)
cursor = Rect(rect.topright, (3, rect.height))

running = True
background = GRAY

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(text)>0:
                    text = text[:-1]
                    
            else:
                text += event.unicode
            img = font.render(text, True, RED)
            rect.size=img.get_size()
            cursor.topleft = rect.topright

    screen.fill(background)
    screen.blit(img, rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, RED, cursor)
    pygame.display.update()

pygame.quit()