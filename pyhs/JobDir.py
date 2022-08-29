from Img import Img
from Doc import Doc
from ProductionPlan import ProductionPlan
from ShotList import ShotList
from FileTransmitter import FileTransmitter
from datetime import date
from pathlib import Path
import os
import shutil
import sys
import pyperclip

class JobDir:
    #class attributes
    #server client folders as brand list
    brandBaseDir = Path('/Volumes/Studio/CLIENTS/')
    brandBase = os.listdir(brandBaseDir)
    brandBase.extend(['OnTheList', 'MBG', 'Agnes b'])

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
    No. of Products: {self.get_product_count()}
    No. of Images: {self.get_img_count()}
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

    def get_img_count(self):
        return self.imgDirObj.get_total_img_count()

    def get_cat_img_count(self):
        return self.imgDirObj.get_cat_img_count()

    def get_product_list(self):
        return self.imgDirObj.get_product_list(self.get_brand())

    def get_product_count(self):
        return self.imgDirObj.get_product_count(self.get_brand())

    def check_img_spec(self):
        return self.imgDirObj.check_img_spec(self.get_brand())

    def check_img_name(self):
        return self.imgDirObj.check_img_name(self.get_brand())
    
    def write_summary(self):
        self.productList = self.get_product_list()
        self.prodCount = self.get_product_count()

        with open(self.jobDir / str(self.jobName + ' Summary'), 'a') as sumFile:
            sumFile.write('%s Summary\n\nNo. of products: %s\n' % (self.jobName, self.prodCount))
            if self.productList != None:
                for key, value in self.productList.items():
                    sumFile.write('''\n%s:
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
        #only run if shotlist of the brand is accessible
        if self.shotListObj != None:
            self.shotListObj.fill_qc_tab(str(self.get_img_count() + 1), self.get_img_list())
        pass


class ToSend(JobDir):
    def __init__(self, directory):
        super().__init__(directory)
        self._check_dir_structure(directory)
        
    @staticmethod
    def get_today_out_job():
        return ProductionPlan.get_today_out_job()

    def run(self):
        self.check_img_spec()
        self.check_img_name()
        self.display()
        self.fill_qc_tab()
        self.fill_prod_plan()
        self.update_job_status('Retouching')
        self.write_email()
        self.write_summary()

    def _check_dir_structure(self, directory):
        jobDirls = os.listdir(directory)
        if 'Images' in jobDirls and 'Documents' in jobDirls:
            pass
        else:
            #could change to return boolean, then a restructure function
            print('Error: wrong folder structure')
            sys.exit(2)

    def check_img_spec(self):
        return self.imgDirObj.check_img_spec('ToSend')

    def fill_prod_plan(self):
        return self.prodPlanObj.fill_prod_plan(self.get_product_count(), self.get_cat_img_count())

    def write_email(self):
        self.imgCount = self.get_img_count()
        self.docItems = self.get_doc_items()
        self.email = f'Hi!\n\nPlease note that {self.jobName} is being uploaded to the server, including {self.imgCount} images along with {self.docItems}. Let me know if there is any question. Thanks!\n\n'
        pyperclip.copy(self.email)
        print('\nEmail Template Copied')

class QC(JobDir):
    mainQCDir = Path.home() / 'Desktop/QCing'
    mainQCDir.mkdir(exist_ok=True)

    def __init__(self, directory):
        super().__init__(directory)

    # # __init__() without enduser downloading their own job
    # def __init__(self):
        # directory = self.startup()
        # super().__init__(directory)

    def startup(self):
        """
        startup function run before calling super().__init__()
        as jobDir does not exist yet
        """
        self.jobName = ""
        self.qcDuty = QC.get_qc_duty()
        option = {}
        #print job option for qc to choose
        for index, jobName in enumerate(self.qcDuty):
            option.update({index: jobName})
            print('{}: {}'.format(index, jobName))

        while not self.jobName:
            try:
                choice = input('Enter your job:\n')
                self.jobName = self.qcDuty[int(choice)]
            except IndexError:
                print('Invalid input')
                continue

        self.prodPlanObj = ProductionPlan(self.jobName)
        if self.check_download():
            print('Job is already downloaded')
            sys.exit()

        self.vendor = self.get_vendor()
        QC.download_job(self.vendor, self.jobName)
        return FileTransmitter.TBQ / self.jobName

    def run(self):
        self.update_job_status('QCing')
        self.mv_to_QCing()
        self.check_img_spec()
        self.check_img_name()
        # self.write_summary()
        self.display()

    def check_download(self):
        return self.prodPlanObj.check_download()

    def mv_to_QCing(self):
        dateStr = date.today().strftime('%Y%m%d')
        newjobDir = self.jobDir.parent / f'{dateStr} {self.jobDir.name}'
        shutil.move(self.jobDir, newjobDir)
        self.jobDir = newjobDir
        shutil.move(self.jobDir, QC.mainQCDir)

    @staticmethod
    def get_qc_duty():
        """
        static method to get the qc duty (since no job dir yet)
        """
        qc_id = input('Enter your name: ')
        qcDutyList = ProductionPlan.get_qc_duty(qc_id)
        return qcDutyList

    @staticmethod
    def download_job(vendor, job):
        """
        static method to download the jobDir (which does not exist on the end user's os yet)
        """
        if vendor == 'CutOut' or vendor == 'Schnell':
            FileTransmitter(vendor, job).download_ftp_job()
        elif vendor == 'Dresma':
            pass
        elif vendor == 'Adnet':
            pass
