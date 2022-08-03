from PIL import Image
import sys
import re
import json

class Img:
    def __init__(self, directory):
        """
        initialize ImgList obj
        Parameter: Path obj of JobDir
        """
        self.imgDir = directory / 'Images'
        self.imgListIter = self.imgDir.glob('**/*.tif') #Iterator for img

        self.imgNameList = []
        for i in self.imgListIter:
           img = i.name
           self.imgNameList.append(img)

        self.imgPathList = []
        for i in self.imgListIter:
           img = i
           self.imgNameList.append(img)

    def get_img_list(self):
        return self.imgNameList

    def get_img_num(self):
        self.imgNum = len(self.get_img_list())
        return self.imgNum

    @classmethod
    def _access_json(cls, brand):
        with open('Resources/BrandDatabase.json') as brandJsonFile:
            Img.brandJson = json.load(brandJsonFile)
            return Img.brandJson[brand]

    def check_img_spec(self, brand):
        Img.brandImgSpec = Img._access_json(brand)['Spec']
        self.wrongSpecList = [] #change to dictionary with key as img, value as specs

        for img in self.imgPathList:
            with Image.open(self.imgDir / img) as imgObj:
                for spec, value in Img.brandImgSpec.items():
                    if str(eval(f'imgObj.{spec}')) != value:
                        self.wrongSpecList.append(img)
                        # wrongSpec = str(eval(f'imgObj.{spec}'))
                        # print(f'Error: Wrong Image Spec\nimg: {img}\ncorrect spec: {value}\nwrong spec: {wrongSpec}')

        print('All Image Spec Checked')
        if len(self.wrongSpecList) != 0:
            print(self.wrongSpecList)
            sys.exit(1)

    def check_img_name(self, brand):
        Img.brandCorName = Img._access_json(brand)['Name']
        corName = re.compile(r'{}'.format(Img.brandCorName))
        self.wrongNameList = []

        for img in self.imgNameList:
                if not corName.search(img):
                    print(f'Error: Wrong Image Name\nimg: {img}')
                    self.wrongNameList.append(img)

        print('All Image Name Checked')
        if len(self.wrongNameList) != 0:
            print(self.wrongNameList)
            sys.exit(1)
