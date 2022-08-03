from pathlib import Path
from tkinter.filedialog import askdirectory
from JobDir import JobDir
#from ToSend import ToSend

def main():
    jobFolder = Path(askdirectory())
    jobDirFolder = JobDir(jobFolder)
    jobDirFolder.check_img_spec()

if __name__ == '__main__':
    main()
