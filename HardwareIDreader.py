#!/usr/bin/python3.6
from easysnmp import Session
import re
import pprint

class HardwareIDreader(object):
    def __init__(self):
        self.siteMap={}

    def readInput(self,inputfile):
        with open(inputfile) as ifile:
            itemList=[]
            site=""
            self.siteMap={}
            for line in ifile:
#               print(line)
                r1 = re.search(r'Evertz',line)
                if r1 != None:
                    deviceName=line.split("><")[2].split(">")[1].split("<")[0]
                    #print(deviceName)
                    deviceIP=line.split("><")[5].split(">")[1].split("<")[0]
                    #print(deviceIP)
                    tmpList=[deviceName,deviceIP]
                    itemList.append(tmpList)
                r2 = re.search(r'<Type dt:dt="ui4">1<\/Type>',line)
                if r2 != None:
                    siteName=line.split("><")[2].split(">")[1].split("<")[0]
                    if(len(itemList)>0):
                        self.siteMap[siteName]=itemList
                        itemList=[]
            addition = ['TD1-TD6-Rx-Evertz DVB-S2','http://10.49.3.48']
            self.siteMap['6153 Radio Hill']=[addition]

    def printMap(self):
        pprint.pprint(self.siteMap)

    def getSNSW(self):
        print("Site,TX Name,IP Address,Software Build Version")
        for site, devices in self.siteMap.items():
            for device in devices:
                #print(site+","+device[0]+","+device[1])
                #get the snmp values
                IP=(device[1])[7:]
                #print(IP)
                try:
                    session = Session(hostname=IP, community='BANMSRO', version=2)
                    SN = session.get('.1.3.6.1.4.1.6827.10.216.5.3.0')
                    print(site+","+device[0]+","+device[1]+","+SN.value)
                except Exception as e:
                    try:
                        session2 = Session(hostname=IP, community='public', version=2)
                        SN2 = session2.get('.1.3.6.1.4.1.6827.10.216.5.3.0')
                        print(site+","+device[0]+","+device[1]+","+SN2.value)
                    except Exception as e:
                        print(site+","+device[0]+","+device[1]+","+str(e))

if __name__ == "__main__":
    myreader=HardwareIDreader()
    myreader.readInput("Evertz.txt")
#myreader.printMap()
    myreader.getSNSW()
