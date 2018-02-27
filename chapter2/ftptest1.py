# -*- coding:utf-8 -*-
import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', '123@your.com')
        print '\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded.'
        ftp.quit()
        return True
    except Exception, e:
        print '\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed.'
        return False


hostname = '172.25.51.10'
anonLogin(hostname)