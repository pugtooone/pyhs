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
            return brandJson['Not Specified']

    def check_img_spec(self, brand):
        Img.brandImgSpec = Img._access_json(brand)['Spec']
        # self.wrongSpecList = [] #change to dictionary with key as img, value as specs

        for img in self.imgPathList:
            with Image.open(img) as imgObj:
                for spec, value in Img.brandImgSpec.items():
                    if str(eval(f'imgObj.{spec}')) != value:
                        checkDir = self.imgDir / 'Check Required'
                        checkDir.mkdir(exist_ok=True)
                        shutil.move(img, checkDir)
                        # self.wrongSpecList.append(img)

    def check_img_name(self, brand):
        Img.brandCorName = Img._access_json(brand)['Name']
        corName = re.compile(r'{}'.format(Img.brandCorName))
        # self.wrongNameList = []

        for imgPath in self.imgPathList:
            img = imgPath.name
            if not corName.fullmatch(img):
                checkDir = self.imgDir / 'Check Required'
                checkDir.mkdir(exist_ok=True)
                shutil.move(imgPath, checkDir)
                # self.wrongNameList.append(img)

    def get_product_list(self, brand):
        Img.brandCorName = Img._access_json(brand)['Name']
        corName = re.compile(r'{}'.format(Img.brandCorName))
        self.productShotList = {}

        for img in self.imgNameList:

            #ignore img with wrong naming
            if self.check_img_name(brand) != None and img in self.check_img_name(brand):
                continue

            product = corName.fullmatch(img).group(1)
            if not product in self.productShotList:
                self.productShotList.update({product:{'shot': 1, 'comp': 0}})
            else:
                self.productShotList[product]['shot'] += 1
            if 'COMP' in img or 'INSERT' in img:
                self.productShotList[product]['comp'] += 1

        #actual shot count
        for product in self.productShotList.keys():
            self.productShotList[product]['shot'] -= self.productShotList[product]['comp']

        return self.productShotList

    def get_product_count(self, brand):
        return len(self.get_product_list(brand).keys())
