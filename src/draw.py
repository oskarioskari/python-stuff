import pygame
from tablehandler import getRows
from tablehandler import saveToFile
from gameoflife import playRound
import time

def drawWin(width,height,tablefile,xlim,ylim):
    pygame.init()
    
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    
    size = [width,height]
    screen = pygame.display.set_mode(size)
    
    done = False
    clock = pygame.time.Clock()
    
    blockwidth = int(width/xlim)
    blockheight = int(height/ylim)
    tilelist = getRows(tablefile,xlim,ylim)
    print "Loaded",blockwidth,blockheight
    
    print "Starting game"
    while not done:
        clock.tick(5)
        nyt = time.time()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        screen.fill(BLACK)
        
        for k in tilelist:
            xy = k.split("-")
            x = xy[0]
            y = xy[1]
            x = int(x)*blockwidth
            y = int(y)*blockheight
            color = int(tilelist[k])
            if color == 1: # DEAD
                pygame.draw.rect(screen,WHITE,[x,y,blockwidth,blockheight],0)
            elif color == 2: # ALIVE
                pygame.draw.rect(screen,BLACK,[x,y,blockwidth,blockheight],0)
        
        pygame.display.flip()
        tilelist = playRound(tilelist,xlim,ylim)
    print "Quitting"
    pygame.quit()
    saveToFile(tilelist,tablefile)
