# base character
class Character:
    def __init__(self, name, health, sn1, s1, sn2, s2):
        self.name = name
        self.health = health
        self.s1 = s1
        self.sn1 = sn1
        self.s2 = s2
        self.sn2 = sn2

    def __str__(self):
        return self.name + "'s health is " + str(self.health)

# the weakness of the chemist will be its low health
class Chemist(Character):
    def __init__(self, name, health, sn1, s1, sn2, s2):
        super().__init__(name, health, sn1, s1, sn2, s2)
    
# the weakness of the wizard will be its low stamina
class Wizard(Character):
    def __init__(self, name, health, sn1, s1, sn2, s2, staminaName, stamina):
        super().__init__(name, health, sn1, s1, sn2, s2)
        self.s3 = stamina
        self.sn3 = staminaName

    def __str__(self):
        return self.name + "'s health is " + str(self.health) + " and " + self.sn3 + " left is " + str(self.s3)
        
    def healing(self):
        print(self.name + " has healed " + str(10) + " health" )
        self.health += 10

    def OutOfStamina(self):
        if self.s3 <=0:
            return True
        else:
            return False

# weakness will be its low stamina
class Warrior(Wizard):
    def __init__(self, name, health, sn1, s1, sn2, s2, staminaName, stamina):
        super().__init__(name, health, sn1, s1, sn2, s2, staminaName, stamina)

# will have no weakness final boss fight
class Alien(Wizard):
    def __init__(self, name, health, sn1, s1, sn2, s2, staminaName, stamina, sn3, s3):
        super().__init__(name, health, sn1, s1, sn2, s2, staminaName, stamina)
        self.s3 = s3
        self.sn3 = sn3

    def __str__(self):
        return self.name + "'s health is " + str(self.health)

    def healing(self):
        print(self.name + " has healed " + str(20) + " health" )
        self.health += 20