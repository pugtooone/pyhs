from importlib import resources
import json
import gspread

class ProductionPlan:

    with resources.open_text('Resources', 'service_account.json') as credJSON:
        #convert to dict type as gspread.auth.service_account accepts only filename path or dict
        credDict = json.load(credJSON)
    gc = gspread.service_account_from_dict(credDict)
    ppbook = gc.open('Copy of 2022 HK Production Planning')
    ppsheet = ppbook.worksheet('2022')

    def __init__(self, job_name):
        self.jobCell = ProductionPlan.ppsheet.find(job_name)

    def _find(self, keyword):
        colToFind = ProductionPlan.ppsheet.find(keyword)
        return ProductionPlan.ppsheet.cell(self.jobCell.row, colToFind.col)

    def get_vendor(self):
        return self._find('Vendor').value

    def get_job_status(self):
        return self._find('Job Status').value

    def check_download(self):
        if self._find('Job Downloaded').value == 'TRUE':
            return True
        return False

    def check_qc_duty(self):
        pass

    def update_job_status(self, stage):
        self.jobStatusCell = self._find('Job Status')
        ProductionPlan.ppsheet.update(self.jobStatusCell.address, stage)
