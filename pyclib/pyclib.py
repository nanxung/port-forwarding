#coding:utf8
import socket
SEND_BUF_SIZE=4096
RECV_BUF_SIZE=4096
def test_socket_timeout():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print "Default socket timeout:%s" %s.gettimeout()
    s.settimeout(100)
    print "Current socket timeout:%s" %s.gettimeout()

def modify_buff_size():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    bufsize=sock.getsockopt(socket)


if __name__=="__main__":
    test_socket_timeout()