from importlib import resources
from pathlib import Path
import json
import gspread
import sys

class ServerQuery:
    #class attribute
    #brand folders
    try:
        brandDir = Path('/Volumes/Studio/CLIENTS/Ralph Lauren/Production/')
    except FileNotFoundError:
        print('Server is not connected')
        sys.exit(1)

    @staticmethod
    def open_gsheet_center():
        with resources.open_text('Resources', 'service_account.json') as credJSON:
            #convert to dict type as gspread.auth.service_account accepts only filename path or dict
            credDict = json.load(credJSON)
        gc = gspread.service_account_from_dict(credDict)
        wkbook = gc.open('RL Server Draft')
        wksheet = wkbook.worksheet('RL')
        return wksheet

    @staticmethod
    def get_prodList(wksheet):
        """
        static method that does not need instantiation, for checking qc duty
        """
        prodCol = wksheet.find('Product').col
        prodList = wksheet.col_values(prodCol)
        return prodList

    def __init__(self):
        self.wksheet = ServerQuery.open_gsheet_center()
        self.prodList = ServerQuery.get_prodList(self.wksheet)

    def update_shot_status(self):
        for prod in self.prodList:
            product = ServerQuery.brandDir.glob(f'**/{prod}')
            #if product != '':

    def update_job_status(self, stage):
        self.jobStatusCell = self._find('Job Status')
        ProductionPlan.ppsheet.update(self.jobStatusCell.address, stage)
