import os
import sys
import tarfile
import time


class Archive:
    """
    A class used to create and delete tar archive for chosen directory

    Attributes
    ----------
    dir : str
        Input directory
    local : int
        Save local backup (0-no, 1-yes)
    local_dir : str
        Local backup directory
    output: str
        Output data
    """
    def __init__(self, dir, **kwargs):
        """
        Parameters
        ----------
        dir : str
            Input directory
        local : int
            Save local backup (0-no, 1-yes)
        local_dir : str
            Local backup directory
        """
        self.__dir = dir
        self.__local = kwargs.get('local', 0)
        self.__local_dir = os.path.abspath(kwargs.get('local_dir', ''))
        self.__output = None

    def __enter__(self):
        """
        Create tar archive after init
        """
        return self.__create()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        If something wrong or _local = 0 delete archive
        """
        if exc_type is not None or not self.__local:
            self.__delete()
        else:
            print(f'LOCAL BACKUP: "{self.__dir}"')

    def __create(self):
        """
        @private
        Create tar archive for chosen directory and save that name in output
        """
        time_name = time.strftime('_%Y_%m_%d_%H%M%S')
        dir_name = os.path.basename(self.__dir)

        with tarfile.open(f'{self.__local_dir}\\{dir_name}{time_name}.tar.gz', "w:gz") as tar:
            tar.add(self.__dir, arcname=dir_name)
            self.__output = tar.name

        return self.__output

    def __delete(self):
        """
        @private
        Delete archive from output
        """
        os.remove(self.__output)
