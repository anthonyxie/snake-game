import pygame
import random
pygame.init()
fail = False
running = True
global board
xsize = 25
ysize = 25
board = pygame.display.set_mode([16*xsize,16*ysize])
movex = 0
movey = 0
foodyay = False
headx = 0
heady = 0
oldheadx = 0
oldheady = 0 
direction = "up"
snakeLength = 1
running = True
gameboard = [[0 for x in range(0,xsize)] for y in range(0,ysize)]
#gameboardmake
# temp = []
# gameboard = []
# for i in range (0,16):
#     temp.append(0)
# for i in range (0,16):
#   gameboard.append(temp)

print gameboard
#DEFINITIONS
def init(x):
    global gameboard
    global headx
    global heady
    global xsize
    global ysize
    tempx = (random.randint(4,xsize-4))
    tempy = (random.randint(4,xsize-4))
    gameboard[tempx][tempy] = x
    headx = tempx
    heady = tempy

def getInput():
    global running
    global direction
    global movex
    global movey
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.KEYDOWN:
            if direction != "right" and direction != "left":
                    if event.key == pygame.K_RIGHT:
                        direction = "right"
                    if event.key == pygame.K_LEFT:
                        direction = "left"
            if direction != "up" and direction != "down":
                    if event.key == pygame.K_UP:
                        direction = "up"
                    if event.key == pygame.K_DOWN:
                        direction = "down"
    if direction == "up":
        movex = 0
        movey = -1
    if direction == "down":
        movex = 0
        movey = 1
    if direction == "left":
        movex = -1
        movey = 0
    if direction == "right":
        movex = 1
        movey = 0
    


def evaluateHead():
    global headx
    global heady
    global movex
    global movey
    checkWall(headx, heady, movex, movey)
    checkCollision(headx, heady, movex, movey)
    checkFood(headx, heady, movex, movey)

def checkWall(headx, heady, movex, movey):
    global gameboard
    global fail
    if (heady + movey) < 0 or (heady + movey) > ysize-1:
        fail = True
    if (headx + movex) < 0 or (headx + movex) > xsize-1:
        fail = True

def checkCollision(headx, heady, movex, movey):
    global gameboard
    global fail
    if gameboard[headx + movex][heady + movey] > 0:
        fail = True


def checkFood(headx, heady, movex, movey):
    global gameboard
    global foodyay
    global snakeLength
    if gameboard[headx + movex][heady + movey] == -1:
        foodyay = True
        snakeLength = snakeLength + 1


def updateHead():
    global gameboard
    global headx
    global heady
    global movex
    global movey
    gameboard[headx + movex][heady + movey] = 1
    headx = headx + movex
    heady = heady + movey

def updateBody():
    global oldheadx
    global oldheady
    global foodyay
    global snakeLength
    for i in range (0,ysize):
        for j in range (0,xsize):
            if foodyay == False:
                if gameboard[i][j] > 0 and gameboard[i][j] < snakeLength:
                    gameboard[i][j] = gameboard[i][j] + 1
                elif gameboard[i][j] + 1 >= snakeLength:
                    gameboard[i][j] = 0
            if foodyay == True:
                if gameboard[i][j] > 0 and gameboard[i][j] < snakeLength:
                    gameboard[i][j] = gameboard[i][j] + 1
                elif gameboard[i][j] + 1 >= snakeLength:
                    gameboard[i][j] = snakeLength         

def NewFood():
    global gameboard
    if foodyay == True:
        tempx = (random.randint(2,xsize-2))
        tempy = (random.randint(2,ysize-2))
        while gameboard[tempx][tempy] > 0:
            tempx = (random.randint(2,xsize-2))
            tempy = (random.randint(2,ysize-2))
        gameboard[tempx][tempy] = -1


def drawState():
    global foodyay
    global gameboard
    colorname = random.choice(pygame.color.THECOLORS.keys())
    #pause for 20 milliseconds
    pygame.time.delay(75)
    #make the screen completely white
    board.fill((0,0,0))
    
    for i in range (0,ysize):
        for j in range (0,xsize):
            if gameboard[i][j] == 1:
                pygame.draw.rect(board, pygame.color.THECOLORS['green'], (16*i,16*j,16,16))
            elif gameboard[i][j] > 1:
                pygame.draw.rect(board, pygame.color.THECOLORS['red'], (16*i,16*j,16,16))
            elif gameboard[i][j] == -1:
                pygame.draw.rect(board, pygame.color.THECOLORS['blue'], (16*i,16*j,16,16))
            elif gameboard[i][j] == 0:
                pygame.draw.rect(board, pygame.color.THECOLORS['white'], (16*i,16*j,16,16))

    pygame.display.flip()
    foodyay = False
    print snakeLength
 # MAIN CODE
init(-1) 
init(1) 
drawState()
while running:
    getInput()
    evaluateHead()
    if fail == False:    
        updateBody()
        updateHead()
        NewFood()
        drawState()

pygame.quit()

    

 

