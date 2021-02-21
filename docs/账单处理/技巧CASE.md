# 技巧CASE

## 重置df的index（索引），让其从0开始

```python
df.index = range(len(df))
```

[返回目录](#目录)

## 把list（列表）放入df中

```python
df = pd.DataFrame(columns=list("ABC"))
df.loc[len(df)] = [1,2,3]
```

[返回目录](#目录)

## list（列表）转换为dict（字典）

```python
a = ['a1','a2']
b = ['b1','b2']
c = [a,b]
dict(c)
```

[返回目录](#目录)

## 对list（列表）中的元素进行切片操作

```python
files1 = glob.glob(path+'/*.xlsx')
files2 = glob.glob(path+'/*.xls')

files1 = [a[:45] for a in files1]
files2 = [a[:45] for a in files2]
```

[返回目录](#目录)

## 比较两个list（列表）的不同

```python
set(files1).difference(set(files2))
```

[返回目录](#目录)

## 将csv中的数字按字符串读取，解决数字前0被消失的问题

```python
df = pd.read_csv('/Users/yideriwen/DA/DA/Public_Code/data.csv', dtype={'股票代码':str})
```

[返回目录](#目录)

## 自动检测文件编码格式

```python
import chardet
def get_encoding(file):
    with open(file,'rb') as f:
        tmp = chardet.detect(f.read())
        return tmp['encoding']
```

[返回目录](#目录)

## 读取某目录下的CSV格式文件并入一个DataFrame

```python
import glob
import pandas as pd

# get data file names
path ='/Users/yideriwen/Nutstore Files/000 MyFiles/000 - InBox I 我的InBox体系/001 - Inbox - 原料中转站/【拼多多】1.0账单数据/预付费'
filenames = glob.glob(path + "/*.csv")

dfs = []
for filename in filenames:
    dfs.append(pd.read_csv(filename,encoding = 'GB2312'))
# Concatenate all data into one DataFrame
big_frame = pd.concat(dfs, ignore_index=True)
```

