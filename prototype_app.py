from player import Player

class MainApp:
    def __init__(self):
        self.playerData = None
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
            case _:
                print("Menu is not available.")

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
        pass 
    
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