import os
import json
from lib.Archive import Archive
from lib.FTPConnect import FTPConnect


class FTPUpload:
    """
    A class used to upload archive to FTP

    Attributes
    ----------
    config_file : str
        Path to config file
    config : int
        Config data
    session : str
        FTP session
    """
    def __init__(self, config_file):
        """
        Parameters
        ----------
        config_file : str
            Path to config file
        """
        self.__config_file = config_file
        self.__config = None
        self.__session = None

    def upload(self):
        """
        @public
        Service of sending archive

        1. Get data from config file
        2. Connect with FTP
        3. Send archive to FTP
        4. Remove old archives on FTP
        5. Delete or not local archive version
        """
        with open(self.__config_file) as config:
            self.__config = json.load(config)
            ftp_host = self.__config['ftp']['host']
            ftp_username = self.__config['ftp']['username']
            ftp_password = self.__config['ftp']['password']
            ftp_dir = self.__config['ftp']['dir']

            with FTPConnect(ftp_host, ftp_username, ftp_password) as session:
                self.__session = session
                self.__session.cwd(ftp_dir)

                for dir in self.__config['backup']['dirs']:
                    self.__upload_dir(dir)
                    self.__remove_old_backups(dir)
                    print(f'UPLOADED: "{dir}"')

    def __remove_old_backups(self, dir):
        """
        @private
        Remove old backups on FTP

        Parameters
        ----------
        dir : str
            Input directory
        """
        files = [x for x in self.__session.nlst() if x.startswith(dir)]
        diff = len(files) - self.__config['backup']['number']

        if 0 < diff:
            for file in files[:diff]:
                self.__session.delete(file)

    def __upload_dir(self, dir):
        """
        @private
        Create archive for directory and send to FTP

        Parameters
        ----------
        dir : str
            Input directory
        """
        local = self.__config['backup']['local']
        local_dir = self.__config['backup']['local_dir']

        with Archive(dir=dir, local=local, local_dir=local_dir) as archive:
            with open(archive, 'rb') as file:
                filename = os.path.basename(file.name)
                self.__session.storbinary(f'STOR {filename}', file)
