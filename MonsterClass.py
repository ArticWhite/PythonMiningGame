class Goblin:
    HP=0
    ATK=0
    POS=[]
    def __init__(self,ATK,HP,POS):
        self.ATK = 1
        self.HP = 1
        self.POS=POS
    
    def takeDamage(self,damage):
        if (self.HP>0):
            self.HP-=damage
    def showHP(self):
        return self.HP
    def showATK(self):
        return self.ATK