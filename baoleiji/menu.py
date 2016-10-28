#!/usr/bin/python2
#coding:utf8
import os
import sys
msg='''\033[42;1mWelcome using eddy's auditing system!\033[0m'''
print msg

host_dict={
    'eddy1':'192.168.1.2',
    'eddy2':'192.168.1.3'
}

while True:
    for hostname,ip in host_dict.items():
        print hostname,ip
    try:
        host=raw_input('Please choose one server to login:').strip()
        if host=='quit':
            print 'Goodbye'
            break
    except KeyboardInterrupt:
        continue
    except EOFError:
        continue
    if len(host)==0:
        continue
    if not host_dict.has_key(host):
        print 'No host matched,try again'
        continue
    print '\033[32;1mGoing to connect \033[0m',host_dict[host]
    os.system("python eddy_auditing.py %s" %host_dict[host])
