import gspread

class ProductionPlan:

    gc = gspread.service_account(filename='Resources/Credentials/service_account.json')
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

    def update_job_status(self):
        pass
