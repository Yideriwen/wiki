# Tips

## 关于字符串前的'r'，斜杠的正确处理方式：

> 【路径】**必须**写成双反斜杠 F:\\Code\\Q1Branch或加个r，像这样： r“F:\Code\Q1Branch”

[返回目录](#目录)

## 怎么省略写模块名：

> 正常需要写：库名.模块名，多行的时候就不方便了
>
> 在import上做文章：from 库/模块 import 函数/方法/类/变量
>
> 这样就可以省略写模块名了
>
> ```python
> import openpyxl
> 
> # 通过文件路径，打开工作簿
> wb1 = openpyxl.load_workbook('./demo_excel.xlsx')
> # 用 Workbook() 创建新工作簿
> wb2 = openpyxl.Workbook()
> ```
>
> 上面是还需要写模块名的状态
>
> 下面是不需要的状态：
>
> ```python
> from openpyxl import load_workbook, Workbook
> 
> # 通过文件路径，打开已有工作簿
> wb1 = load_workbook('./demo_excel.xlsx')
> # 用 Workbook() 创建新工作簿
> wb2 = Workbook()
> ```
>
> ![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-11-22-164449.jpg)

[返回目录](#目录)

## 时间戳转字符串
`timestamp`转`str`:
```python
<timestamp>.strftime('%Y-%m-%d')
```
