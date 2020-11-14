# encoding=utf8

from MysqlHelper import MysqlHelper
from hashlib import sha1

insert_sql = "insert into userinfos(name,pwd) values(%s,%s)"
select_sql = "select name from userinfos where name = %s"

while 1:
    name = input("请输入用户名：")
    mysql = MysqlHelper("localhost",3306,"datasource","tony","123456")
    check_name = mysql.get_one(select_sql, name)
    if check_name != None:
        print("用户名已存在,请重新输入")
        continue

    # 加密
    
    pwd = input("请输入密码:")
    s1 = sha1()
    s1.update(pwd.encode("utf-8"))
    pwdSha1 = s1.hexdigest()

    mysql = MysqlHelper("localhost",3306,"datasource","tony","123456")
    count = mysql.insert(insert_sql,(name,pwdSha1))
    if count == 1:
        print("恭喜，注册成功")
    else:
        print("失败")
    
    break


