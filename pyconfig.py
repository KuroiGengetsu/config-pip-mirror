import os
import sys


CONTENT = """[global]
index-url = http://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host = mirrors.aliyun.com
"""


def main():
    if sys.platform == "win32":                                   # if on windows
        homepath = os.path.expandvars("%userprofile%")            # The userhome's path
        if not os.path.exists(homepath + "\\pip"):                # check whether the folder named pip existed
            os.makedirs(homepath + "\\pip")                       # if not, create it
        with open(homepath + "\\pip\\pip.ini", "w") as fp:        # create the pip.ini file
            fp.write(CONTENT)                                     # write CONTENT
    elif sys.platform == 'linux':                                 # if on linux
        if not os.path.exists('~/pip'):                           # check whether the folder named .pip existed
            os.makedirs("~/.pip")                                 # if not, create it
        with open("~/.pip/pip.conf", "w") as fp:                  # create the pip.conf file
            fp.write(CONTENT)                                     # write CONTENT


if __name__ == '__main__':
    main()
