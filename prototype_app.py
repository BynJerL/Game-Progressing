class MainApp:
    def __init__(self):
        self.playerName = None
        self.playerLevel = None
        self.playerPoint = None

    def initialRun(self):
        self.playerName = input("Insert your name: ")
        self.playerLevel = 1
        self.playerPoint = 0

        print("Your current status:")
        self.printPlayerStatus()
    
    def printPlayerStatus(self):
        print(f"playerName: {self.playerName}")
        print(f"playerLevel: {self.playerLevel}")
        print(f"playerPoint: {self.playerPoint}")

if __name__ == "__main__":
    root = MainApp()
    root.initialRun()