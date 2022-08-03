from Img import Img
from Doc import Doc
from ProductionPlan import ProductionPlan
from pathlib import Path
import os
import sys
import pyperclip

class JobDir:
    # class attributes
    #brandBaseDir = Path('/Volumes/Studio/CLIENTS/')
    #brandBase = os.listdir(brandBaseDir)

    def __init__(self, directory):
        """
        initialize JobDir obj
        Parameter: Path obj of JobDir
        """
        JobDir._check_dir_structure(directory)
        self.jobDir = directory
        self.jobName = directory.name
        self.imgDirObj = Img(self.jobDir)
        self.docDirObj = Doc(self.jobDir)
        self.prodPlanObj = ProductionPlan(self.jobName)

    @classmethod
    def _check_dir_structure(cls, directory):
        jobDirls = os.listdir(directory)
        if 'Images' in jobDirls and 'Documents' in jobDirls:
            pass
        else:
            #could change to return boolean, then a restructure function
            print('Error: wrong folder structure')
            sys.exit(2)

    def get_brand(self):
        for brand in JobDir.brandBase:
            if brand in self.jobName:
                return brand
        return None


    #imgObj
    def get_img_list(self):
        return self.imgDirObj.get_img_list()

    def get_img_num(self):
        return self.imgDirObj.get_img_num()

    def check_img_spec(self):
        return self.imgDirObj.check_img_spec(self.get_brand())

    def check_img_name(self):
        return self.imgDirObj.check_img_name(self.get_brand())

    #docObj
    def get_doc_list(self):
        return self.docDirObj.get_doc_list()

    def get_doc_items(self):
        return self.docDirObj.get_doc_items()


    #prodPlanObj
    def get_vendor(self):
        return self.prodPlanObj.get_vendor()

    def get_job_status(self):
        return self.prodPlanObj.get_job_status()

    def check_download(self):
        return self.prodPlanObj.check_download()


class ToSend(JobDir):
    def __init__(self, directory):
        super().__init__(directory)

    def write_email(self):
        self.imgNum = self.get_img_num()
        self.docItems = self.get_doc_items()
        self.email = f'Hi!\n\nPlease note that {self.jobName} is being uploaded to the server, including {self.imgNum} images along with {self.docItems}. Let me know if there is any question. Thanks!\n\n'
        pyperclip.copy(self.email)
        print('email template copied')

    def check_img_spec(self):
        return self.imgDirObj.check_img_spec('ToSend')
