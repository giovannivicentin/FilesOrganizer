import os
import shutil
from typing import Dict
import dotenv as env

env.load_dotenv()


class Done:
    def __init__(self):
        self.baseDoingPath = env.get("BASE_DOING_PATH")
        self.baseDonePath = env.get("BASE_DONE_PATH")
        self.categories: Dict[str, str] = {
            "FGTS": "FGTS",
            "DARF Federal": "DARF Federal",
            "AvisosVencimento": "AvisosVencimento",
            "DAE": "DAE",
            "Extratos": "Extratos",
            "ExtratosA": "ExtratosA",
            "Ferias": "Ferias",
            "Holerites": "Holerites",
            "HoleritesA": "HoleritesA",
            "Liquidos": "Liquidos",
            "LiquidosA": "LiquidosA",
        }

    def moveFilesByCategory(self, category: str):
        sourceDestiny = os.path.join(self.baseDoingPath, category)
        finalDestiny = os.path.join(self.baseDonePath, category)

        if not os.path.exists(sourceDestiny):
            raise FileNotFoundError(f"Directory {sourceDestiny} not found.")

        if not os.path.exists(finalDestiny):
            raise FileNotFoundError(f"Directory {finalDestiny} not found.")

        archiveFiles = os.listdir(sourceDestiny)

        for archiveFile in archiveFiles:
            sourceFile = os.path.join(sourceDestiny, archiveFile)
            destinationFile = os.path.join(finalDestiny, archiveFile)

            shutil.move(sourceFile, destinationFile)
            print(f"{archiveFile} moved.")

    def moveAll(self):
        for category in self.categories.values():
            self.moveFilesByCategory(category)

        print("All items have been successfully moved!")
