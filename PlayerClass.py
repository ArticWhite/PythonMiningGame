class Charater:
    #stats
    HP = 0
    ATK = 0
    EXP=0
    LVL=0
    MAXEXP= 5+5*LVL
    #resources
    stone = 0
    coal = 0
    iron = 0
    gold = 0
    ironIngot=0
    goldIngot=0
    #items
    hand = None
    items = [["ROCK",0],["DAGGER",0],["SWORD",0]]
    WEAPONS ={
        "ROCK":2,
        "DAGGER":3,
        "SWORD":4
    }
    
    ARMOR={
        "HELMET" : 2,
        "CHEST PLATE" : 6,
        "IRON PANTS" : 4
    }
    def __init__(self):
        self.LVL = 1
        self.HP = 8 + 2*self.LVL
        self.ATK = 1
        self.MAXEXP=5+5*self.LVL
    
    def addStone(self):
        self.stone+=1
    def addCoal(self):
        self.coal+=1
    def addIron(self):
        self.iron+=1
    def addGold(self):
        self.gold+=1
    def addEXP(self, exp):
        self.EXP += exp
        if (self.EXP>=self.MAXEXP):
            self.LVL+=1
            self.EXP=self.EXP-self.MAXEXP
            self.HP = 8 + 2*self.LVL
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
    def showHand(self):
        return self.hand
    def equipRock(self):
        if(self.items[0][1]>0):
            self.hand = "ROCK"
            self.ATK=self.WEAPONS["ROCK"]
    def equipDagger(self):
        if(self.items[1][1]>0):
            self.hand = "DAGGER"
            self.ATK=self.WEAPONS["DAGGER"]
    def equipSword(self):
        if(self.items[2][1]>0):
            self.hand = "SWORD"
            self.ATK=self.WEAPONS["SWORD"]
    def craftRock(self):
        if (self.stone>=5):
            self.stone -=5
            self.items[0][1]+=1
    def craftDagger(self):
        if (self.ironIngot>=15):
            self.ironIngot -=15
            self.items[1][1]+=1
    def craftSword(self):
        if (self.ironIngot>=30):
            self.ironIngot -=30
            self.items[2][1]+=1
    
    