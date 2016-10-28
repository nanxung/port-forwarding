#!/usr/bin/python2
#coding:utf8
import poplib

username="15727705387@163.com"
password="chenbo01"

mail_server="mail.163.com"

p=poplib.POP3(mail_server)
p.user(username)
p.pass_(password)

for msg_id in p.list():
    outf=open('%s.eml' % msg_id,'w')
    outf.write('\n'.join(p.retr(msg_id)[1]))
    outf.close()
p.quit()