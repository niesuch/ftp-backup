import ftplib
import sys
import os
from lib.FTPUpload import FTPUpload

if __name__ == '__main__':
    try:
        ftp_upload = FTPUpload(os.path.abspath('config/config.json'))
        ftp_upload.upload()
    except FileNotFoundError as error:
        sys.exit(f'File `{error.filename}` does not exist.')
    except ftplib.all_errors as e:
        sys.exit(e)