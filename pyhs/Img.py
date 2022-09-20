from PIL import Image
from importlib import resources
from glob import glob
import sys
import shutil
import re
import json

class Img:

    imgCat = ('Model', 'Flatlay', 'Mannequin', 'Still', 'Jewel')

    def __init__(self, directory):
        """
        initialize ImgList obj
        Parameter: Path obj of JobDir
        """
        self.imgDir = directory / 'Images'
        if not self.imgDir.is_dir():
            self.imgDir.mkdir()
            stuffs = glob(f'{directory}/*')
            for stuff in stuffs:
                shutil.move(f'{stuff}', f'{self.imgDir}')
        self.imgListIter = self.imgDir.glob('**/*.tif') #Iterator for img

        self.imgPathList = []
        for i in self.imgListIter:
           self.imgPathList.append(i)

        self.imgNameList = []
        for i in self.imgPathList:
           img = i.name
           self.imgNameList.append(img)

    def get_img_list(self):
        return self.imgNameList

    def get_total_img_count(self):
        self.imgNum = len(self.get_img_list())
        return self.imgNum

    def get_cat_img_count(self):
        imgNumDict = {}
        for cat in Img.imgCat:
            imgCatDir = self.imgDir / cat
            catImgList = []
            for i in imgCatDir.glob('**/*.tif'):
                img = i.name
                catImgList.append(img)
            imgNumDict.update({cat: len(catImgList)})
        return imgNumDict

    @staticmethod
    def _access_brand_spec(brand, spec):
        with resources.open_text('Resources', 'BrandDatabase.json') as brandJsonFile:
            brandJson = json.load(brandJsonFile)
        try:
            return brandJson[brand][spec]
        except KeyError:
            raise NoBrandDataError(brand)

    def check_img_spec(self, brand):
        try:
            Img.brandImgSpec = Img._access_brand_spec(brand, 'Spec')
        except NoBrandDataError:
            return None
        self.wrongSpecList = [] #change to dictionary with key as img, value as specs

        for img in self.imgPathList:
            with Image.open(img) as imgObj:
                for spec, value in Img.brandImgSpec.items():
                    if str(eval(f'imgObj.{spec}')) != value:
                        print(f'{img.name} - {spec} is incorrect')
                        checkDir = img.parent / 'Check Required'
                        checkDir.mkdir(exist_ok=True)
                        try:
                            shutil.move(img, checkDir)
                        except shutil.Error:
                            pass
                        self.wrongSpecList.append(img)
        if self.wrongSpecList != []:
            print('Wrong file spec')
            sys.exit(1)

    def check_img_name(self, brand):
        try:
            Img.brandCorName = Img._access_brand_spec(brand, 'Name')
        except NoBrandDataError:
            return None

        corName = re.compile(r'{}'.format(Img.brandCorName))
        self.wrongNameList = []

        for imgPath in self.imgPathList:
            img = imgPath.name
            img = img.replace('comp', 'COMP')
            img = img.replace('insert', 'INSERT')
            if corName.fullmatch(img) == None:
                self.wrongNameList.append(img)
                checkDir = imgPath.parent / 'Check Required'
                checkDir.mkdir(exist_ok=True)
                try:
                    shutil.move(imgPath, checkDir)
                except shutil.Error:
                    pass
                # self.wrongNameList.append(img)
        if self.wrongNameList != []:
            print('Wrong file naming')
            sys.exit(1)

    def get_product_list(self, brand):
        try:
            Img.brandCorName = Img._access_brand_spec(brand, 'Name')
        except NoBrandDataError:
            return None

        corName = re.compile(r'{}'.format(Img.brandCorName))
        self.productShotList = {}

        for img in self.imgNameList:
            img = img.replace('comp', 'COMP')
            img = img.replace('insert', 'INSERT')
            #raise exception when file naming is wrong, or re.compile is wrong
            #need fix since one wrong name will make all wrong
            try:
                product = corName.fullmatch(img).group(1)
            except AttributeError:
                raise WrongNamingError(img)

            if not product in self.productShotList:
                self.productShotList.update({product:{'shot': 1, 'comp': 0}})
            else:
                self.productShotList[product]['shot'] += 1
            if 'comp' in img.lower() or 'insert' in img.lower():
                self.productShotList[product]['comp'] += 1

        #actual shot count
        for product in self.productShotList.keys():
            self.productShotList[product]['shot'] -= self.productShotList[product]['comp']

        return self.productShotList

    def get_product_count(self, brand):
        try:
            if self.get_product_list(brand) == None:
                self.prodCount = 'NA (No Brand Data)'
            self.prodCount = len(self.get_product_list(brand).keys())
        except WrongNamingError:
            self.prodCount = 'NA (Wrong Naming)'
        finally:
            return self.prodCount

class WrongNamingError(Exception):
    pass

class NoBrandDataError(Exception):
    def __init__(self, brand):
        super().__init__(f'No brand data for {brand}')
