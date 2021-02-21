# openpyxl库


**用来操作excel表格**

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-11-22-164703.jpg)

## 概览

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-11-23-165741.png)

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-11-23-165901.png)

## 获取工作簿对象

1. 直接在已有文件中读取：

```python
from openpyxl import load_workbook

# 打开【公司人员名单.xlsx】工作簿
staff_wb = load_workbook('./codes/material/公司人员名单.xlsx')
# 打印工作簿对象
print(staff_wb)
```

2. 先创建再说，可能后面会存成文件

```python
from openpyxl import Workbook

# 新建工作簿
new_wb = Workbook()
# 将新建的工作簿保存为【new_excel.xlsx】
new_wb.save('./new_excel.xlsx')
```

其实，第一个case中的staff_wb也是可以存为文件的

综合，如图：

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-11-22-165740.jpg)

## 获取活动的工作表

ws = wb.active

## 工作表操作

获取某个工作簿的工作表：

```python
from openpyxl import load_workbook

# 打开【公司人员名单.xlsx】工作簿
staff_wb = load_workbook('./codes/material/公司人员名单.xlsx')
# 按表名取表
fhy_ws = staff_wb['上半年公司名单']  # fhy为first half year（上半年）的缩写
shy_ws = staff_wb['下半年公司名单']  # shy为second half year（下半年）的缩写

# 打印工作簿对象
print(staff_wb)
# 打印工作表对象
print(fhy_ws)
print(shy_ws)
```

> workbook['worksheet_name']

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-11-22-180114.jpg)

## 操作工作表的行列

> * 可以通过`工作表对象[行数]`或`工作表对象['列名']`的方式获取到一个**元组**，这个**元组**中包含了指定行或列中的所有数据
> * 可以借助工作表对象的方法`iter_rows()`来得到表格中指定范围内的多行数据

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-11-22-181015.jpg)

> 参数`min_row`和`max_row`分别表示最小行索引和最大行索引，最小行索引的值默认为1，最大行索引的值默认为表格中有数据的最下面一行的行数；
>
> 参数`min_col`和`max_col`分别表示最小列索引和最大列索引，最小列索引的值默认为1，最大列索引的值默认为表格中有数据的最右面一列的列数;
>
> 参数`values_only`决定是否返回单元格的值，如果为True则返回**单元格的值**，如果为False则返回**单元格对象**。通常情况下，只读数据时，需要将该参数设置为True，要写入数据时，保持其为默认的False就好。
>
> `value_only`的默认值为False，返回的是单元格对象，即包含格式等信息。
>
> 当需要取单元格对象值的时候，需要：单元格.value，才能得出。
>
> 打印行：
>
> ```python
> for row in 工作表对象.iter_rows()
> ```
>
> 当参数values_only为默认False时，row就是一个个单元格对象组成的**元组**

### 增加行

```python
info_tuple = ('S1912', '吴琐薇', 5000, '销售')
staff_ws.append(info_tuple)
```

## 操作单元格

* 什么是单元格

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-11-23-071604.png)

excel的操作最终都可以细化到单元格的操作。

单元格对象，只针对单元格，不管是否单元格中有数据：

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-11-23-072339.png)

单元格对象和列表的区别：

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-11-23-072453.png)

### 调用单元格的3种方式：

1. 通过iter_rows()及索引取出单元格对象

2. for cell in 工作表对象[行数] ｜ for cell in 工作表对象['列名']，可以指定单元格，如A1、A2等等，for cell in ws['A1']。

   取出的就是`单元格对象`如果要取值，就是`.value`

3. 工作表对象['A1']

    

   ![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-11-26-165820.png)

### 单元格对方向的基本操作

```python
# 获取单元格的值
单元格对象.value
# 给单元格对象赋值
单元格对象.value = 值
```

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-11-23-074528.png)

## 样式和图形的操作

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-11-23-165550.png)

## Excel文件的读写

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-11-26-170322.png)

## Excel表格数据字典化

```python
for row in performance_ws.iter_rows(min_row=2, values_only=True):
取出工号
    member_number = row[0]
    # 将信息存入员工信息字典
    staff_info[member_number] = {
         '姓名': row[1],
         '部门': row[2],
         '绩效': row[3],
         '奖金': row[4],
         '基本工资': row[5],
         '是否确认': row[6]
     }
```

### 取表头的套路

```python
# 获取表头，把表头放入列表
late_header = []
for cell in ws[1]:
    late_header.append(cell.value)
    
……

# 将表头写入新工作簿的工作表中
new_ws.append(late_header)
```

## 筛选匹配

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-08-073320.png)

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-08-073710.png)


## 设置excel样式

```python
import os
from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Alignment, Side, Border

# 定义表头颜色样式为橙色
header_fill = PatternFill('solid', fgColor='FF7F24')
# 定义表中、表尾颜色样式为淡黄色
content_fill = PatternFill('solid', fgColor='FFFFE0')
# 定义表尾颜色样式为淡桔红色
bottom_fill = PatternFill('solid', fgColor='EE9572')

# 定义对齐样式横向居中、纵向居中
align = Alignment(horizontal='center', vertical='center')

# 定义边样式为细条
side = Side('thin')
# 定义表头边框样式，有底边和右边
header_border = Border(bottom=side, right=side)
# 定义表中、表尾边框样式，有左边
content_border = Border(left=side)

# 设置文件夹路径
path = './各部门利润表汇总/'
 # 返回当前目录下所有文件名
files = os.listdir(path)

 # 循环文件名列表
for file in files:
    # 拼接文件路径
    file_path = path + file
    # 打开工作簿
    wb = load_workbook(file_path)
    # 打开工作表
    ws = wb.active

    # 调整列宽
    ws.column_dimensions['A'].width = 10
    ws.column_dimensions['B'].width = 25
    ws.column_dimensions['C'].width = 50
    ws.column_dimensions['D'].width = 10
    ws.column_dimensions['E'].width = 20
    ws.column_dimensions['F'].width = 15

    # 循环第一行单元格，调整表头样式
    for cell in ws[1]:
        # 设置单元格填充颜色
        cell.fill = header_fill
        # 设置单元格对齐方式
        cell.alignment = align
        # 设置单元格边框
        cell.border = header_border

    # 获取最后一行行号
    row_num = ws.max_row

    # 从第二行开始，循环到倒数第二行
    for row in ws.iter_rows(min_row=2, max_row=(row_num-1)):
        # 循环取出单元格，调整表中样式
        for cell in row:
            cell.fill = content_fill
            cell.alignment = align
            cell.border = content_border

    # 循环最后一行单元格，调整表尾样式
    for cell in ws[row_num]:
        cell.fill = bottom_fill
        cell.alignment = align
        cell.border = content_border

    # 保存
    wb.save(file_path)
```

![img](https://res.pandateacher.com/6BKRYK4W1596205188186.png)

| 功能           | 代码                                                         | 备注 |
| -------------- | ------------------------------------------------------------ | ---- |
| 调整工作表列宽 | Sheet.column_dimensions['列位置'].width `eg:ws.column_dimensions['A'].width = 20` |      |
| 边框样式       | Cell.border                                                  |      |
| 颜色填充       | Cell.fill                                                    |      |
| 对齐方式       | Cell.alignment                                               |      |

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-10-131952.png)

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-10-144055.png)

## 添加excel图表

### 条状图

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-10-160440.png)

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-10-163852.png)

```python
import os
from openpyxl import load_workbook
from openpyxl.chart import LineChart, Reference

# 设置目标文件夹路径
path = './各部门利润表汇总/'
# 获取文件夹下的所有文件名
file_list = os.listdir(path)
# 遍历文件名列表，取得每一个文件名
for file_name in file_list:
    # 拼接文件路径
    file_path = path + file_name
    print('正在处理：' + file_name)
    # 读取工作簿
    wb = load_workbook(file_path)
    # 定位到工作簿中的活跃工作表
    ws = wb.active

    # 实例化 LineChart() 类，得到 LineChart 对象
    chart = LineChart()
    # 引用工作表的部分数据
    data = Reference(worksheet=ws, min_row=3, max_row=9, min_col=1, max_col=5)
    # 添加被引用的数据到 LineChart 对象
    chart.add_data(data, from_rows=True, titles_from_data=True)
    # 添加 LineChart 对象到工作表中，指定生成折线图的位置
    ws.add_chart(chart, "C12")

    # 引用工作表的表头数据
    cats = Reference(worksheet=ws, min_row=2, max_row=2, min_col=2, max_col=5)
    # 设置类别轴的标签
    chart.set_categories(cats)
    # 设置 x 轴的标题
    chart.x_axis.title = "季度"
    # 设置 y 轴的标题
    chart.y_axis.title = "利润"
    # 设置折线图的颜色
    chart.style = 48

    # 保存工作簿
    wb.save(file_path)
```

![img](https://res.pandateacher.com/OCVG22PY1596195295419.png)

### 柱状图

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-10-165421.png)

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-10-165517.png)

[返回目录](#目录)

# 