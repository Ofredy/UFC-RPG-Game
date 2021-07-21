# demo game code - fixed gameplay bugs
import pygame
from chracters import *
from gameFunctions import *
from pygameGameFunctions import *
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
playerImage = pygame.image.load(enemy1.image)

# enemy image
enemyImage = pygame.image.load(enemy3.image)

# demo while loop
running = True
while running:
    screen.fill((255,255,255))
    screen.blit(background,(0,0))
    
    screen.blit(playerImage,(enemy1.px,enemy3.py))
    screen.blit(enemyImage,(enemy3.px,enemy3.py))

    PygameGameFunctions.nameprint(enemy1, screen)
    PygameGameFunctions.nameprint(enemy3, screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    running = GameFunctions.fight(enemy1, enemy3, screen, background)
    if running == False:
        PygameGameFunctions.gameOver(screen, background, enemy1, enemy3)
    pygame.display.update()