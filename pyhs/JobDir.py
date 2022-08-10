from Img import Img
from Doc import Doc
from ProductionPlan import ProductionPlan
from ShotList import ShotList
from pathlib import Path
import os
import sys
import pyperclip

class JobDir:
    # class attributes
    brandBaseDir = Path('/Volumes/Studio/CLIENTS/')
    brandBase = os.listdir(brandBaseDir)
    # brandBase = ['OnTheList', 'Arena', 'Kipling']

    def __init__(self, directory):
        """
        initialize JobDir obj
        Parameter: Path obj of JobDir
        """
        self.jobDir = directory
        self.jobName = directory.name
        self.imgDirObj = Img(self.jobDir)
        self.docDirObj = Doc(self.jobDir)
        self.prodPlanObj = ProductionPlan(self.jobName)
        self.shotListObj = ShotList(self.get_brand())

    #menu display for CLI (not for gui)
    def display(self):
        print(f"""====================================================================================================
    Job Directory Information
----------------------------------------------------------------------------------------------------
    Job: {self.jobName}
    Number of Images: {self.get_img_num()}
====================================================================================================
                """)

    def get_brand(self):
        for brand in JobDir.brandBase:
            if brand in self.jobName:
                return str(brand)
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
    
    def write_summary(self):
        self.productList = self.imgDirObj.get_product_list(self.get_brand())
        with open(self.jobDir / str(self.jobName + ' Summary'), 'a') as prodFile:
            prodFile.write('%s Summary\n' % (self.jobName))
            for key, value in self.productList.items():
                prodFile.write('''\n%s:
No. of shots: %s
No. of comps: %s\n''' % (key, value['shot'], value['comp']))


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

    def update_job_status(self, stage):
        return self.prodPlanObj.update_job_status(stage)


    #shotListObj
    def fill_qc_tab(self):
        self.shotListObj.fill_qc_tab()

class ToSend(JobDir):
    def __init__(self, directory):
        super().__init__(directory)
        self._check_dir_structure(directory)
        
    def run(self):
        self.check_img_spec()
        self.check_img_name()
        # self.fill_qc_tab()
        self.write_summary()
        self.write_email()
        self.update_job_status('Retouching')
        self.display()

    def _check_dir_structure(self, directory):
        jobDirls = os.listdir(directory)
        if 'Images' in jobDirls and 'Documents' in jobDirls:
            pass
        else:
            #could change to return boolean, then a restructure function
            print('Error: wrong folder structure')
            sys.exit(2)

    def write_email(self):
        self.imgNum = self.get_img_num()
        self.docItems = self.get_doc_items()
        self.email = f'Hi!\n\nPlease note that {self.jobName} is being uploaded to the server, including {self.imgNum} images along with {self.docItems}. Let me know if there is any question. Thanks!\n\n'
        pyperclip.copy(self.email)
        print('\nEmail Template Copied')

    def check_img_spec(self):
        return self.imgDirObj.check_img_spec('ToSend')

class QC(JobDir):
    def __init__(self, directory):
        super().__init__(directory)

    def run(self):
        self.check_download()
        self.check_img_spec()
        self.check_img_name()
        self.display()

    def check_download(self):
        return self.prodPlanObj.check_download()

    def download_batch(self):
        pass
