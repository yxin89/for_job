import os

result = os.getcwd()
print(result)

# chdir()改变当前工作目录
os.chdir('d:\\')
print(os.getcwd())
os.chdir(result)

# listdir()获取指定文件夹中所有内容的名称列表
result = os.listdir(result)
print(result)

# 当前文件夹
print(os.curdir)
# 上层文件夹
print(os.pardir)

# 进入上层文件夹
os.chdir(os.pardir)
print(os.getcwd())

#name 获取代表操作系统的名称字符串
print(os.name)

#sep 获取系统路径间隔符号
print(os.sep)

# 获取环境变量
result = os.getenv('PATH')
print(result)
print(result.split(';'))

 
#extsep 获取文件名称和后缀之间的间隔符号
print(os.extsep)

#linesep  获取操作系统的换行符号
print(repr(os.linesep))

# os.path子模块中的内容

#abspath()  将相对路径转化为绝对路径
print(os.listdir())
# os.chdir(os.path.join(os.getcwd(),'file_operation'))
print(os.getcwd())
path = 'file_operation'
print(os.path.abspath('file_operation'))

#dirname()  获取完整路径当中的目录部分  &  basename()获取完整路径当中的主体部分
print("dirname()  ---------------------")
cwd = os.getcwd()
result = os.path.dirname(cwd)
print(result)
print(os.path.basename(cwd))

#split() 将一个完整的路径切割成目录部分和主体部分
print(os.path.split(cwd))

#splitext() 将一个路径切割成文件后缀和其他两个部分,主要用于获取文件的后缀
path = os.path.join(cwd,'file_operation', '01_os_demo.py')
result = os.path.splitext(path)
print(result)

#getsize()  获取文件的大小
result = os.path.getsize(path)
print(result)

#isfile() 检测是否是文件
result = os.path.isfile(path)
print(result)
 
#isdir()  检测是否是文件夹
result = os.path.isdir(path)
print(result)
 
#islink() 检测是否是链接
result = os.path.islink(path)
print(result)


import time
#getctime() 获取文件的创建时间 get create time
#getmtime() 获取文件的修改时间 get modify time
#getatime() 获取文件的访问时间 get active time
print(time.ctime(os.path.getctime(path)))

#exists() 检测某个路径是否真实存在
filepath = '/home/sy/下载/chls'
result = os.path.exists(filepath)
print(result)
 
#isabs() 检测一个路径是否是绝对路径
path = '/boys'
result = os.path.isabs(path)
print(result)
 
 
#samefile() 检测2个路径是否是同一个文件
print("are they the same?-------")
path1 = os.path.join(cwd,'file_operation', '01_os_demo.py')
path2 = './file_operation/01_os_demo.py'
result = os.path.samefile(path1,path2)
print(result)
 
 
#os.environ 用于获取和设置系统环境变量的内置值
import os
#获取系统环境变量  getenv() 效果
print(os.environ['PATH'])
 
#设置系统环境变量 putenv()
# os.environ['PATH'] += ':/home/sy/下载'
# os.system('chls')