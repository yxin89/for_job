# encodin=utf8

from MysqlHelper import MysqlHelper

sql = "insert into student(name,age) values(%s,%s)"
name = input("name:")
age = input("age:")
params = [name, age]

mysqlhelper = MysqlHelper(host='localhost',port=3306,db='datasource',user='tony', passwd='123456',charset = 'utf8')
count = mysqlhelper.insert(sql, params)

if count == 1:
    print('OK')
else:
    print('error')