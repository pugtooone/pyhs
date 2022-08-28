from ftplib import FTP
from pathlib import Path
from importlib import resources
import json

class FileTransmitter:

    TBQ = Path.home() / 'Desktop' / 'To Be QC'

    def __init__(self, vendor):
        self.vendor = vendor

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
        print("{}'s FTP connected".format(vendor))
        ftp.login(user=username, passwd=password)
        print('Login Success\n')
        ftp.cwd(dir)
        return ftp

    def download_ftp_job(self, job):

        def ftp_loop(fileList, jobPath):
            """
            nested loop function within download_job() to work with folder tree
            """
            print('ftp_loop running...\n')
            for file, data in fileList:
                fileType = data['type']

                if fileType == 'dir':
                    print('{} is a directory'.format(file))
                    jobPath = jobPath / file
                    jobPath.mkdir(exist_ok=True)
                    ftp.cwd(file)
                    print('cd to {}'.format(file))
                    fileList = ftp.mlsd()
                    ftp_loop(fileList, jobPath) #re-run this function with the subfolders

                elif fileType == 'file':
                    filePath = jobPath / file
                    with open(filePath, 'wb') as f:
                        print('{} is being downloaded'.format(file))
                        ftp.retrbinary('RETR {}'.format(file), f.write)
                        print('{} is downloaded'.format(file))

        ftp = self._connect_ftp('download')
        ftp.cwd(job)

        fileList = ftp.mlsd() #return tuple (filename, data dict)

        jobPath = FileTransmitter.TBQ / job
        jobPath.mkdir(exist_ok=True)

        ftp_loop(fileList, jobPath)
        ftp.quit()

    def upload_ftp_job(self, job):
        pass
