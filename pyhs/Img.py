from PIL import Image
from importlib import resources
import os
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

    def get_comp_count(self):
        self.compCount = 0
        for img in self.imgNameList:
            if 'comp' in img.lower() or 'insert' in img.lower():
                self.compCount += 1
        return self.compCount

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
    def _access_brand_spec(brand, spec, special=None):
        if special != None:
            brand = f'{brand} {special}'
        with resources.open_text('Resources', 'BrandDatabase.json') as brandJsonFile:
            brandJson = json.load(brandJsonFile)
        try:
            return brandJson[brand][spec]
        except KeyError: #raise exception if no brand data is found
            while True:
                print('There is not brand data, proceed or not? Y/N')
                ans = input()
                if ans.lower() == 'y':
                    return brandJson['Not Specified'][spec]
                elif ans.lower() == 'n':
                    raise NoBrandDataError(brand)

    #internal function to mv the image with wrong attributes to "Check Required" folder
    @staticmethod
    def _mv_to_check(img):
        checkDir = img.parent / 'Check Required'
        checkDir.mkdir(exist_ok=True)
        try:
            shutil.move(img, checkDir)
        except shutil.Error:
            pass

    def check_img_spec(self, brand):

        #parse the subfolders to see if any special job
        imgSubDir = os.listdir(self.imgDir)
        for i in range(len(imgSubDir)):
            imgSubDir[i] = imgSubDir[i].title()
        for job in ('Model', 'Macy'):
            if job in imgSubDir:
                try:
                    Img.brandImgSpec = Img._access_brand_spec(brand, 'Spec', f'{job}')
                except NoBrandDataError:
                    return None
            else:
                try:
                    Img.brandImgSpec = Img._access_brand_spec(brand, 'Spec')
                except NoBrandDataError:
                    return None

        self.wrongSpecList = [] #change to dictionary with key as img, value as specs

        for img in self.imgPathList:
            with Image.open(img) as imgObj:
                #check the bg colour at top left and bottom right
                corBG = int(2)
                for spec, value in Img.brandImgSpec.items():
                    if str(eval(f'imgObj.{spec}')) != value and 'getpixel' not in spec:
                        print(f'{img.name} - {spec} is incorrect')
                        Img._mv_to_check(img)
                        self.wrongSpecList.append(img)
                    if str(eval(f'imgObj.{spec}')) != value and 'getpixel' in spec:
                        corBG -= 1
                        if corBG == 0:
                            print(f'{img.name} - BG colour is incorrect')
                            Img._mv_to_check(img)
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
                Img._mv_to_check(img)
                self.wrongNameList.append(img)

        if self.wrongNameList != []:
            print(f'Wrong file naming for: {self.wrongNameList}')
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

    def export_jpg(self):
        for img in self.imgPathList:
            filename, extension = os.path.splitext(img)
            extension = '.jpg'
            outfile = filename + extension

            with Image.open(img) as imgObj:
                imgObj.save(outfile)

class WrongNamingError(Exception):
    pass

class NoBrandDataError(Exception):
    def __init__(self, brand):
        super().__init__(f'No brand data for {brand}')
