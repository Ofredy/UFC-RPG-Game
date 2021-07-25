import pygame
import time
from pygame.constants import MOUSEBUTTONDOWN
from chracters import *
# functions for visuals
class PygameGameFunctions:
    def skillselection(character, screen):
        running = True
        box1 = False
        box2 = False
        font = pygame.font.Font('freesansbold.ttf',22)
        box1text = font.render(character.sn1 + ": " + str(character.s1) + " power", True, (0,0,0))
        box2text = font.render(character.sn2 + ": " + str(character.s2) + " power", True, (0,0,0))
        while(running):
            if box1:
                pygame.draw.rect(screen, (255,215,0), (character.px+225, character.py-150, 175, 70))
            else:    
                pygame.draw.rect(screen, (0,255,0), (character.px+225, character.py-150, 175, 70))
            if box2:
                pygame.draw.rect(screen, (255,215,0), (character.px+225, character.py-50, 175, 70))
            else:    
                pygame.draw.rect(screen, (0,255,0), (character.px+225, character.py-50, 175, 70))       
            
            screen.blit(box1text,(character.px+225, character.py-125))
            screen.blit(box2text,(character.px+225, character.py-25))
        
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    if mouseX >= character.px+225 and mouseX <= character.px+225+175 and mouseY >= character.py-150 and mouseY <= character.py-80:
                        box1 = True
                    else:
                        box1 = False
                    if mouseX >= character.px+225 and mouseX <= character.px+225+175 and mouseY >= character.py-50 and mouseY <= character.py + 16:
                        box2 = True
                    else:
                        box2 = False           

                if event.type == MOUSEBUTTONDOWN:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    if mouseX >= character.px +225 and mouseX <= character.px +225+175 and mouseY >= character.py-150 and mouseY <= character.py-80:
                        return 1
                    elif mouseX >= character.px+225 and mouseX <= character.px+225+175 and mouseY >= character.py-50 and mouseY <= character.py + 16:
                        return 2
            pygame.display.update()

    def printaction(character1, character2, screen, background, damage, healed, num):
        font2 = pygame.font.Font('freesansbold.ttf',30)
        screen.blit(background,(0,0))
        screen.blit(pygame.image.load(character1.image),(character1.px,character1.py))
        screen.blit(pygame.image.load(character2.image),(character2.px,character2.py))
        PygameGameFunctions.nameprint(character1,screen)
        PygameGameFunctions.nameprint(character2, screen)
        if num == 1 and healed:
            pie = font2.render(character1.name + " healed " + str(damage) + " health", True, (255,255,0))
        elif num==1:
            pie = font2.render(character1.name + " dealt " + str(damage), True, (255,255,0))
        elif num==2 and healed:
            pie = font2.render(character2.name + " healed " + str(damage) + " health", True, (255,255,0))
        elif num==2:
            pie = font2.render(character2.name + " dealt " + str(damage), True, (255,255,0))

        if isinstance(character1, Wizard):
            pie1 = font2.render(character1.name + " has " + str(character1.health) + " health and " + str(character1.health) + " stamina", True, (255,255,0))
        else:
            pie2 = font2.render(character1.name + " has " + str(character1.health) + " health", True, (255,255,0))
        if isinstance(character2, Wizard):
            pie2 = font2.render(character2.name + " has " + str(character2.health) + " health and " + str(character2.health) + " stamina", True, (255,255,0))
        else:
            pie2 = font2.render(character2.name + " has " + str(character2.health) + " health", True, (255,255,0))
        screen.blit(pie,(170,110))
        screen.blit(pie1,(170,160))
        screen.blit(pie2, (170,210))
        pygame.display.update()

    def healthbar(character1,screen, inital1, initial2):
        if isinstance(character1, Wizard):
            pygame.draw.rect(screen, (0,0,0), (character1.px, character1.py-40, inital1*3, 20))
            pygame.draw.rect(screen, (0,255,0), (character1.px, character1.py-40, ((character1.health)*3) , 20))
            pygame.draw.rect(screen, (0,0,0), (character1.px, character1.py-70, initial2*3, 20))
            pygame.draw.rect(screen, (255,0,0), (character1.px, character1.py-70, ((character1.stamina)*3) , 20))        
        else: 
            pygame.draw.rect(screen, (0,0,0), (character1.px, character1.py-40, inital1*3, 20))
            pygame.draw.rect(screen, (0,255,0), (character1.px, character1.py-40, ((character1.health)*3) , 20))
        pygame.display.update()

    def nameprint(character, screen):
        font = pygame.font.Font('freesansbold.ttf',22)
        name = font.render(character.name, True, (0,0,0))
        screen.blit(name,(character.px+10, character.py+290))
        pygame.display.update()

    def gameover(screen, background, character1, character2):
        font2 = pygame.font.Font('freesansbold.ttf',80)
        screen.blit(background,(0,0))
        screen.blit(pygame.image.load(character1.image),(character1.px,character1.py))
        screen.blit(pygame.image.load(character2.image),(character2.px,character2.py))
        # game over text
        text = font2.render("GAME OVER", True, (255,0,0))
        screen.blit(text,(260, 400))
        pygame.display.update()
        time.sleep(1)

    def levelup(screen, character1, progress):
        screen.fill((176,224,230))
        screen.blit(pygame.image.load(character1.image),(character1.px, character1.py-50))
        font2 = pygame.font.Font('freesansbold.ttf',65)
        text = font2.render("Select which skill to level up", True, (255,255,255))
        screen.blit(text,(75, 150))
        skillUp = PygameGameFunctions.skillselection(character1, screen)
        if skillUp == 1:
            character1.s1 = character1.s1 + progress*5
        else:
            character1.s2 = character1.s2 + progress*5
        pygame.display.update()

    def characterbuild(screen, background):
        # the player list will have the character class, name, and skill selection
        playerList = []
        screen.blit(background,(0,0))
        font2 = pygame.font.Font('freesansbold.ttf',65)
        text = font2.render("Select your class", True, (255,255,0))
        screen.blit(text,(245, 150))
        text1 = font2.render("Chemist", True, (255,255,0))
        text2 = font2.render("Warrior", True, (255,255,0))
        text3 = font2.render("Wizard", True, (255,255,0))
        screen.blit(text1,(335, 300))
        screen.blit(text2, (350, 400))
        screen.blit(text3, (350, 500))
        pygame.display.update()
        return playerList