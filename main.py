import wget
import os
import numpy
workingDir = os.listdir(os.curdir)
url = 'http://micro.windguru.cz/?s=274620&m=21'
x = ([2,2,2], [2,2,2])

if "download.wget" in workingDir:
    print('already exists')
    os.remove('download.wget')
    if 'download.get' in workingDir:
        print('delete failed')
    else:
        print('delete successful')
if "temp" in workingDir:
    print('already exists')
    os.remove('temp')
    if "temp" in workingDir:
        print('delete failed')
    else:
        print('delete successful')
    print('downloading')
wget.download(url)
os.rename("download.wget", "temp")
with open('temp') as f:
    temp = f.readlines()
temp = temp[23:51]
print(temp)
