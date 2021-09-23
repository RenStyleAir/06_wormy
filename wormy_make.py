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


