import os

class DeployAgent:
    def package_game(self):
        print("[DeployAgent] 📦 Building .zip package...")
        os.system("zip -r game_build.zip game.py assets/")
