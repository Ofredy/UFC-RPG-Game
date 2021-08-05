from defaultMaterial import *
from chracters import *
from gameFunctions import *
from pygameGameFunctions import *
import pygame
from pygame import mixer 

# display initalizing
pygame.init()

# screen dimensions
height = 768
width = 1024
screen = pygame.display.set_mode((width,height))

# background pictures
mainBackground = pygame.image.load('cage.png')
fightBackground = pygame.image.load('background1.png')
characterBackground = pygame.image.load('background2.png')

# screen caption
pygame.display.set_caption("UFC RPG")
icon = pygame.image.load("ufc_icon.png")
pygame.display.set_icon(icon)

# background music
mixer.music.load("background.wav")
mixer.music.play(-1)

# game check points
startGame = False
level2 = False
level3 = False
level4 = False

# main game loop
while True:
    
    # to exit out of pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAMEOVER = True

    # main menu
    startGame = PygameGameFunctions.startMenu(screen, mainBackground)
    
    time.sleep(1)

    # character build
    playerList = PygameGameFunctions.characterbuild(screen, characterBackground)

    if playerList[0] == "Chemist":
        player = Chemist(playerList[1], 45, "Flame Thrower", 13, "Mini Nuke", 15, 'playerChemist.png', 50, 390, "Stamina", 55)
    elif playerList[0] == "Warrior":
        player = Warrior(playerList[1], 55 ,"Axe", 15, "Bow and Arrow", 9, 'warrior.png', 85, 460, "Stamina", 45)
    else:
        player = Wizard(playerList[1], 45, "Lightning Spell", 14, "Healing Spell", 10, 'wizard.png', 75, 415, "Mana", 45)

    time.sleep(1)

    # fight 1
    level2 = GameFunctions.fight(player, enemy1, screen, fightBackground)
    
    time.sleep(1)
    if level2:
        PygameGameFunctions.levelup(screen, characterBackground, player, 1)
    else:
        PygameGameFunctions.gameover(screen, fightBackground, player, enemy1)
        break

    time.sleep(1)

    # fight 2
    level3 = GameFunctions.fight(player, enemy2, screen, fightBackground)
    if level3:
        PygameGameFunctions.levelup(screen, characterBackground, player, 2)
    else:
        PygameGameFunctions.gameover(screen, fightBackground, player, enemy2)
        break

    # fight 3
    level4 = GameFunctions.fight(player, enemy3, screen, fightBackground)
    time.sleep(1)
    if level4:
        break
    else:
        PygameGameFunctions.gameover(screen,fightBackground, player, enemy3)
        break