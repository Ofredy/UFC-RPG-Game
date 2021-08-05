import pygame
from defaultMaterial import *
import time
from pygame.constants import K_BACKSPACE, MOUSEBUTTONDOWN, MOUSEMOTION
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
                pygame.draw.rect(screen, (255,215,0), (character.px+225, character.py-150, 270, 70))
            else:    
                pygame.draw.rect(screen, (0,255,0), (character.px+225, character.py-150, 270, 70))
            if box2:
                pygame.draw.rect(screen, (255,215,0), (character.px+225, character.py-50, 270, 70))
            else:    
                pygame.draw.rect(screen, (0,255,0), (character.px+225, character.py-50, 270, 70))       
            
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
            pie1 = font2.render(character1.name + " has " + str(character1.health) + " health", True, (255,255,0))
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

    def levelup(screen, background ,character1, progress):
        screen.blit(background,(0,0))
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
        font2 = pygame.font.Font('freesansbold.ttf',65)
        screen.blit(background, (0,0))
        text = font2.render("Select your class", True, (255,255,0))
        text1 = font2.render("Chemist", True, (255,255,0))
        text2 = font2.render("Warrior", True, (255,255,0))
        text3 = font2.render("Wizard", True, (255,255,0))
        running1 = True

        while(running1):
            screen.blit(text,(245, 150))  

            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    print(str(mouseX) + " " + str(mouseY))

                    if mouseX >= 337 and mouseX <= 600 and mouseY >= 300 and mouseY <= 350:
                        text1 = font2.render("Chemist", True, (255,255,255))
                        screen.blit(text1,(335, 300))
                    else:
                        text1 = font2.render("Chemist", True, (255,255,0))
                        screen.blit(text1,(335, 300))
                    if mouseX >= 350 and mouseX <= 590 and mouseY >= 403 and mouseY <= 450:
                        text2 = font2.render("Warrior", True, (255,255,255))
                        screen.blit(text2, (350, 400))
                    else:
                        text2 = font2.render("Warrior", True, (255,255,0))
                        screen.blit(text2, (350, 400)) 
                    if mouseX >= 350 and mouseX <= 580 and mouseY >= 500 and mouseY <= 552:
                        text3 = font2.render("Wizard", True, (255,255,255))   
                        screen.blit(text3, (350, 500))
                    else:
                        text3 = font2.render("Wizard", True, (255,255,0))   
                        screen.blit(text3, (350, 500))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    if mouseX >= 337 and mouseX <= 600 and mouseY >= 300 and mouseY <= 350:
                        playerList.append("Chemist")
                        running1 = False
                    elif mouseX >= 350 and mouseX <= 590 and mouseY >= 403 and mouseY <= 450:
                        playerList.append("Warrior")
                        running1 = False
                    elif mouseX >= 350 and mouseX <= 580 and mouseY >= 500 and mouseY <= 552:
                        playerList.append("Wizard")
                        running1 = False
            pygame.display.update()
        time.sleep(0.2)

        running2 = True
        box1 = False
        font3 = pygame.font.Font('freesansbold.ttf',45)
        text4 = font3.render("Enter your name", True, (255,255,255))
        name = ""
        text5 = font3.render(name, True, (255,255,255))
        text6 = font3.render("Done", True, (0,0,0))
        while running2:
            screen.blit(background,(0,0))
            screen.blit(text4, (300,150))
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    print(str(mouseX) + " " + str(mouseY))
                
                if event.type == pygame.KEYDOWN and event.key != K_BACKSPACE and event.key >= 97 and event.key <= 122:
                    key = event.key
                    name = name + chr(key)
                    text5 = font3.render(name, True, (255,255,255))
                elif event.type == pygame.KEYDOWN and event.key == K_BACKSPACE and len(name)>0:
                    name = name[:-1]
                    text5 = font3.render(name, True, (255,255,255))

                if event.type == MOUSEBUTTONDOWN:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    if mouseX >= 398 and mouseX <= 550 and mouseY >=440 and mouseY <= 500:
                        running2 = False
                        playerList.append(name)

                if event.type == MOUSEMOTION:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    if mouseX >= 398 and mouseX <= 550 and mouseY >=440 and mouseY <= 500:
                        box1 = True
                    else:
                        box1 = False
            if len(name)>=1 and box1:
                pygame.draw.rect(screen, (255,0,0), (400, 440, 150, 60))
                screen.blit(text6, (420, 455))
            elif len(name) >=1:
                pygame.draw.rect(screen, (255,255,255), (400, 440, 150, 60))
                screen.blit(text6, (420, 455))

            screen.blit(text5, (380,290))
            pygame.display.update()

        return playerList

    def startMenu(screen, background):
        box = False
        font = pygame.font.Font('freesansbold.ttf',35)
        font2 = pygame.font.Font('freesansbold.ttf',40)
        text = font.render("New Game", True, (0,0,0))
        gameText = font2.render("UNIVERSE FIGHTHING CHAMPIONSHIP", True, (255,255,255))

        while True:
            screen.blit(background, (0,0))
            if box:
                pygame.draw.rect(screen, (255,215,0), (390, 583, 200, 100))
            else:    
                pygame.draw.rect(screen, (255,0,0), (390, 583, 200, 100))
            
            screen.blit(text, (395,620))
            screen.blit(gameText, (135, 365))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

                if event.type == MOUSEMOTION:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    if mouseX >= 389 and mouseX <= 589 and mouseY >=589 and mouseY <= 682:
                        box = True
                    else:
                        box = False

                if event.type == MOUSEBUTTONDOWN:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    if mouseX >= 389 and mouseX <= 589 and mouseY >=589 and mouseY <= 682:
                        return True

            pygame.display.update()