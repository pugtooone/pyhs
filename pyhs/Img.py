from PIL import Image
from importlib import resources
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
    def _access_json(brand):
        with resources.open_text('Resources', 'BrandDatabase.json') as brandJsonFile:
            brandJson = json.load(brandJsonFile)
        try:
            return brandJson[brand]
        except KeyError:
            raise NoBrandDataException

    def check_img_spec(self, brand):
        try:
            Img.brandImgSpec = Img._access_json(brand)['Spec']
        except NoBrandDataException:
            print('No brand data for {}'.format(brand))
            return None
        # self.wrongSpecList = [] #change to dictionary with key as img, value as specs

        for img in self.imgPathList:
            with Image.open(img) as imgObj:
                for spec, value in Img.brandImgSpec.items():
                    if str(eval(f'imgObj.{spec}')) != value:
                        checkDir = img.parent / 'Check Required'
                        checkDir.mkdir(exist_ok=True)
                        try:
                            shutil.move(img, checkDir)
                        except shutil.Error:
                            pass
                        # self.wrongSpecList.append(img)

    def check_img_name(self, brand):
        try:
            Img.brandCorName = Img._access_json(brand)['Name']
        except NoBrandDataException:
            print('No brand data for {}'.format(brand))
            return None

        corName = re.compile(r'{}'.format(Img.brandCorName))
        # self.wrongNameList = []

        for imgPath in self.imgPathList:
            img = imgPath.name
            if not corName.fullmatch(img.lower()):
                checkDir = imgPath.parent / 'Check Required'
                checkDir.mkdir(exist_ok=True)
                try:
                    shutil.move(imgPath, checkDir)
                except shutil.Error:
                    pass
                # self.wrongNameList.append(img)

    def get_product_list(self, brand):
        #raise exception if no brand data
        try:
            Img.brandCorName = Img._access_json(brand)['Name']
        except NoBrandDataException:
            print('No brand data for {}'.format(brand))
            return None

        corName = re.compile(r'{}'.format(Img.brandCorName))
        self.productShotList = {}

        for img in self.imgNameList:
            #raise exception when file naming is wrong, or re.compile is wrong
            try:
                print(img)
                product = corName.fullmatch(img.lower()).group(1)
            except AttributeError:
                raise Exception('Wrong file naming or Wrong RE')

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
            self.prodCount = len(self.get_product_list(brand).keys())
        except NoBrandDataException:
            self.prodCount = 'NA'
        finally:
            return self.prodCount

class NoBrandDataException(Exception):
    pass
