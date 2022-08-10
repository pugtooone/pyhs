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

    def fill_qc_tab(self):
        pass
        # self.qcTab.update(len, imgNamelist)
