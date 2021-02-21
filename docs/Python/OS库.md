# OS库

## 快速获取文件名

```
import os

path = '/home/python-class/lesson1-2/work/参考资料'
filenames = os.listdir(path) #listdir 显示所有文件夹名和文件名

print(filenames)
```

## 文件/目录部分操作

```
os.remove() #删除一个文件
os.path.isfile(path) #是否存在这个文件，path是一个存在的文件
os.path.isdir(path) #是否存在这个目录，path是一个目录
os.getcwd() #获取当前工作目录

os.environ #获取系统环境变量上百个函数
```

## 文件打开关闭读取等操作

```
target_file = './工作文件夹/05_20_2020会议记录.txt'
file = open(target_file,'r',encoding = 'utf-8')
content = file.read()
print(content)
file.close()

# 另一种打开文件的方法
with open(target_file,'r',encoding = 'utf-8') as file:
  xxx
```

## 文件写入操作

```
# 目标文件是工作文件夹内的06_01_2020会议记录.txt文件
target_file = './工作文件夹/06_01_2020会议记录.txt'
# 需要添加的内容列表
content_list = ["会议记录：陈知枫", "会议复盘：徐小刚", "会议室清洁：廖雨"]
# 使用 open() 函数打开 06_01_2020会议记录.txt 文本文件，并使用追加模式'a'，记得将编码设置为'utf-8'
file = open(target_file, 'a', encoding='utf-8')
# 使用for循环遍历内容列表
for content in content_list:
    # 使用方法，文件对象.write()
    file.write(content+'\n')
# 关闭文件对象
file.close()
```

## 文件筛选与读写

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-11-21-153250.jpg)

[返回目录](#目录)