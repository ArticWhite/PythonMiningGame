import PlayerClass
import numpy as np
import pygame
import random
mapSize = 8
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
#game object stone #, coal *, iron @, gold $
gameObjects=['#','*','@','$','']
#map tile probablity
probablity=[75,87,97,99,100]
#map array generating
gameMap = np.zeros((mapSize,mapSize))
charPos=[0,0]
#map generating
for i in range(mapSize):
    for j in range(mapSize):
        number = random.randint(1,100)
        if ((i != charPos[0]) or (j != charPos[1])):
            if probablity[0]>=number:
                gameMap[i][j]=0
            elif probablity[1]>=number:
                gameMap[i][j]=1
            elif probablity[2]>=number:
                gameMap[i][j]=2
            elif probablity[3]>=number:
                gameMap[i][j]=3
            elif probablity[4]>=number:
                gameMap[i][j]=4
        else:
            gameMap[i][j]=4
#character class generated
Player = PlayerClass.Charater()
pygame.init()
#checks to see if block is moveable to or has to be mined
def mineBlock(movingTo,gameMap):
    if (gameMap[movingTo[0]][movingTo[1]]==4):
        return True
    else:
        gameMap[movingTo[0]][movingTo[1]]=4
        return False
    
def moveUp(charPos,gameMap):
    if (charPos[1]!=0):
        if (mineBlock((charPos[0],charPos[1]-1),gameMap)):
            charPos[1]-=1
def moveDown(charPos,gameMap):
    if (charPos[1]!=len(gameMap[0])-1):
        if (mineBlock((charPos[0],charPos[1]+1),gameMap)):
            charPos[1]+=1
def moveLeft(charPos,gameMap):
    if (charPos[0]!=0):
        if (mineBlock((charPos[0]-1,charPos[1]),gameMap)):
            charPos[0]-=1
def moveRight(charPos,gameMap):
    if (charPos[0]!=len(gameMap[0])-1):
        if (mineBlock((charPos[0]+1,charPos[1]),gameMap)):
            charPos[0]+=1

#set up the drawing screen
screen = pygame.display.set_mode([500, 500])
running = True

while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Fill the background with white
    screen.fill((0, 0, 0))
    # Draw map tiles
    for i in range(0,mapSize,1):
        for j in range(0,mapSize,1):
            if gameMap[i][j]==0:
                pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(50*(i+1), 50*(j+1), 50, 50))
            elif gameMap[i][j]==1:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50*(i+1), 50*(j+1), 50, 50))
            elif gameMap[i][j]==2:
                pygame.draw.rect(screen, (175, 50, 0), pygame.Rect(50*(i+1), 50*(j+1), 50, 50))
            elif gameMap[i][j]==3:
                pygame.draw.rect(screen, (255, 215, 0), pygame.Rect(50*(i+1), 50*(j+1), 50, 50))
            elif gameMap[i][j]==4:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(50*(i+1), 50*(j+1), 50, 50))
    pygame.draw.circle(screen, (0, 100, 5), (50*(charPos[0]+1)+25, 50*(charPos[1]+1)+25), 25)
    # Look at every event in the queue
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_UP:
                moveUp(charPos,gameMap)
            elif event.key == K_DOWN:
                moveDown(charPos,gameMap)
            elif event.key == K_LEFT:
                moveLeft(charPos,gameMap)
            elif event.key == K_RIGHT:
                moveRight(charPos,gameMap)
    # Flip the display
    pygame.display.flip()
# Done! Time to quit.
pygame.quit()
