from pathlib import Path
from tkinter.filedialog import askdirectory
from ToSend import ToSend

def main():
    jobFolder = Path(askdirectory())
    toSendFolder = ToSend(jobFolder)
    docItems = toSendFolder.get_doc_items()
    print(docItems)

if __name__ == '__main__':
    main()
