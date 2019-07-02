#!/usr/bin/python3.6
from easysnmp import Session

session = Session(hostname='10.49.3.48', community='public', version=2)
SN = session.get('.1.3.6.1.4.1.6827.10.216.5.3.0')
#SW = session.get('.1.3.6.1.4.1.6827.10.216.5.2')
print(SN.value)
#print(SW.value)

#session2 = Session(hostname='10.49.3.48', community='BANMSRO', version=2)
#SN2 = session2.get('.1.3.6.1.4.1.6827.10.216.5.3')
#SW2 = session2.get('.1.3.6.1.4.1.6827.10.216.5.5')
#print(SN2.value)
#print(SW2.value)

#session3 = Session(hostname='10.49.3.48', community='BANMSRO', version=2)
#SN3 = session3.get('.1.3.6.1.2.1.47.1.1.1.1.11.1')
#SW3 = session3.get('.1.3.6.1.2.1.47.1.1.1.1.9.1')
#print(SN3.value)
#print(SW3.value)
