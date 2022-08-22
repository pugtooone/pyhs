from ftplib import FTP
from importlib import resources
import json

class Uploader:
    def __init__(self, vendor):
        self.vendor = vendor

    def _connect_ftp(self):
        vendor = self.vendor
        with resources.open_text('Resources', 'Vendor.json') as vendorJSON:
            vendorData = json.load(vendorJSON)
            host = vendorData[vendor]['Host']
            username = vendorData[vendor]['Username']
            password = vendorData[vendor]['Password']
        with FTP(host) as ftp:
            ftp.login(user=username, passwd=password)
            ftp.cwd('Completed')
