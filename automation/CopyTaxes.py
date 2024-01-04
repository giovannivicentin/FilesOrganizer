import os
import shutil
import dotenv as env

env.load_dotenv()


class CopyTaxes:
    def __init__(self):
        self.baseTaxesPath = env.get("BASE_TAXES_PATH")
        self.finalDestiny = env.get("FINAL_DESTINY")

    def copyFiles(self, sourceDestiny, monthCompetence, typeTax):
        if not os.path.exists(sourceDestiny):
            raise FileNotFoundError("Directory " + sourceDestiny + " not found.")

        if not os.path.exists(self.finalDestiny):
            raise FileNotFoundError("Directory " + self.finalDestiny + " not found.")

        # loop through all subfolders of the source folder
        for root, dirs, taxesFiles in os.walk(sourceDestiny):
            for taxesFile in taxesFiles:
                # check if the file name contains the specified pattern
                if f"-{monthCompetence}-{typeTax}" in taxesFile:
                    # copy the file to the destination folder
                    sourceFilePath = os.path.join(root, taxesFile)
                    finalFilePath = os.path.join(self.finalDestiny, taxesFile)
                    shutil.copy2(sourceFilePath, finalFilePath)

    def copyFgts(self):
        self.sourceDestiny = os.path.join(self.baseTaxesPath, "RPA GFIP")
        monthCompetence = input(
            'You choose FGTS\nPut the month with 2 digits and the year with 4.\nFor example "082025"\nEnter the value to search for: '
        )
        self.copyFiles(
            sourceDestiny=self.sourceDestiny,
            monthCompetence=monthCompetence,
            typeTax="GRF",
        )

    def copyDarfFederal(self):
        self.sourceDestiny = os.path.join(self.baseTaxesPath, "RPA DCTFWEB")
        monthCompetence = input(
            'You choose DARF Federal\nPut the month with 2 digits and the year with 4.\nFor example "082025"\nEnter the value to search for: '
        )
        self.copyFiles(
            sourceDestiny=self.sourceDestiny,
            monthCompetence=monthCompetence,
            typeTax="Guia",
        )

    def copyReciboDarfFederal(self):
        self.sourceDestiny = os.path.join(self.baseTaxesPath, "RPA DCTFWEB")
        monthCompetence = input(
            'You choose Recibo DARF Federal\nPut the month with 2 digits and the year with 4.\nFor example "082025"\nEnter the value to search for: '
        )
        self.copyFiles(
            sourceDestiny=self.sourceDestiny,
            monthCompetence=monthCompetence,
            typeTax="Recibo",
        )
