# FTP Backup
<b>Author:</b> Niesuch <br />
<b>Programming language:</b> Python <br />

## Table of Contents:
1. [Description](https://github.com/niesuch/ftp-backup#description)
2. [How to use it](https://github.com/niesuch/ftp-backup#how-to-use-it)
2. [Install](https://github.com/niesuch/ftp-backup#how-to-install)
3. [Changelog](https://github.com/niesuch/ftp-backup#changelog)
4. [Copyright and License](https://github.com/niesuch/ftp-backup#copyright-and-license)

## Description:
![Screen](/docs/screens/screen1.jpg)

FTP Backup was created for data backup on the chosen FTP. Application gets a config file in which we can define e.g. a directory path, FTP connection data, etc. Firstly, application opens connection with FTP. Then it creates an archive for chosen directory and sends it to the server. In next step, application remove old backups from the FTP - we can define how many copies we want to store. Int the last step, it may remove the local archive version (or not, as defined in the config file).

## How to use it:
* Prepare the config file
* Open a console
* Use a command: `py main.py`
* Wait for the success :)

## How to install
* Download a repository
* Download Python in version 3.6+

## Changelog
Click on the following link to see the changelog: [CHANGELOG](https://github.com/niesuch/ftp-backup/releases)

## Copyright and License
Copyright 2019 Niesuch, Inc. Code released under the [MIT license](https://github.com/niesuch/ftp-backup/blob/master/LICENSE.md).

[Back to top](https://github.com/niesuch/ftp-backup/blob/master/README.md#ftp-backup)
