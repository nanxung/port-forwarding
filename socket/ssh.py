import paramiko
par=paramiko.SSHClient()
par.set_missing_host_key_policy(paramiko.AutoAddPolicy())
par.connect('119.29.238.116',22,"root","chenbo01")
par.exec_command(r'cd ..')
par.exec_command(r'cd ..')
par.exec_command(r'cd ..')
par.exec_command(r'cd ..')
ins1,out1,error1=par.exec_command(r"cd /")
ins2,out2,error2=par.exec_command('cd / && ls -l')
'''ins,out,error= par.exec_command('ls')'''
s=out1.read()
s1=out2.read()
print s,s1
