from ftplib import FTP
from pathlib import Path
from importlib import resources
import json

class FileTransmitter:

    TBQ = Path.home() / 'Desktop' / 'IHS' / 'To Be QC'

    def __init__(self, vendor):
        self.vendor = vendor

    def download_job(self, job):
        ftp = self._connect_ftp('download')
        jobPath = FileTransmitter.TBQ / job

        #not working as retrbinary only works on file not dir
        # with open(jobPath, 'wb') as file:
            # ftp.retrbinary('RETR {}'.format(job), file.write)
        ftp.quit()

    def _connect_ftp(self, stage):
        """
        connect to the vendor's ftp, and set the cwd according to the stage
        """
        vendor = self.vendor

        #retrieving data from vendor json
        with resources.open_text('Resources', 'Vendor.json') as vendorJSON:
            vendorData = json.load(vendorJSON)
            host = vendorData[vendor]['Host']
            username = vendorData[vendor]['Username']
            password = vendorData[vendor]['Password']
            if stage == 'download':
                dir = vendorData[vendor]['DownloadDir']
            elif stage == 'upload':
                dir = vendorData[vendor]['UploadDir']
            else:
                raise Exception('Wrong Stage')

        ftp = FTP(host)
        ftp.login(user=username, passwd=password)
        ftp.cwd(dir)
        return ftp
