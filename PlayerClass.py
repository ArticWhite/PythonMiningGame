class Charater:
    HP = 0
    stone = 0
    coal = 0
    iron = 0
    gold = 0
    ironIngot=0

    def __init__(self, mode='EASY'):
        self.HP = 3
    
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
            print(self.ironIngot)
