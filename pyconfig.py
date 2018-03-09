import os
import sys


CONTENT = """[global]
index-url = http://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host = mirrors.aliyun.com
"""


def main():
    if sys.platform == 'win32':
        homepath = os.path.expandvars("%userprofile%" + "\\pip")
        filename = '\\pip.ini'
    else:
        homepath = '~/.pip'
        filename = '/pip.conf'

    if not os.path.exists(homepath):
        os.makedirs(homepath)
    with open(homepath + filename, 'w') as write_file:
        write_file.write(CONTENT)


if __name__ == '__main__':
    main()
