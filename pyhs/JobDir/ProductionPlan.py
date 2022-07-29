import gspread

class ProductionPlan:
    gc = gspread.service_account(filename='Resources/Credentials/service_account.json')
    def __init__(self):
        self.workbook = ProductionPlan.gc.open('2022 HK Production Planning')
        self.prodPlan = self.workbook.worksheet('2022')
