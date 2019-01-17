from ftplib import FTP


class FTPConnect:
    """
    A class used to init connection with FTP

    Attributes
    ----------
    host : str
        FTP host
    username : str
        FTP username
    password : str
        FTP user password
    ftp : obj
        FTP object
    """

    def __init__(self, host, username, password):
        """
        Parameters
        ----------
        host : str
            FTP host
        username : str
            FTP username
        password : str
            FTP user password
        """
        self.__host = host
        self.__username = username
        self.__password = password

    def __enter__(self):
        """
        Connect with FTP after init
        """
        self.__ftp = FTP(self.__host)
        self.__ftp.login(self.__username, self.__password)
        return self.__ftp

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close connection with FTP
        """
        self.__ftp.close()
