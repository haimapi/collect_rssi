import numpy as np


def gettable(filename):

    '''this function extract inforomation from a file and 
       outputs a dict'''

    fp = open(filename)

    channel = []
    essid = []
    mac = []
    rssi = []

    table = {}

    for k in fp:
        if 'Channel:' in k:
            channel.append(k.strip())
        if 'ESSID:' in k:
            essid.append(k.strip()[7:].replace('"', ''))
        if 'Address' in k:
            mac.append(k.strip()[19:40])
        if 'Signal' in k:
            rssi.append(float(k.strip()[28:31]))
    
    fp.close()

    for k in range(len(essid)):
        
        if essid[k] in ['CSI', 'TP-LINK_2.4GHz_CSI', 'xq']:
            if essid[k] in table.keys():
                table[essid[k]].append(rssi[k])
            else:
                table[essid[k]] = [rssi[k]]
 
    return table

def getmean(mydict):

    m = []
    for k in [0, 1, 2]:
        m.append(np.mean(mydict[mydict.keys()[k]]))

    return m


    

def getstd(mydict):

    s = []

    for k in [0, 1, 2]:
        s.append(np.var(mydict[mydict.keys()[k]]))

    return s
