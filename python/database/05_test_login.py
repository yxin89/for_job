# encoding=utf8
from MysqlHelper import MysqlHelper
from hashlib import sha1

# 如果使用md5加密，则密码包含32个字符
# 如果使用sha1加密，则密码包含40个字符，推荐使用这种方式

# 插入如下数据，用户名为123,密码为123,这是sha1加密后的值
# insert into userinfos values(0,'123','40bd001563085fc35165329ea1ff5c5ecbdbbeef',0);

name = input("输入名字：")
pwd = input("输入密码：")

s1 = sha1()
s1.update(pwd.encode("utf-8"))
spwdSha1 = s1.hexdigest()

sql = "select pwd from userinfos where name = %s"
params = [name]

myconn = MysqlHelper("localhost",3306,"datasource","tony","123456")
res = myconn.get_one(sql, params)

if res == None:
    print("用户名错误")
elif res[0] == spwdSha1:
    print("登陆成功")
else:
    print("密码错误")



