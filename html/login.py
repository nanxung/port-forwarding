##解决中文报错
#coding:utf-8
import sys
import re
import urllib2
import urllib
import requests
import cookielib


class Login(object):
    def __init__(self):
        self.name=''
        self.passwprd=''
        self.domin=''
        self.cj=cookielib.LWPCookieJar()
        self.opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
