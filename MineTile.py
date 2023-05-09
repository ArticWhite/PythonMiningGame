import PlayerClass
import numpy as np
import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
mapSize = 8
#game object stone #, coal *, iron @, gold $
#map tile probablity
probability=[75,87,97,99,100]
# objects 0 is stone, 1 is coal, 2 is iron, 3 gold 4 is open space, and 5 is stairs
#map array generating
gameMap = np.zeros((mapSize,mapSize))
#create player position and next level stair positon
charPos=[random.randint(0,mapSize-1),random.randint(0,mapSize-1)]
stairsPos=[random.randint(0,mapSize-1),random.randint(0,mapSize-1)]
while (stairsPos==charPos):
    stairsPos=[random.randint(0,mapSize-1),random.randint(0,mapSize-1)]
#map generating
def lvlGen():
    stairsPos=[random.randint(0,mapSize-1),random.randint(0,mapSize-1)]
    while (stairsPos==charPos):
        stairsPos=[random.randint(0,mapSize-1),random.randint(0,mapSize-1)]
    generateMap(charPos,stairsPos,mapSize,gameMap,probability)
    return charPos

def generateMap(charPos,stairsPos,mapSize,gameMap,probability):
    for i in range(mapSize):
        for j in range(mapSize):
            number = random.randint(1,100)
            if ((i != charPos[0]) or (j != charPos[1])):
                if probability[0]>=number:
                    gameMap[i][j]=0
                elif probability[1]>=number:
                    gameMap[i][j]=1
                elif probability[2]>=number:
                    gameMap[i][j]=2
                elif probability[3]>=number:
                    gameMap[i][j]=3
                elif probability[4]>=number:
                    gameMap[i][j]=4
            else:
                gameMap[i][j]=4
    gameMap[stairsPos[0]][stairsPos[1]]=5
generateMap(charPos,stairsPos,mapSize,gameMap,probability)

#character class generated
Player = PlayerClass.Charater()
pygame.init()
#checks to see if block is moveable to or has to be mined
def mineBlock(movingTo,gameMap):
    if (gameMap[movingTo[0]][movingTo[1]]==5):
        charPos = lvlGen()
    else: 
        if (gameMap[movingTo[0]][movingTo[1]]==4 or gameMap[movingTo[0]][movingTo[1]]==5):
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
            elif gameMap[i][j]==5:
                pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(50*(i+1), 50*(j+1), 50, 50))
    
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
