#!/usr/bin/python2
#coding:utf-8
import socket
def print_machine_info():
    host_name="www.sddsaffdgdfg.org"
    try:
        ip_address=socket.gethostbyname(host_name)
        print "Host name:%s" %ip_address
    except socket.error, err_msg:
        print "%s:%s" %(host_name,err_msg)

if __name__=="__main__":
    print_machine_info()
