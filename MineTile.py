import PlayerClass
from ButtonClass import Button
import MonsterClass
import numpy as np
import pygame
import random
import time
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_i,
)
X = 650
Y = 650
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
mapSize = 12
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
def resourcesText(font):
    text = font.render('Stone: {} Coal: {}, Iron: {} Gold: {}'.format(Player.stone,Player.coal,Player.iron,Player.gold), True, green, blue) 
    textRect = text.get_rect()
    textRect.center = (X // 3, Y -25)
    screen.blit(text, textRect)
def inventoryText(font):
    text = font.render('Iron Ignots: {} Gold Ingots: {}'.format(Player.ironIngot,Player.goldIngot), True, green, blue) 
    textRect = text.get_rect()
    textRect.center = (X // 3, Y -50)
    screen.blit(text, textRect)
#player HP bar
def playerHP(font):
    text = font.render('HP:'+"@"*Player.HP, True, green, blue) 
    textRect = text.get_rect()
    textRect.center = (100, 20)
    screen.blit(text, textRect)
    #battle screen for combat
def monsterHP(enemy,font):
    text = font.render('Enemy HP:'+"@"*enemy.HP, True, green, blue) 
    textRect = text.get_rect()
    textRect.center = (400, 20)
    screen.blit(text, textRect)   

def fightScreen(monster):
    battling = True
    enemy=None
    if (monster==6):
        enemy = MonsterClass.Goblin(1,3)
    def runAway():
        battling=False
    def attack():
        time.sleep(0.1)
        enemy.HP-=Player.showATK()
        Player.HP-=enemy.showATK()
    
    while battling:
        if (Player.showHP() == 0):
            return False
        if (enemy.showHP() == 0):
            return True
        objects=[]
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, X, Y))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    battling = False
        
        #player sprit location
        pygame.draw.circle(screen, (0, 0, 255), (125, 400), 100)
        #enemy Sprite location
        pygame.draw.circle(screen, (0, 255, 0), (550, 350), 100)
        #player hot bar
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, Y - 200, X, Y))
        playerHP(font)
        monsterHP(enemy,font)
        b1 = Button(100, Y - 75 , 200, 50, screen, 'Attack', attack)
        #b2 = Button(325, Y - 75, 200, 50, screen, 'RUN', runAway)
        objects.append(b1)
        #objects.append(b2)
        for button in objects:
            button.process()
        pygame.display.flip()
#death screen script
def deathScreen():
    while True:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, X, Y))
        font = pygame.font.Font('freesansbold.ttf', 40)
        text = font.render('You have Died', True, green, blue) 
        textRect = text.get_rect()
        textRect.center = (X // 2, Y // 2)
        screen.blit(text, textRect)  
        pygame.display.flip()
    
#map generating
def lvlGen(Pos):
    stairsPos=[random.randint(0,mapSize-1),random.randint(0,mapSize-1)]
    charPos=Pos
    while (stairsPos==charPos):
        stairsPos=[random.randint(0,mapSize-1),random.randint(0,mapSize-1)]
    generateMap(charPos,stairsPos,mapSize,gameMap,probability)
    

def generateMap(charPos,stairsPos,mapSize,gameMap,probability):
    for i in range(mapSize):
        for j in range(mapSize):
            number = random.randint(1,100)
            if ((i != charPos[0]) or (j != charPos[1])):
                #spawn stone
                if probability[0]>=number:
                    gameMap[i][j]=0
                #spawn coal
                elif probability[1]>=number:
                    gameMap[i][j]=1
                #spawn iron
                elif probability[2]>=number:
                    gameMap[i][j]=2
                #spawn gold
                elif probability[3]>=number:
                    gameMap[i][j]=3
                #spawn open space or goblin
                elif probability[4]>=number:
                    num=random.randint(1,2)
                    if (num == 1):
                        gameMap[i][j]=4
                    else:
                        gameMap[i][j]=6
            else:
                gameMap[i][j]=4
    gameMap[stairsPos[0]][stairsPos[1]]=5
generateMap(charPos,stairsPos,mapSize,gameMap,probability)
#checks to see if block is moveable to or has to be mined
def mineBlock(movingTo,gameMap):
    # if enter stair tile
    if (gameMap[movingTo[0]][movingTo[1]]==5):
        #if the block is stairs go down
        lvlGen(movingTo)
        return True
    else: 
        if (gameMap[movingTo[0]][movingTo[1]]==4 or gameMap[movingTo[0]][movingTo[1]]==5):
            return True
        # if enetered combat with enemy tile
        elif gameMap[movingTo[0]][movingTo[1]]==6:
            outcome = fightScreen(monster=gameMap[movingTo[0]][movingTo[1]])
            if (outcome == True):
                gameMap[movingTo[0]][movingTo[1]]=4
            return outcome
            
        else:
            #adding collected material to inventory
            if gameMap[movingTo[0]][movingTo[1]] == 0:
                Player.addStone()
            if gameMap[movingTo[0]][movingTo[1]] == 1:
                Player.addCoal()
            if gameMap[movingTo[0]][movingTo[1]] == 2:
                Player.addIron()
            if gameMap[movingTo[0]][movingTo[1]] == 3:
                Player.addGold()
            gameMap[movingTo[0]][movingTo[1]]=4
            return False
    
#movement controls for the player
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

#helper method for smelting ore for buttons
#character class generated
Player = PlayerClass.Charater()
pygame.init()
#game title
pygame.display.set_caption('Mine Tile')
#game font text
font = pygame.font.Font('freesansbold.ttf', 10)

#set up the drawing screen
screen = pygame.display.set_mode([X, Y])
running = True

while running:
    if Player.showHP()<=0:
        break
    screen.fill((0, 0, 0))
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Fill the background with white
    
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
            elif gameMap[i][j]==6:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(50*(i+1), 50*(j+1), 50, 50))
                pygame.draw.circle(screen, (0, 255, 0), (50*(i+1)+25, 50*(j+1)+25), 25)
    pygame.draw.circle(screen, (0, 0, 255), (50*(charPos[0]+1)+25, 50*(charPos[1]+1)+25), 25)
    resourcesText(font)
    playerHP(font)
    # Look at every event in the queue
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_i:
                inInv=True
                #inventory
                while inInv:
                    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, X, Y))
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                        # Was it the Escape key? If so, stop the loop.
                            if event.key == K_i:
                                inInv = False
                    #buttons created here for inventory
                    objects = []
                    resourcesText(font)
                    inventoryText(font)
                    b1 = Button(30, 50, 400, 100, screen, 'Smelt Iron', Player.smeltIron)
                    b2 = Button(30, 150, 400, 100, screen, 'Smelt Gold', Player.smeltGold)
                    objects.append(b1)
                    objects.append(b2)
                    for object in objects:
                        object.process()
                    pygame.display.flip()
                    #resourced text
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        moveUp(charPos,gameMap)
        time.sleep(0.2)
    if keys[pygame.K_DOWN]:
        moveDown(charPos,gameMap)
        time.sleep(0.2)
    if keys[pygame.K_LEFT]:
        moveLeft(charPos,gameMap)
        time.sleep(0.2)
    if keys[pygame.K_RIGHT]:
        moveRight(charPos,gameMap)
        time.sleep(0.2)
    

    # Flip the display
    pygame.display.flip()
#death screen
deathScreen()
# Done! Time to quit.
pygame.quit()
