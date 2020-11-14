# encodin=utf8

from MysqlHelper import MysqlHelper

sql = "select name,age from student order by name desc"

mysqlhelper = MysqlHelper('localhost',3306,'datasource','tony', '123456')
res = mysqlhelper.get_one(sql)

print(res)