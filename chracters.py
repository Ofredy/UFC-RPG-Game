# base character
class Character:
    def __init__(self, name, health, sn1, s1, sn2, s2, image, pX, pY, staminaName, stamina):
        self.name = name
        self.health = health
        self.s1 = s1
        self.sn1 = sn1
        self.s2 = s2
        self.sn2 = sn2
        self.image = image
        self.px = pX
        self.py = pY
        self.staminaName = staminaName
        self.stamina = stamina

    def __str__(self):
        return self.name + "'s health is " + str(self.health)

# the weakness of the chemist will be its low health
class Chemist(Character):
    def __init__(self, name, health, sn1, s1, sn2, s2, image, pX, pY, staminaName, stamina):
        super().__init__(name, health, sn1, s1, sn2, s2, image, pX, pY, staminaName, stamina)
    
# the weakness of the wizard will be its low stamina
class Wizard(Character):
    def __init__(self, name, health, sn1, s1, sn2, s2, image, pX, pY, staminaName, stamina):
        super().__init__(name, health, sn1, s1, sn2, s2, image, pX, pY, staminaName, stamina)

    def __str__(self):
        return self.name + "'s health is " + str(self.health) + " and " + self.sn3 + " left is " + str(self.s3)
        
    def healing(self):
        self.health += 10
        return 10

    def outofstamina(self):
        if self.stamina <=0:
            return True
        else:
            return False

# weakness will be its low stamina
class Warrior(Wizard):
    def __init__(self, name, health, sn1, s1, sn2, s2, image, pX, pY, staminaName, stamina):
        super().__init__(name, health, sn1, s1, sn2, s2, image, pX, pY, staminaName, stamina)

# will have no weakness final boss fight
class Alien(Wizard):
    def __init__(self, name, health, sn1, s1, sn2, s2, image, pX, pY, staminaName, stamina, sn3, s3):
        super().__init__(name, health, sn1, s1, sn2, s2, image, pX, pY, staminaName, stamina)
        self.sn3 = sn3
        self.s3 = s3

    def __str__(self):
        return self.name + "'s health is " + str(self.health)

    def healing(self):
        print(self.name + " has healed " + str(20) + " health" )
        self.health += 20