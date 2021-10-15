# Wormy (a Nibbles clone)
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Creative Commons BY-NC-SA 3.0 US

import random, sys, pygame
from pygame.locals import *

FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480 
CELLSIZE = 20 
assert WINDOWWIDTH % CELLSIZE == 0, 'win..'
assert WINDOWHEIGHT % CELLSIZE ==0,  'win..'
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWWIDTH/ CELLSIZE)


WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
DARKGREEN = (0, 155,0)
DARKGRAY = (40,40,40)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 10

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansblod.ttf, 18')
    pygame.display.set_caption('Wormy')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def runGame():

    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLWIDTH -6 )
    wormCords = [{'x': startx, 'y':starty},
        {'x': startx -1, 'y':starty},
        {'x': startx-2, 'y':starty}]
    directoin = 'RIGHT'


    apple = getRandomLocation()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT():
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate() 
                    

                # check if the worm has hit itself or the edge
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
            return # game over
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                return # game over

        # check if worm has eaten an apply
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            # don't remove worm's tail segment
            apple = getRandomLocation() # set a new apple somewhere
        else:
            del wormCoords[-1] # remove worm's tail segment

        if direction == UP:
            newHead == {'x':wormCords[HEAD]['x'],'y':wormCords[HEAD]['y']-1}
        elif direction == DOWN:
            newHead == {'x':wormCords[HEAD]['x'],'y':wormCords[HEAD]['y']+1}
        elif direction == LEFT:
            newHead == {'x':wormCords[HEAD]['x'] - 1,'y':wormCords[HEAD]['y']}
        elif direction == RIGHT:
            newHead == {'x':wormCords[HEAD]['x'] + 1,'y':wormCords[HEAD]['y']}

        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCords)
        drawApple(apple)
        drawScore(len(wormCords)- 3)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('press a key to play', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get.rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

    
def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0 :
        terminate()
    
    keyUpEvent = pygame.event.get(KEYUP):
    if len(keyUpEvent) == 0:
        return None
    if keyUpEvent[0].key == K_ESCAPE:
        terminate()
    return keyUpEvent[0].key

def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Wormy!', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('Wormy!', True, GREEN)

    degrees1 = 0 
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)

        rotateSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotateRect1 = rotateSurf1.get_rect()
        rotateRect1.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
        DISPLAYSURF.blit(rotateSurf1, rotateRect1)

        rotateSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotateRect2 = rotateSurf1.get_rect()
        rotateRect2.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
        DISPLAYSURF.blit(rotateSurf2, rotateRect2)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get()
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)

        






 
