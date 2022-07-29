from ProductionPlan import ProductionPlan
from pathlib import Path
from tkinter.filedialog import askdirectory
from ToSend import ToSend

def main():
    jobFolder = Path(askdirectory())
    toSendFolder = ToSend(jobFolder)
    prodPlan = ProductionPlan()
    testCell = prodPlan.prodPlan.acell('C691').value
    print(testCell)

if __name__ == '__main__':
    main()
