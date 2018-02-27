# -*- coding:utf-8 -*-
from _winreg import *

def va12addr(val):
    addr=""
    for ch in val:
        addr += ("%02x " %ord(ch))
    addr = addr.strip(' ').replace(" ",":")[0:17]
    return addr

def printNets():
    net ="SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
    key = OpenKey(HKEY_LOCAL_MACHINE,net, 0)
    print '\n[+] Networks You have Joined.'
    for i in range(100):
       try:
            guid = EnumKey(key,i)
            netKey = OpenKey(key,str(guid))
            (n,name,t) = EnumValue(netKey,1)
            (n,addr,t) = EnumValue(netKey,5)
            macAddr = va12addr(addr)
            netName = str(name)
            print '[+] '+netName +' '+macAddr
            CloseKey(netKey)
       except Exception ,e:
            print e
            pass

def main():
    printNets()
if __name__=='__main__':
    main()