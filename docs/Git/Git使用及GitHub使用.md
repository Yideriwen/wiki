# 1. 安装Git
使用brew安装
# 2. 创建版本库
```zsh
$ git init
```

在需要进行版本管理的对象目录中执行该命令，会在目录里创建一个`.git`文件夹，用来存储版本相关文件

`.git`不可见，可输入`ls -ah`后查看

# 3. 版本管理
## 1）查看仓库状态
```zsh
$ git staus
```

## 2）查看每个版本的变化情况
```zsh
$ git diff <filename>
```

## 3）提交修改到stage【暂存区】
```zsh
$ git add <filename>
```

## 4）从【暂存区】提交到master【当前分支】
```zsh
$ git commit -m "<description>"
```

# 4. 与GitHub关联及设置
## 1）创建SSH Key
先看有没有：
```zsh
$ cd ~/.ssh
```

if 有：
	id_ras ：是私钥
	id_rsa.pub ：是公钥
- 私钥：重要保密
- 公钥：可公开
else：
```zsh
$ ssh-keygen -r rsa -C "<youemail>"
```
可不设置密码

## 2）GitHub上的配置
头像——setting——左侧菜单栏“Add SSH Key”——添加：
- Title：便于区分和识别的标题
- Key：id_rsa.pub中的文件内容

## 3）添加远程库
创建新库：
“Create new repo"
添加到远程：
```zsh
$ git remote add origin git@github.com:<yourname>/<your repo name>.git
```
origin是默认远程库的叫法

## 4）把本地内容推送到远程
```zsh
$ git push -u origin master
```

