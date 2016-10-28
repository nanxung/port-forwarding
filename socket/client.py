import socket
host='localhost'
port=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
w=open('s.txt','r')
s.send('s.txt')
l=w.readlines(5)
'''while not l:
    l+=w.readline()'''
for i in l:
    s.send(i)
s.close()
w.close()
