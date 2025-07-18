class Fighter:
    def __init__(self, name: str, health: int, maxHealth: int, power: int):
        self.name = name
        self.currHealth = health
        self.maxHealth = maxHealth
        self.power = power

    def takeDamage(self, amount):
        self.currHealth = max(0, self.currHealth - amount)

    def attack(self, target: 'Fighter'):
        damage = self.power
        target.takeDamage(damage)
        return damage
    
    def isAlive(self):
        return self.currHealth > 0