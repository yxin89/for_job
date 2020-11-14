# encoding=utf8

# MySQL数据库操作

import pymysql

# pymysql.connect(host, port, db, user, password, charset)
# charset: 通信采用的编码方式，默认是'gb2312'，要求与数据库创建时指定的编码一致，否则中文会乱码

try:
    conn = pymysql.connect(host='localhost',port=3306,db='datasource',user='tony', password='123456',charset = 'utf8')
    cursor = conn.cursor()
    count = cursor
    
    # 增加
    print('普通插入数据------------------------')
    sql = "insert into student(name,age,grade) values('Tom',16,13)"
    count = cursor.execute(sql)
    print('影响行数：', count)
    conn.commit()
    # 参数化插入
    name=input("输入名字:")
    age=int(input("输入年龄:"))
    sql = "insert into student(name,age) values(%s,%s)"
    params = [name,age]
    count = cursor.execute(sql, params)
    conn.commit()

    # 查询
    print('查询------------------------')
    cursor.execute("select * from student")
    res = cursor.fetchall()
    for line in res:
        print(line)

    # 删除
    print('查询------------------------')
    sql = "delete from student where name = 'Tom'"
    cursor.execute(sql)
    conn.commit()
    cursor.execute("select * from student")
    res = cursor.fetchall()
    for line in res:
        print(line)
    
    
except Exception as e:
    print(e)
finally:
    # 退出游标和链接
    cursor.close()
    conn.close()