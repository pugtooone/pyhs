from importlib import resources
import json
import gspread

class ShotList:

    with resources.open_text('Resources', 'service_account.json') as credJSON:
        #convert to dict type as gspread.auth.service_account accepts only filename path or dict
        credDict = json.load(credJSON)
    gc = gspread.service_account_from_dict(credDict)

    def __init__(self, brand):
        with resources.open_text('Resources', 'BrandShotList.json') as ShotListJSON:
            self.shotListName = json.load(ShotListJSON)[brand]
            self.brandShotList = ShotList.gc.open(self.shotListName)
            self.qcTab = self.brandShotList.worksheet('For QC')

    def fill_qc_tab(self, imgNum, imgNameList):
        self.qcTab.batch_clear(['A2:A'])
        self.qcTabRange = 'A2:A' + imgNum

        #convert list (row: [a,b]) into list of lists (column: [[a],[b]]) 
        self.qcTabInput = []
        for img in imgNameList:
            self.qcTabInput.append([img])
        self.qcTabDict = {'range': self.qcTabRange, 'values': self.qcTabInput}
        #batch_update() accepts a list of dicts
        self.qcTab.batch_update([self.qcTabDict])

    def fill_shotlist(self):
        pass
