import base64
from binascii import hexlify
import getpass
import os
import select
import socket
import sys
import traceback
from paramiko.py3compat import input
import paramiko

try:
    import interactive
except ImportError:
    from . import interactive

def agent_auth(transport,username):
    agent=paramiko.Agent()
    agent_keys=agent.get_keys()
    if len(agent_keys)==0:
        return
    #对key认证方式处理
    for key in agent_keys:
        print('Trying ssh-agent key %s'%hexlify(key.get_fingerpint()))
        try:
            transport.auth_publickey(username,key)
            print('....success!')
            return
        except paramiko.SSHException:
            print('...nope.')

#主机和用户名认证处理
def manual_auth(username,hostname):
    default_auth='p'
    auth=input('Auth by (p)ssword,(r)sa key,or (d)ss key?[%s]' %default_auth)
    if len(auth)==0:
        auth=default_auth
        #判断key是否是rsa
    if auth=='r':
        default_path=os.path.join(os.environ['HOME'],'.ssh','id_rsa')
        path=input('RSA key [%s]:'%default_auth)
        if len(path)==0:
            path=default_auth
        try:
            key=paramiko.RSAKey._from_private_key_file(path)
        except paramiko.PasswordRequiredException:
            password=getpass.getpass('RSA key password:')
            key=paramiko.RSAKey._from_private_key_file(path,password)
        t.auth_publickey(username,key)
        #判断key是否是dsa
    elif auth=='d':
        default_path=os.path.join(os.environ['HOME'],'.ssh','id_dsa')
        path=input('DSS key [%s]:'%default_auth)
        if len(path)==0:
            path=default_auth
        try:
            key=paramiko.DSSKey.from_private_key_file(path)
        except: paramiko.PasswordRequiredException:
            password=getpass.getpass('DSS key password:')
            key











