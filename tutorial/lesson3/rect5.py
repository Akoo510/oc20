from rect import *

rect0 = Rect(50, 60, 200, 80)
rect = rect0.copy()

#dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        if event.type == KEYDOWN:
            if event.key in dir:
                v = dir[event.key]
                rect.inflate_ip(v)
                
    screen.fill(GRAY)
    pygame.draw.rect(screen, BLUE, rect0, 3)
    pygame.draw.rect(screen, RED, rect, 5)
    pygame.display.flip()
    
pygame.quit()