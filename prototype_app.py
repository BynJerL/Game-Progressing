from player import Player

class MainApp:
    def __init__(self):
        self.playerData = None

    def initialRun(self):
        playerName = input("Insert your name: ")
        self.playerData = Player(name=playerName)

        print("Your current status:")
        self.printPlayerStatus()
    
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