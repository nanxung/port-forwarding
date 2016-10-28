import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    if not s.connect(('119.29.238.116',22)):
        print 'True'
    else:
        print 'False'
except socket.error,e:
    print 'error:%s' %e