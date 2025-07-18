class Fighter:
    def __init__(self, name: str, health: int, maxHealth: int, power: int):
        self.name = name
        self.currHealth = health
        self.maxHealth = maxHealth
        self.power = power