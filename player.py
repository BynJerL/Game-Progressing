class Player:
    def __init__(self, name, level=1, point=0, currentHealth=150, maxHealth=150, power=20, currentExp=0, limitExp=150):
        self.name = name
        self.level = level
        self.point = point
        self.currentHealth = currentHealth
        self.maxHealth = maxHealth
        self.power = power
        self.currentExp = currentExp
        self.limitExp = limitExp
    
    def getMaxHealCost(self):
        return int((self.maxHealth - self.currentHealth) * 1.25)