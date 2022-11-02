from importlib import resources
import gspread
import json

class JobStatusReport:
    with resources.open_text('Resources', 'service_account.json') as credJSON:
        #convert to dict type as gspread.auth.service_account accepts only filename path or dict
        credDict = json.load(credJSON)
    gc = gspread.service_account_from_dict(credDict)

    def __init__(self, vendor):
        try:
            with resources.open_text('Resources', 'JobStatusReport.json') as jsrJSON:
                self.vendorJsrJSON = json.load(jsrJSON)[vendor]
                self.vendorJSR = JobStatusReport.gc.open(self.vendorJsrJSON)
        except KeyError:
            print(f'No Job Status Report for {vendor}')
            self.vendorJSR = None
            return self.vendorJSR

