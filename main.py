# imports
import wget
import os
import numpy
import time
import datetime

tme = datetime.datetime
# initialising vars
i = 0
windsp = [[0 for x1 in range(3)] for x2 in range(40)]
workingDir = os.listdir(os.curdir)
# cache data
url = '/home/samuel/Desktop/index.html?s=416'
# realurl = 'http://micro.windguru.cz/?s=274620&m=21'
daysinthismonth = int()

# pulling data

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
temp = wget.download(url)
os.rename("index.html", "download.wget")

# file into variable
os.rename("download.wget", "temp")
with open('temp') as f:
    temp = f.readlines()
temp = temp[23:51]
temp = numpy.transpose(temp)
temp = [i.split(' ')[0:-1] for i in temp]
list1 = temp[0][2]

# making easy to work with list
j = 0
# for i in temp:
#     temp[j][0] = i.strip(".")
#     j+=1
#     print(temp)
for i in range(0, 20, 1):
    windsp[i][0] = temp[i][2]
    windsp[i][1] = temp[i][3]
    windsp[i][2] = temp[i][9]

if time.strftime(":%m") == 4 or 6 or 9 or 11:
    daysinthismonth = 30
elif time.strftime(":%m") == 2:
    daysinthismonth = 28
elif time.strftime(":%m") == 2 and time.strftime(":%y") % 4 == 0:
    daysinthismonth = 29
else:
    daysinthismonth = 31
count1 = int(0)
countfinal = 10
#
# if 28. in windsp[0:]:
#     print('first in the month')
# else:
#     print('help')
print [windsp]
