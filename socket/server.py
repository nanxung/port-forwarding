import socket
host=''
port =50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn,addr=s.accept()
print 'Connected by',addr
r=conn.recv(5)
r1=open('r%s' %r,'w')
while 1:
    data=conn.recv(1024)
    if not data:
        break
    r1.write(data)
r1.close()
conn.close()
s.close()