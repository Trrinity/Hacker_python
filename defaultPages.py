import ftplib
def returnDefault(ftp):
    try:
        dirList=ftp.nlst()
    except:
        dirList=[]
        print '[-] Could not list directory contents.'
        print '[-] Slipping To Next Target'
        return
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.jsp' in fn or '.htm' in fn:
            print'[+] Found default page:'+fileName
            retList.append(fileName)
        print 'nono'
        return retList
if __name__ == '__main__':
    host='127.0.0.1'
    userName='Shannon'
    password='lyt520'
    ftp=ftplib.FTP(host)
    ftp.login(userName,password)
    returnDefault(ftp)