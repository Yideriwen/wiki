### 数据导入
```python
df = pd.read_csv(<path+filename>,encoding = 'gbk',sep=',',skiprows = 1,parse_dates = [<列名>])

```

- `# sep = <character> 数据间的分隔符`
- `# skiprows = <number> 跳过读取的行数`
- `# parse_dates = <columns name> 指定列为日期格式`


- `# 处理字符串：字符串开头加r变为raw string`
- `# 常见编码格式：gbk, utf-8等`
- `# 读取前n行数据：nrows = <n>`
- `# 指定列设置为index：index_col = [<column name>]`
- `# 指定读取某些列：usecols = [<column1,column2>]`
- `# 当数据有问题，直接跳过该行，不报错：error_bad_lines = False`
- `# 将数据中的null识别为空值：na_values = 'NULL'`



