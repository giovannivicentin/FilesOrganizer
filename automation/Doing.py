import os
import shutil
from datetime import datetime
import dotenv as env

env.load_dotenv()


class Doing:
    def __init__(self):
        self.sourceDestiny = env.get("SOURCE_DESTINY")
        self.basePath = env.get("BASE_DOING_PATH")

    def moveFiles(self, sourceDestiny, finalDestiny, fileName, numberOfName):
        if not os.path.exists(sourceDestiny):
            raise FileNotFoundError(f"Directory {sourceDestiny} not found.")

        if not os.path.exists(finalDestiny):
            raise FileNotFoundError(f"Directory {finalDestiny} not found.")

        for verifyName in os.listdir(sourceDestiny):
            if fileName in verifyName and verifyName.count("-") >= numberOfName:
                parts = verifyName.split("-")
                newVerifyName = (
                    "-".join(parts[:numberOfName])
                    + "-"
                    + "-".join(parts[numberOfName:])
                )
                sourcePath = os.path.join(sourceDestiny, verifyName)
                destinationPath = os.path.join(finalDestiny, newVerifyName)
                shutil.move(sourcePath, destinationPath)
                print(f"{newVerifyName} moved.")

    def moveFilesByCondition(self, fileName, numberOfName, folderName):
        finalDestiny = os.path.join(self.basePath, folderName)
        self.moveFiles(
            sourceDestiny=self.sourceDestiny,
            finalDestiny=finalDestiny,
            fileName=fileName,
            numberOfName=numberOfName,
        )

    def moveFgts(self):
        self.moveFilesByCondition("GRF", 2, "FGTS")

    def moveDarfFederal(self):
        self.moveFilesByCondition("Guia", 2, "DARF Federal")

    def moveAvisosDeVencimento(self):
        self.moveFilesByCondition("AV", 1, "AvisosVencimento")

    def moveDaeDomestica(self):
        self.moveFilesByCondition("DAE", 1, "DAE")

    def moveProgramacaoDeFerias(self):
        self.moveFilesByCondition("ProgramaçãodeFérias", 1, "Ferias")

    def moveHoleriteMensal(self):
        currentDay = datetime.now().day
        if currentDay >= 21 or currentDay <= 7:
            self.moveFilesByCondition("RecibodePagamento", 1, "Holerites")
        elif currentDay >= 8 and currentDay <= 20:
            self.moveFilesByCondition("RecibodePagamento", 1, "HoleritesA")

    def moveExtratoMensal(self):
        currentDay = datetime.now().day
        if currentDay >= 21 or currentDay <= 7:
            self.moveFilesByCondition("ExtratoMensal", 1, "Extratos")
        elif currentDay >= 8 and currentDay <= 20:
            self.moveFilesByCondition("ExtratoMensal", 1, "ExtratosA")

    def moveRelatorioDeLiquidos(self):
        currentDay = datetime.now().day
        if currentDay >= 21 or currentDay <= 7:
            self.moveFilesByCondition("RelatóriodeLíquidos", 1, "Liquidos")
        else:
            self.moveFilesByCondition("RelatóriodeLíquidos", 1, "LiquidosA")

    def moveAll(self):
        self.moveFgts()
        self.moveDarfFederal()
        self.moveAvisosDeVencimento()
        self.moveDaeDomestica()
        self.moveProgramacaoDeFerias()
        self.moveHoleriteMensal()
        self.moveExtratoMensal()
        self.moveRelatorioDeLiquidos()
        print("All items have been successfully moved!")
