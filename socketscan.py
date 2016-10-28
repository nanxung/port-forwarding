#!/usr/bin/python2
import socket

def checkPort(address,port):
    s=socket.socket()
    try:
        s.connect((address,port))
        print "connected !!!!"
        return True
    except socket.error,e:
        print "error is %s" %e
        return False

if __name__=="__main__":
    from optparse import OptionParser
    parser=OptionParser()
    parser.add_option("-a","--address",dest='address',default='localhost',help="ADDRESS")
    parser.add_option("-p","--port",dest='port',type="int",default=22,help="PORTS")
    (options,args)=parser.parse_args()
    checkPort(options.address,options.port)

