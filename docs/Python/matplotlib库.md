# matplotlib库


## 导入

`from matplotlib import pyplot as plt`

绘图用pyplot模块即plt

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-13-185847.png)

## 画图流程

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-14-094951.png)

### 1. 生成画布

`plt.figure(figsize = (6,6)) `生成一个长宽都为6的画布

### 2. 设置X轴和Y轴的值

二维表一般一个索引，一个值

```python
x = order_number.index
y = order_number.values
```

### 3. 绘图

`plt.plot(x,y)`

### 4. 调整图形样式

#### 线条宽度

`linewidth`（可以简写为：lw）

`plt.plot(x, y, linewidth = 3)`

#### 颜色

`color`

`plt.plot(x, y, linewidth = 2, color = 'r')`

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-14-102406.png)

#### 标记

`marker`

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-14-102609.png)

`plt.plot(x, y, linewidth = 2, color = 'r', marker = 'o')`

![image-20201214182832284](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-14-102833.png)

marker的颜色、大小设置：

`markerfacecolor`

`markersize`

`plt.plot(x, y, linewidth = 2, color = 'r', marker = 'o', markerfacecolor = 'blue', markersize = 8)`

![image-20201214183201621](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-14-103202.png)

### 小结

![img](https://res.pandateacher.com/69UTC8TF1605598798757.png)

### 5. 调整x轴和y轴样式

#### 调整x轴和y轴刻度

`plt.xticks()`

`plt.yticks()`

```python
plt.xticks(size = 12)
plt.yticks(size = 12)
```

#### x轴y轴标签

`plt.xlabel()`

`plt.ylabel()`

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-14-103803.png)

```python
plt.xlabel('月份', fontdict = {'size': 15})
plt.ylabel('各月总订单量', fontdict = {'size': 15})
```

size参数控制字体大小

#### 设置图形标题

`plt.title('各月总订单量变化折线图',fontsize = 15)`

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-14-104059.png)

#### 6. 保存图形

`plt.savefig('文件路径+文件名')`

#### 回顾

##### 画折线图

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-14-105645.png)

##### 画柱状图

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-14-111005.png)

##### 饼图



![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-14-111825.png)

爆炸效果的起始位置：

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-14-111916.png)

数据源按顺序排列

###### 设置图例

`plt.legend()`

`plt.legend(labels = order_number.index)`

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-14-112119.png)

##### 总结

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-14-161453.png)

[返回目录](#目录)

