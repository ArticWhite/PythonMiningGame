from random import randint
class Goblin:
    HP=0
    ATK=0
    EXP = randint(2,3)
    def __init__(self,ATK=1,HP=3):
        self.ATK = ATK
        self.HP = HP
    
    def takeDamage(self,damage):
        if (self.HP>0):
            self.HP-=damage
    def showHP(self):
        return self.HP
    def showATK(self):
        return self.ATK
    def showEXP(self):
        return self.EXP
class HobGoblin(Goblin):
    HP=0
    ATK=0
    EXP = randint(5,8)
    def __init__(self,ATK=3,HP=8):
         super().__init__(ATK,HP)
class Troll(Goblin):
    HP=0
    ATK=0
    EXP = randint(12,20)
    def __init__(self,ATK=6,HP=12):
        super().__init__(ATK,HP)
