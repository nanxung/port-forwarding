#coding:utf-8
import requests
import re
import threading
# url='http://zhihudaily.ahorn.me/'
# html=requests.get(url)
# titles1=re.findall("<a href=(.*?)>",html.text,re.S)
#titles2=re.findall("<span class='title'>(.*?)</span>",html.text,re.S)
'''for i in range(len(titles2)):
    print titles2[i]+":"+titles1[i+1]'''
#print html.text


class myThread(threading.Thread):
    def __init__(self,threadID):
        threading.Thread.__init__(self)
        self.threadID=threadID
    def run(self):
        url = 'http://zhihudaily.ahorn.me/'
        html = requests.get(url)
        titles1 = re.findall("<a href=(.*?)>", html.text, re.S)
        print titles1[2]
        html = requests.get(titles1[2])
        text = re.findall("<p>(.*)</p>", html.text, re.S)
        print text

thread1=myThread(1)
thread1.start()

# def getpage():
#     #for n in titles1:
#       #  print n
#     html=requests.get(titles1[2]+"/")
#     text=re.findall("<p>(.*)</p>",html.text,re.S)
#     print text

# try:
#     thread.start_new_thread(getpage(),("thread-1",4,))
# except:
#     print "Error:unable to start thread"