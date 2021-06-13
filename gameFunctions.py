from pygame.constants import MOUSEBUTTONDOWN
from chracters import *
from pygameGameFunctions import *
import pygame
import random

class GameFunctions:
    # fight action when fighthing 
    def fight(character1, character2, screen, background):
        count = 0
        
        initial1 = character1.health
        if isinstance(character1, Wizard):
            initial2 = character1.stamina
        else:
            initial2 = 0
        initial3 = character2.health
        if isinstance(character2, Wizard):
            initial4 = character2.stamina
        else:
            initial4 = 0

        while True:
            # will be inputted from user using pygame, for now i will do this
            PygameGameFunctions.healthbar(character1, screen, initial1, initial2) 
            PygameGameFunctions.healthbar(character2, screen, initial3, initial4)
            c1 = PygameGameFunctions.skillselection(character1,screen)
            if character1.sn1 == "Healing Power":
                if c1 == 1:
                    character1.health += character1.s1
                    h = character1.s1
                    PygameGameFunctions.printaction(character1, character2, screen, background, h, True, 1)
                    PygameGameFunctions.healthbar(character1, screen, initial1, initial2)
                else:
                    character2.health -= character1.s2
                    damage = character1.s2
                    # I will change this once I begin to work with pygame
                    PygameGameFunctions.printaction(character1, character2, screen, background, damage, False, 1)
                    PygameGameFunctions.healthbar(character2, screen, initial3, initial4)
            elif character1.sn2 == "Healing Power":
                if c1 == 1:
                    character2.health -= character1.s1
                    damage = character1.s1
                    PygameGameFunctions.printaction(character1, character2, screen,background, damage, False, 1) 
                    PygameGameFunctions.healthbar(character2, screen, initial3, initial4)
                else:
                    character1.health += character1.s2
                    h = character1.s2
                    PygameGameFunctions.printaction(character1, character2, screen,background, h, True, 1)
                    PygameGameFunctions.healthbar(character1, screen, initial1, initial2)    
            else:
                if c1 == 1:
                    character2.health -= character1.s1
                    damage = character1.s1
                    PygameGameFunctions.printaction(character1, character2, screen,background, damage, False, 1)
                    PygameGameFunctions.healthbar(character2, screen, initial3, initial4)     
                else:
                    character2.health -= character1.s2
                    damage = character1.s2
                    # I will change this once I begin to work with pygame
                    PygameGameFunctions.printaction(character1, character2, screen,background, damage, False, 1)
                    PygameGameFunctions.healthbar(character2, screen, initial3, initial4)

            if character2.health <= 0:
                print(character1.name + " has won the battle")
                break         
            elif isinstance(character2, Wizard) and character2.outofstamina():
                print(character1.name + " has won the battle " + character2.name + " is out of " + character2.sn3)
                break

            if character2.name == "Voldermont" and character2.health <= 25 and count == 0:
                count += 1
                h = character2.healing()
                PygameGameFunctions.printaction(character1, character2, screen, background , h, True, 2)    
                PygameGameFunctions.healthbar(character2, screen, initial3, initial4)  
                continue      

            c2 = random.randint(1,10)
            if c2%2 == 0:
                character1.health -= character2.s1
                damage = character2.s1
                PygameGameFunctions.printaction(character1, character2, screen, background , damage, False, 2)
                PygameGameFunctions.healthbar(character1, screen, initial1, initial2)
            else:
                character1.health -= character2.s2
                damage = character2.s2
                PygameGameFunctions.printaction(character1, character2, screen, background, damage, False, 2)
                PygameGameFunctions.healthbar(character1, screen, initial1, initial2)

            if character1.health <= 0:
                print(character2.name + " has won the battle")
                return False
            elif isinstance(character1, Wizard) and character1.outofstamina():
                print(character2.name + " has won the battle " + character1.name + " has ran out of " + character1.sn3)
                return False

    def multiplayerfight(character1, character2):
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
            elif isinstance(character2, Wizard) and character2.outofstamina():
                print(character1.name + " has won the battle " + character2.name + " is out of " + character2.sn3)
                break

            # character 2
            c2 = int(input("Choose a move " + character2.sn1 + " or " + character2.sn2))
            if character2.sn1 == "Healing Power":
                if c2 == 1:
                    character2.health += character2.s1
                    h = character2.s1
                    print(character2.name + " healed " + str(h) + " health")
                    print(character1)
                    print(character2)
                else:
                    character1.health -= character2.s2
                    damage = character2.s2
                    # I will change this once I begin to work with pygame
                    print(character2.name + " dealt " + str(damage) + " damage ")
                    print(character1)
                    print(character2)
            elif character2.sn2 == "Healing Power":
                if c2 == 1:
                    character1.health -= character2.s1
                    damage = character2.s1
                    print(character2.name + " dealt " + str(damage) + " damage ")
                    print(character1)
                    print(character2)  
                else:
                    character2.health += character2.s2
                    h = character2.s2
                    print(character2.name + " healed " + str(h) + " health")
                    print(character1)
                    print(character2)    
            else:
                if c2 == 1:
                    character1.health -= character2.s1
                    damage = character2.s1
                    print(character2.name + " dealt " + str(damage) + " damage ")
                    print(character1)
                    print(character2)     
                else:
                    character1.health -= character2.s2
                    damage = character2.s2
                    # I will change this once I begin to work with pygame
                    print(character2.name + " dealt " + str(damage) + " damage ")
                    print(character1)
                    print(character2)

            if character1.health <= 0:
                print(character1.name + " has won the battle")
                break
            elif isinstance(character1, Wizard) and character1.outofstamina():
                print(character2.name + " has won the battle " + character1.name + " has ran out of " + character1.sn3)
                break

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

    def makingcharacter(list1, check1, check2):
        info = []
        print("Select your class")
        info.append(int(input(list1[0] + " " + list1[1] + " " + list1[2])))
        info.append(input("Enter the name of your character"))
        if info[0] == 1:
            return info
        elif info[0] == 2:
            list2 = check1
            print("Select which skills 2 you want to use")
            index1 = int(input(list2[0] + " strenght " + str(list2[1]) + ", " + list2[2] + " strenght " + str(list2[3]) + ", " + list2[4] + " strenght " + str(list2[5])))
            if index1 == 1:
                info.append(list2[index1-1])
                info.append(list2[index1])
                list2.remove(list2[index1-1])
                list2.remove(list2[index1-1])
            elif index1 == 2:
                info.append(list2[index1])
                info.append(list2[index1+1])
                list2.remove(list2[index1])
                list2.remove(list2[index1])
            elif index1 ==3:
                info.append(list2[index1+1])
                info.append(list2[index1+2])
                list2.remove(list2[index1+1])
                list2.remove(list2[index1+1])

            index2 = int(input(list2[0] + " strenght " + str(list2[1]) + ", " + list2[2] + " strenght " + str(list2[3])))
            if index2 == 1:
                info.append(list2[index2-1])
                info.append(list2[index2])
            else:
                info.append(list2[index2])
                info.append(list2[index2+1])
            
            return info
        else:
            list3 = check2
            print("Select which skills 2 you want to use")
            index1 = int(input(list3[0] + " strenght " + str(list3[1]) + ", " + list3[2] + " strenght " + str(list3[3]) + ", " + list3[4] + " strenght " + str(list3[5])))
            if index1 == 1:
                info.append(list3[index1-1])
                info.append(list3[index1])
                list3.remove(list3[index1-1])
                list3.remove(list3[index1-1])
            elif index1 == 2:
                info.append(list3[index1])
                info.append(list3[index1+1])
                list3.remove(list3[index1])
                list3.remove(list3[index1])
            elif index1 == 3:
                info.append(list3[index1+1])
                info.append(list3[index1+2])
                list3.remove(list3[index1+1])
                list3.remove(list3[index1+1])
            index2 = int(input(list3[0] + " strenght " + str(list3[1]) + ", " + list3[2] + " strenght " + str(list3[3])))
            if index2 == 1:
                info.append(list3[index2-1])
                info.append(list3[index2])
            else:
                info.append(list3[index2])
                info.append(list3[index2+1])                
            return info

    def levelup(character):


        # adjust for pygame
        print("Health is " + str(character.health))
        print(str(character.sn1))
        print(str(character.sn2))
        choice = int(input("What would you like to improve"))
        if choice == 1:
            character.health += 5
        elif choice == 2:
            character.s1 += 5
        else:
            character.s2 += 5