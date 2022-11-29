from importlib import resources
from pathlib import Path
import json
import gspread
import os
import sys

class ServerQuery:
    #class attribute
    #brand folders
    try:
        brandDir = Path('/Volumes/Studio/CLIENTS/Ralph Lauren/Production/')
    except FileNotFoundError:
        print('Server is not connected')
        sys.exit(1)
    sessionBase = os.listdir(brandDir)

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
    def get_prodlist():
        """
        static method that does not need instantiation, for checking qc duty
        """
        wksheet = ServerQuery.open_gsheet_center()
        prodCol = wksheet.find('Product').col
        prodList = wksheet.col_values(prodCol)
        return prodList

    def __init__(self):
        ServerQuery.wksheet = ServerQuery.open_gsheet_center()
        self.prodList = ServerQuery.get_prodlist()

    def update_shot_status(self):
        for prod in self.prodList:
            ServerQuery.brandDir.glob(f'**/{prod}*.CR2')

    def update_job_status(self, stage):
        self.jobStatusCell = self._find('Job Status')
        ProductionPlan.ppsheet.update(self.jobStatusCell.address, stage)
