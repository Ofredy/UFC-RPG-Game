from pygame.constants import MOUSEBUTTONDOWN
from chracters import *
from pygameGameFunctions import *
import pygame
import random

class GameFunctions:
    # fight action when fighthing 
    def fight(character1, character2, screen, background):
        count = 0
        screen.blit(background,(0,0))
        screen.blit(pygame.image.load(character1.image),(character1.px, character1.py))
        screen.blit(pygame.image.load(character2.image),(character2.px, character2.py))
        pygame.display.update()

        font = pygame.font.Font('freesansbold.ttf',65)
        box = font.render("VICTORY", True, (255,0,0))

        initial1 = character1.health
        initial2 = character1.stamina
        initial3 = character2.health
        initial4 = character2.stamina

        while True:
            PygameGameFunctions.healthbar(character1, screen, initial1, initial2) 
            PygameGameFunctions.healthbar(character2, screen, initial3, initial4)
            c1 = PygameGameFunctions.skillselection(character1,screen)
            pygame.display.update()
            if character1.sn1 == "Healing Power":
                if c1 == 1:
                    character1.health += character1.s1
                    h = character1.s1
                    character1.stamina -= h * (1/3)
                    PygameGameFunctions.printaction(character1, character2, screen, background, h, True, 1)
                    PygameGameFunctions.healthbar(character1, screen, initial1, initial2)
                else:
                    character2.health -= character1.s2
                    damage = character1.s2
                    character1.stamina -= damage * (1/2)
                    # I will change this once I begin to work with pygame
                    PygameGameFunctions.printaction(character1, character2, screen, background, damage, False, 1)
                    PygameGameFunctions.healthbar(character2, screen, initial3, initial4)
            elif character1.sn2 == "Healing Power":
                if c1 == 1:
                    character2.health -= character1.s1
                    damage = character1.s1
                    character1.stamina -= damage * (1/2)
                    PygameGameFunctions.printaction(character1, character2, screen,background, damage, False, 1) 
                    PygameGameFunctions.healthbar(character2, screen, initial3, initial4)
                else:
                    character1.health += character1.s2
                    h = character1.s2
                    character1.stamina -= h * (1/3)
                    PygameGameFunctions.printaction(character1, character2, screen,background, h, True, 1)
                    PygameGameFunctions.healthbar(character1, screen, initial1, initial2)    
            else:
                if c1 == 1:
                    character2.health -= character1.s1
                    damage = character1.s1
                    character1.stamina -= damage * (1/2)
                    PygameGameFunctions.printaction(character1, character2, screen,background, damage, False, 1)
                    PygameGameFunctions.healthbar(character2, screen, initial3, initial4)     
                else:
                    character2.health -= character1.s2
                    damage = character1.s2
                    character1.stamina -= damage * (1/2)
                    # I will change this once I begin to work with pygame
                    PygameGameFunctions.printaction(character1, character2, screen,background, damage, False, 1)
                    PygameGameFunctions.healthbar(character2, screen, initial3, initial4)

            time.sleep(2)

            if character2.health <= 0:
                print(character1.name + " has won the battle")
                character1.health = initial1
                character1.stamina = initial2
                screen.blit(box, (350, 400))
                pygame.display.update()
                time.sleep(3)
                return True        
            elif isinstance(character2, Wizard) and character2.outofstamina():
                print(character1.name + " has won the battle " + character2.name + " is out of " + character2.sn3)
                character1.health = initial1
                character1.stamina = initial2
                screen.blit(box, (350, 400))
                pygame.display.update()
                time.sleep(3)
                return True

            if character2.name == "Voldermont" and character2.health <= 25 and count == 0:
                count += 1
                h = character2.healing()
                character2.stamina -= h * (1/3)
                PygameGameFunctions.printaction(character1, character2, screen, background , h, True, 2)    
                PygameGameFunctions.healthbar(character2, screen, initial3, initial4)  
                continue      

            c2 = random.randint(1,10)
            if c2%2 == 0:
                character1.health -= character2.s1
                damage = character2.s1
                character2.stamina -= damage * (1/2)
                PygameGameFunctions.printaction(character1, character2, screen, background , damage, False, 2)
                PygameGameFunctions.healthbar(character1, screen, initial1, initial2)
            else:
                character1.health -= character2.s2
                damage = character2.s2
                character2.stamina -= damage * (1/2)
                PygameGameFunctions.printaction(character1, character2, screen, background, damage, False, 2)
                PygameGameFunctions.healthbar(character1, screen, initial1, initial2)

            if character1.health <= 0:
                print(character2.name + " has won the battle")
                return False
            elif isinstance(character1, Wizard) and character1.outofstamina():
                print(character2.name + " has won the battle " + character1.name + " has ran out of " + character1.staminaName)
                return False

    def bossfight(character1, character2):
        count = 0
        while True:
            c1 = int(input("Choose a move " + character1.sn1 + " or " + character1.sn2))
            if character1.sn1 == "Healing Power":
                if c1 == 1:
                    character1.health += character1.s1
                    h = character1.s1
                    print(character1.name + " healed " + str(h) + " health")
                    print(character1)
                    print(character2)
                else:
                    character2.health -= character1.s2
                    damage = character1.s2
                    # I will change this once I begin to work with pygame
                    print(character1.name + " dealt " + str(damage) + " damage ")
                    print(character1)
                    print(character2)
            elif character1.sn2 == "Healing Power":
                if c1 == 1:
                    character2.health -= character1.s1
                    damage = character1.s1
                    print(character1.name + " dealt " + str(damage) + " damage ")
                    print(character1)
                    print(character2)  
                else:
                    character1.health += character1.s2
                    h = character1.s2
                    print(character1.name + " healed " + str(h) + " health")
                    print(character1)
                    print(character2)    
            else:
                if c1 == 1:
                    character2.health -= character1.s1
                    damage = character1.s1
                    print(character1.name + " dealt " + str(damage) + " damage ")
                    print(character1)
                    print(character2)     
                else:
                    character2.health -= character1.s2
                    damage = character1.s2
                    # I will change this once I begin to work with pygame
                    print(character1.name + " dealt " + str(damage) + " damage ")
                    print(character1)
                    print(character2)

            if character2.health <= 0:
                print(character1.name + " has won the battle")
                break

            if count == 0 and character2.health <= 25:
                count += 1
                character2.healing()
                print(character1)
                print(character2)
                continue 
            
            c2 = random.randint(1,100)
            if c2%3 == 0:
                character1.health -= character2.s1
                damage = character2.s1
                print(character2.name + " dealt " + str(damage))
            elif c2%3 == 1:
                character1.health -= character2.s2
                damage = character2.s2
                print(character2.name + " dealt " + str(damage))
            else:
                character1.health -= character2.s3
                damage = character2.s3
                print(character2.name + " dealt " + str(damage))

            if character1.health <= 0:
                print(character2.name + " has won the battle")
                break
            elif isinstance(character1, Wizard) and character1.outofstamina():
                print(character2.name + " has won the battle " + character1.name + " has ran out of " + character1.sn3)
                break

            print(character1)
            print(character2)