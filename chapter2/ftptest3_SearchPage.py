# -*- coding:utf-8 -*-
import ftplib

def returnDefault(ftp):
    try:
        # nlst()方法获取目录下的文件
        dirList = ftp.nlst()
    except:
        dirList = []
        print '[-] Could not list directory contents.'
        print '[-] Skipping To Next Target.'
        return

    retList = []
    for filename in dirList:
        # lower()方法将文件名都转换为小写的形式
        fn = filename.lower()
        if '.php' in fn or '.asp' in fn or '.htm' in fn:
            print '[+] Found default page: ' + filename
            retList.append(filename)
    return retList


host ='127.0.0.1'
# host ='119.28.140.248'
# host = '111.230.43.239'
username = 'root'
password = '123'
ftp = ftplib.FTP(host)
ftp.login(username, password)
returnDefault(ftp)
#
# import ftplib
# ftp = ftplib.FTP()
# ftp.connect('127.0.0.1',2121)
# ftp.login('root','123')
# print ftp.getwelcome()
# list = ftp.nlst()
# print list
