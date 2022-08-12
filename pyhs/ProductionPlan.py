from importlib import resources
import json
import gspread

class ProductionPlan:

    @staticmethod
    def open_prod_plan():
        with resources.open_text('Resources', 'service_account.json') as credJSON:
            #convert to dict type as gspread.auth.service_account accepts only filename path or dict
            credDict = json.load(credJSON)
        gc = gspread.service_account_from_dict(credDict)
        ppbook = gc.open('2022 HK Production Planning')
        ppsheet = ppbook.worksheet('2022')
        return ppsheet

    @staticmethod
    def get_qc_duty(qc_id):
        """
        static method that does not need instantiation, for checking qc duty
        """
        ppsheet = ProductionPlan.open_prod_plan()
        imgDeadlineCol = ppsheet.find('Image Delivery Deadline')
        ppsheet.sort((imgDeadlineCol.col, 'asc'))
        qcDutyRow = ppsheet.findall(qc_id.title())
        qcDutyList = []
        for row in qcDutyRow:
            qcDutyJob = ppsheet.cell(row.row, 3).value
            qcDutyList.append(qcDutyJob)
        return qcDutyList

    def __init__(self, job_name):
        ProductionPlan.ppsheet = ProductionPlan.open_prod_plan()
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

    def fill_prod_plan(self, prodCount, imgCatDict):

        #fill product count
        prodNumCell = self._find('Total No. Product')
        ProductionPlan.ppsheet.update(prodNumCell.address, prodCount)

        #fill img count
        for key, value in imgCatDict.items():
            keyCell = self._find(key)
            if value > 0:
                ProductionPlan.ppsheet.update(keyCell.address, value)

    def update_job_status(self, stage):
        self.jobStatusCell = self._find('Job Status')
        ProductionPlan.ppsheet.update(self.jobStatusCell.address, stage)
