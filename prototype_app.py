from player import Player
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
            case _:
                print("Menu is not available.")
    
    def getMonsters (self):
        with open("monsterData.json", "r") as file:
            monsters = json.load(file)
        self.monsterList = monsters.get("monsterList", [])

    def actionChoose (self):
        print("What will you do?")
        print("(1) ==> Fight a monster")
        print("(2) ==> Heal [Cost: 0 point(s)]")

        playerChoice = input("Your choice: ")
        match playerChoice:
            case "1":
                self.gameState = "chooseMonster"
            case "2":
                self.gameState = "healSelf"
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