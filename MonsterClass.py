from random import randint
class Goblin:
    HP=0
    ATK=0
    POS=[]
    EXP = randint(2,3)
    def __init__(self,ATK=1,HP=3):
        self.ATK = ATK
        self.HP = HP
        #self.POS=POS
    
    def takeDamage(self,damage):
        if (self.HP>0):
            self.HP-=damage
    def showHP(self):
        return self.HP
    def showATK(self):
        return self.ATK
    def showEXP(self):
        return self.EXP
class HobGoblin:
    HP=0
    ATK=0
    POS=[]
    EXP = randint(5,8)
    def __init__(self,ATK=1,HP=3):
        self.ATK = ATK
        self.HP = HP
        #self.POS=POS
    
    def takeDamage(self,damage):
        if (self.HP>0):
            self.HP-=damage
    def showHP(self):
        return self.HP
    def showATK(self):
        return self.ATK
    def showEXP(self):
        return self.EXP