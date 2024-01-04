from automation.Doing import Doing
from automation.Done import Done
from automation.CopyTaxes import CopyTaxes
from automation.Quit import Quit
from automation.Rename import Rename

rename = Rename()
doing = Doing()
done = Done()
copyTaxes = CopyTaxes()
quitAutomation = Quit()

print(
    "Choose an option: \n\n1. Move local files to doing folder.\n2. Move doing folder files to done folder.\n3. Copy Tax files to local folder.\n4. Exit the automation."
)
choice = input('Enter your option "1", "2", "3" or "4": ')
rename.replace_spaces()

if choice == "1":
    doing.moveAll()
elif choice == "2":
    done.moveAll()
elif choice == "3":
    print(
        "Choose a suboption:\n\n1. FGTS\n2. DARF Federal\n3. Recibo DARF Federal\n4. Exit the automation"
    )
    subchoice = input('Enter your option "1", "2", "3" or "4": ')
    if subchoice == "1":
        copyTaxes.copyFgts()
    elif subchoice == "2":
        copyTaxes.copyDarfFederal()
    elif subchoice == "3":
        copyTaxes.copyReciboDarfFederal()
    elif subchoice == "4":
        quitAutomation.execute()
    else:
        print("Invalid choice.")
elif choice == "4":
    quitAutomation.execute()
else:
    print("Invalid choice.")
