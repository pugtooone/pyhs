from JobDir import ToSend, QC
from pathlib import Path
from tkinter.filedialog import askdirectory
from AddOns import pdf_extract
import sys

class Menu:
    def __init__(self):
        self.choice={
                     '1': 'self.ToSend',
                     '2': 'self.QC',
                     '3': 'self.Submit',
                     '4': 'self.AddOn',
                     '5': 'self.Quit'
                     }

    def display_menu(self):
        print('''
========================================

        Main Menu

        [1]: To Send
        [2]: QC
        [3]: Submit
        [4]: Add On Functions
        [5]: Quit

========================================
                ''')

    def run(self):
        while True:
            self.display_menu()
            choice = input('Enter your option: ')
            print('')
            action = self.choice.get(choice)
            if action:
                eval(f'{action}()')
            else:
                print('Error: Invalid Option')

    #Main flow
    def ToSend(self):
        jobFolder = Path(askdirectory())
        toSendFolder = ToSend(jobFolder)
        toSendFolder.check_img_spec()
        toSendFolder.check_img_name()
        toSendFolder.write_email()

    def QC(self):
        jobFolder = Path(askdirectory())
        qcFolder = QC(jobFolder)
        qcFolder.check_img_spec()
        qcFolder.check_img_name()

    def AddOn(self):
        self.addOnChoice={
                     '1': 'pdf_extract.main',
                     '2': 'back'
                     }
        while True:
            print("""
========================================

        Add Ons Menu
        [1]: Extract PDF
        [2]: Back

========================================
                    """)
            choice = input('Enter your option: ')
            action = self.addOnChoice.get(choice)
            if choice == '2':
                break
            elif action:
                eval(f'{action}()')
            else:
                print('Error: Invalid Option')

    def Quit(self):
        sys.exit(0)

if __name__ == '__main__':
    Menu().run()
