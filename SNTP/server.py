#coding:utf8
import sys
import socket
import argparse
host='localhost'
data_payload=2048
backlog=5

def echo_server(port):
    ''' A simple echo server
    #create a tcp server '''
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # Enable reuse address/port
    server_address=(host,port)
    print "starting up echo server on %s port %s" %server_address
    sock.bind(server_address)
    #Listen to clients,backlog argument specifies the max no. of queued connections
    sock.listen(backlog)
    while True:
        print "Waiting to receive message from client"
        client,address=sock.accept()
        data=client.recv(data_payload)
        if data:
            print "Data:%s" %data
            client.send(data)
            print "sent %s bates back to %s"%(data,address)
        client.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Socket server Example')
    parser.add_argument('--port',action="store",dest="port",type=int,required=True)
    given_args=parser.parse_args()
    port= given_args.port
    echo_server(port)