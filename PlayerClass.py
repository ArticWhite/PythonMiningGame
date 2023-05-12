class Charater:
    #stats
    HP = 0
    ATK = 0
    #resources
    stone = 0
    coal = 0
    iron = 0
    gold = 0
    ironIngot=0
    goldIngot=0
    def __init__(self, mode='EASY'):
        self.HP = 10
        self.ATK = 1
    
    
    def addStone(self):
        self.stone+=1
    def addCoal(self):
        self.coal+=1
    def addIron(self):
        self.iron+=1
    def addGold(self):
        self.gold+=1
    def smeltIron(self):
        if (self.iron>=1 and self.coal >= 1):
            self.iron-=1
            self.coal-=1
            self.ironIngot+=1
    def smeltGold(self):
        if (self.gold>=1 and self.coal >= 1):
            self.gold-=1
            self.coal-=1
            self.goldIngot+=1

    def takeDamage(self,damage):
        if (self.HP>0):
            self.HP-=damage
    def showHP(self):
        return self.HP
    def showATK(self):
        return self.ATK
    