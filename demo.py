import pygame
from chracters import *
from gameFunctions import *
from defaultEnemies import *

# display initalizing
pygame.init()
height = 768
width = 1024
screen = pygame.display.set_mode((width,height))
background = pygame.image.load('background1.png')

# caption
pygame.display.set_caption("UFC RPG")

# player image
playerImage = pygame.image.load('warrior.png')
playerX = 70
playerY = 350
onBox1 = False
onBox2 = False

# enemy image
enemyImage = pygame.image.load('kingVito.png')
enemyX = 720
enemyY = 470

# demo while loop
running = True
while running:
    screen.fill((255,255,255))
    screen.blit(background,(0,0))
    
    # player image
    screen.blit(playerImage,(playerX, playerY))
    if onBox1:
        pygame.draw.rect(screen, (255,215,0), (playerX+225, playerY-150, 175, 70))
    else:    
        pygame.draw.rect(screen, (255,255,255), (playerX+225, playerY-150, 175, 70))
    if onBox2:
        pygame.draw.rect(screen, (255,215,0), (playerX+225, playerY-50, 175, 70))
    else:    
        pygame.draw.rect(screen, (255,255,255), (playerX+225, playerY-50, 175, 70))
    pygame.draw.rect(screen, (0,255,0), (playerX-5, playerY-40, 200, 20))
    
    # enemy image
    screen.blit(enemyImage,(enemyX,enemyY))
    pygame.draw.rect(screen, (255,255,255), (enemyX-225, enemyY-150, 175, 70))
    pygame.draw.rect(screen, (255,255,255), (enemyX-225, enemyY-50, 175, 70))
    pygame.draw.rect(screen, (0,255,0), (enemyX-25, enemyY-40, 200, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            print(str(mouseX) + " " + str(mouseY))

            if mouseX >= playerX+225 and mouseX <= playerX+225+175 and mouseY >= playerY-150 and mouseY <= playerY-80:
                onBox1 = True
            else:
                onBox1 = False

            if mouseX >= playerX+225 and mouseX <= playerX+225+175 and mouseY >= playerY-50 and mouseY <= playerY + 16:
                onBox2 = True
            else:
                onBox2 = False

    pygame.display.update()