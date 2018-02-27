# -*- coding:utf-8 -*-
import mechanize
def testUserTest(url, proxy):
    browser = mechanize.Browser()
    browser.addheaders=userAgent
    page = browser.open(url)
    source_code = page.read()
    print source_code

url = 'http://www.whatismyuseragent.dotdoh.com/'
# 网址已失效
userAgent=['User-agent','Mozilla/5.0(X11;U;+Linux 2.4.2-2 i586;en-US;m18)Geo/20010131 Netscap6/6.01']
testUserTest(url, userAgent)