#!/usr/bin/python2
#coding:utf8
import httplib

def check_webserver(address,port,resource):
    if not resource.startswith('/'):
        resource='/'+resource
    try:
        conn=httplib.HTTPConnection(address,port)
        print "######### connected successfull!! ######"
        req=conn.request('GET',resource)
        print "###### request ok!#####"
        res=conn.getresponse()
        print "response ok! status:%s" %res.status
    except Exception,e:
        print "HTTP connection failed:%s" %e
        return False
    finally:
        conn.close()
        print "connection close successfull!"
    if res.status in [200,301]:
        return True
    else:
        return False
if __name__=="__main__":
    from optparse import OptionParser
    --a
    --r
    --p
    check_webserver()
