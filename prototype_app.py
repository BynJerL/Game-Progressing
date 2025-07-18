from player import Player
from fighter import Fighter
from battleManager import BattleManager
import json

class MainApp:
    def __init__(self):
        self.playerData = None
        self.monsterData = None
        self.monsterList = []
        self.gameState = None

    def initialRun(self):
        playerName = input("Insert your name: ")
        self.playerData = Player(name=playerName)

        print("Your current status:")
        self.printPlayerStatus()
        self.gameState = "actionChoose"
        self.stateRouter()
    
    def stateRouter (self):
        print()
        match self.gameState:
            case "actionChoose":
                self.actionChoose()
            case "chooseMonster":
                self.chooseMonster()
            case "healSelf":
                self.healSelf()
            case "battle":
                self.battle()
            case _:
                print("Menu is not available.")
    
    def getMonsters (self):
        with open("monsterData.json", "r") as file:
            monsters = json.load(file)
        self.monsterList = monsters.get("monsterList", [])

    def actionChoose (self):
        healCost = min(self.playerData.point, self.playerData.getMaxHealCost())

        print("What will you do?")
        print("(1) ==> Fight a monster")
        print(f"(2) ==> Heal [Cost: {healCost} point(s)]")

        playerChoice = input("Your choice: ")
        match playerChoice:
            case "1":
                self.gameState = "chooseMonster"
            case "2":
                self.gameState = "healSelf"
        self.stateRouter()
    
    def healSelf(self):
        healCost = min(self.playerData.point, self.playerData.getMaxHealCost())
        self.playerData.point -= healCost
        healPower = int(0.8 * healCost)
        self.playerData.currentHealth = min(self.playerData.currentHealth + healPower, self.playerData.maxHealth)
        print(f"You have restored {healPower} HP\n")
        self.printPlayerStatus()
        self.gameState = "actionChoose"
        self.stateRouter()

    def chooseMonster(self):
        print("Pick your opponent:")
        self.getMonsters()
        for i, monster in enumerate(self.monsterList):
            print(f"({i + 1}) ==> {monster['name']} (Health: {monster['health']}, Power: {monster['power']})")
        
        playerChoice = input("Your choice: ")
        try:
            monsterIndex = int(playerChoice) - 1
            if 0 <= monsterIndex < len(self.monsterList):
                self.monsterData = self.monsterList[monsterIndex]
                print(f"You have chosen {self.monsterData['name']}.")
                self.gameState = "battle"
            else:
                print("Invalid choice. Please try again.")
            
            self.stateRouter()
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    def battle(self):
        playerFighter = Fighter(
            name=self.playerData.name,
            health=self.playerData.currentHealth,
            maxHealth=self.playerData.maxHealth,
            power=self.playerData.power
        )
        monsterFighter = Fighter(
            name=self.monsterData['name'],
            health=self.monsterData['health'],
            maxHealth=self.monsterData['health'],
            power=self.monsterData['power']
        )

        print(f"A battle has started between {playerFighter.name} and {monsterFighter.name}!")

        battleManager = BattleManager(playerFighter=playerFighter, monsterFighter=monsterFighter)
        battleManager.startBattle()
        
        while battleManager.isRunning:
            battleManager.battleLoop()
        
        if battleManager.winner == playerFighter:
            gainedExp = self.monsterData['expGain']
            gainedPoint = self.monsterData['pointGain']
            self.playerData.currentExp += gainedExp
            self.playerData.point += gainedPoint
            self.playerData.currentHealth = battleManager.playerFighter.currHealth
            input(f"You got {gainedExp} Exp and {gainedPoint} Point(s)")
            self.gameState = "actionChoose"
            self.printPlayerStatus()
        else:
            self.gameState = "gameOver"
            print("Game Over!")
        self.stateRouter()

    def printPlayerStatus(self):
        print(f"playerName: {self.playerData.name}")
        print(f"playerLevel: {self.playerData.level}")
        print(f"playerPoint: {self.playerData.point}")
        print(f"playerExp: {self.playerData.currentExp}/{self.playerData.limitExp}")
        print(f"playerHp: {self.playerData.currentHealth}/{self.playerData.maxHealth}")
        print(f"playerPower: {self.playerData.power}")

if __name__ == "__main__":
    root = MainApp()
    root.initialRun()