import MySQLdb

class MySQLCtrl(object)
        def __init__(self,host="localhost",user="root",passwd="chenbo01"):
            self.conn1=MySQLdb.Connect(host=host,user=user,passwd=passwd)
            self.conn1.select_db('test')
            self.cur=conn1.cursor()
        def i(self,name,age):
            sqli="insert into staff values(%s,%s)"
            cur.execute(sqli,('ch',23))
sqls="select * from staff"
cur.executemany(sqli,(('cb',23),('cg',21)))
cur.execute(sqls)
count=cur.execute("select * from staff;")
data_one=cur.fetchone()
data_many=cur.fetchmany()
data_all=cur.fetchone()

cur.close()
conn1.close()
