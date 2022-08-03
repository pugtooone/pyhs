from PIL import Image
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

    def check_img_spec(self, brand):
        Img.brandJsonFile = open('Resources/BrandDatabase.json')
        Img.brandJson = json.load(Img.brandJsonFile)
        Img.brandData = Img.brandJson[brand]['Spec']

        for img in self.imgPathList:
            imgObj = Image.open(self.imgDir / img)

            for spec, value in Img.brandData.items():
                if str(eval(f'imgObj.{spec}')) != value:
                    wrongSpec = str(eval(f'imgObj.{spec}'))
                    print(f'Error: Wrong Image Spec\nimg: {img}\ncorrect spec: {value}\nwrong spec: {wrongSpec}')
                    return False
            
            imgObj.close()

        Img.brandJsonFile.close()
        print('All Images Checked')
        return True
