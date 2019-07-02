#!/usr/bin/python3.6
import re
import pprint

with open("Evertz.txt") as ifile:
    itemList=[]
    site=""
    siteMap={}
    for line in ifile:
#        print(line)
        r1 = re.search(r'Evertz',line)
        if r1 != None:
            deviceName=line.split("><")[2].split(">")[1].split("<")[0]
            print(deviceName)
            deviceIP=line.split("><")[5].split(">")[1].split("<")[0]
            print(deviceIP)
            tmpList=[deviceName,deviceIP]
            itemList.append(tmpList)
        r2 = re.search(r'<Type dt:dt="ui4">1<\/Type>',line)
        if r2 != None:
            siteName=line.split("><")[2].split(">")[1].split("<")[0]
            if(len(itemList)>0):
                siteMap[siteName]=itemList
                itemList=[]
    addition = ['TD1-TD6-Rx-Evertz DVB-S2','http://10.49.3.48']
    siteMap['6153 Radio Hill']=[addition]
pprint.pprint(siteMap)

        


