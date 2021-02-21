# Python发电子邮件

[toc]

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-09-144051.png)

## 简单邮件对象

```python
# 读取工作表文件数据
with open('./04_月考勤表.xlsx', 'rb') as f:
    file_data = f.read()

# 设置内容类型为附件
attachment = MIMEText(file_data, 'base64', 'utf-8')

# 设置附件标题以及文件类型
attachment.add_header('Content-Disposition', 'attachment', filename='04_月考勤表.xlsx')
```

## 设置附件标题及文件类型

```python
# 设置附件标题以及文件类型
attachment.add_header('Content-Disposition', 'attachment', filename = '04_月考勤表.xlsx')
# 其中：
# 'Content-Disposition','attachment' 为固定参数
# filename是可以自己命名的
```



文本格式作为附件时，会与正文有所不同，为：base64

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-09-151642.png)



* 简单邮件对象(MIMEText对象)：像一个物件，可以是一段文本，一个附件，可以单独作为邮件内容发出。
* 复合邮件对象(MIMEMultipart对象)：像一个容器，由多个简单邮件对象组合而成，一起作为邮件内容发出。当要发的邮件内容比较多样的时候，就需要用到复合邮件对象(MIMEMultipart对象)，来承载多个简单邮件对象(MIMEText对象)一起打包发送。



![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-09-165334.png)

## 复杂邮件对象

```python
# 实例化复合邮件对象
msg = MIMEMultipart()

# 设置发送者信息
msg['From'] = '陈知枫'
# 设置接受者信息。
msg['To'] = '闪光科技的同事们' 
# 设置邮件标题
msg['Subject'] = '04_月考勤表'

```



![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-09-165503.png)



* 将简单邮件对象，添加到复杂邮件对象：**使用attach()方法**

## 发送邮件并关闭服务

### sendmail()

```python
# 发送邮件
smtp.sendmail(from_addr, to_addrs, msg.as_string())
```

参数说明：

* fromaddr（发件邮箱地址）
* toaddrs（收件邮箱地址）
* msg.as_string() （邮件内容），msg是需要发送的邮件内容对象，可以是简单邮件对象也可食是符合邮件对象。其中，as_string()是将发送的信息msg变为字符串类型

### quit()

```python
# 关闭邮箱服务
smtp.quit()
```

### smtplib、email

![img](https://adamyide-1256435674.cos.ap-shanghai.myqcloud.com/2020-12-09-183143.png)

[返回目录](#目录)

