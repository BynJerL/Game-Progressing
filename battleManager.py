from fighter import Fighter

class BattleManager:
    def __init__(self, playerFighter: Fighter, monsterFighter: Fighter):
        self.playerFighter = playerFighter
        self.monsterFighter = monsterFighter
        self.winner = None
        self.turnCount = 1
        self.isPlayerTurn = True
        self.isRunning = True

    def startBattle(self):
        print("Battle started!")
        
    def battleLoop(self):
        if self.isPlayerTurn:
            print(f"Turn #{self.turnCount}")
            damage = self.playerFighter.attack(self.monsterFighter)
            input(f"{self.playerFighter.name} (HP: {self.playerFighter.currHealth}/{self.playerFighter.maxHealth}) dealt {damage} damage to {self.monsterFighter.name}")
            if not self.monsterFighter.isAlive():
                self.winner = self.playerFighter
                self.isRunning = False
            else:
                self.isPlayerTurn = False
        else:
            damage = self.monsterFighter.attack(self.playerFighter)
            input(f"{self.monsterFighter.name} (HP: {self.monsterFighter.currHealth}/{self.monsterFighter.maxHealth}) dealt {damage} damage to {self.playerFighter.name}")
            if not self.playerFighter.isAlive():
                self.winner = self.monsterFighter
                self.isRunning = False
            else:
                self.isPlayerTurn = True
                self.turnCount += 1

        if self.isRunning:
            self.battleLoop()
        else:
            self.endBattle()

    def endBattle(self):
        print("Battle ended!")
        print(f"Winner: {self.winner.name}")