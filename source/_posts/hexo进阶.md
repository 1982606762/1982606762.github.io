---
title: hexo进阶
date: 2021-08-21 08:00:29
tags:
  hexo
categories:
  杂
---

实现一些hexo的进阶操作

<!--more-->

# 使用next主题美化

## 安装主题

Next主题的安装方式很简单，只需要在博客主目录下执行：

```
git clone https://github.com/theme-next/hexo-theme-next themes/next
```


然后设置站点配置文件_config.yml：

``` 
theme: next
```

即可将我们的Hexo博客主题替换为Next主题。

## 设置主题

进入到blog/themes/next目录会看到有一个_config.yml文件，打开它，每一项都有相应的注释介绍，按照自己喜好进行修改即可，这里不多介绍。

# 设置typora自动上传图片

我用的编辑器是typora，但是在插入图片的时候默认是存在本地，这样部署到远程之后这些图片是显示不了的。一种解决方案是每张图都上传到图床然后手动插入文章，但是略显繁琐，因此需要设置让编辑器自动帮我们上传图片

## 所需软件下载

我用的是PicGo+gitee的方式，这里如果用github就会因为网速原因有点卡。

首先下载[PicGo](https://github.com/Molunerfinn/PicGo/releases)，下载对应自己电脑的版本即可

[![fjRO4e.png](https://z3.ax1x.com/2021/08/21/fjRO4e.png)](https://imgtu.com/i/fjRO4e)

然后解压安装balabala不谈

## 设置PicGo和gitee仓库

安装好打开软件，左边菜单最下边有一个插件设置，点进去搜索gitee，应该会有三个，全安装即可，我这里全安装了但是只显示出了一个。

[![fjRHHK.png](https://z3.ax1x.com/2021/08/21/fjRHHK.png)](https://imgtu.com/i/fjRHHK)

安装好点图床设置，应该就会有gitee了

[![fjR7B6.png](https://z3.ax1x.com/2021/08/21/fjR7B6.png)](https://imgtu.com/i/fjR7B6)

这时我们需要去gitee新建一个仓库

[![fjRLND.png](https://z3.ax1x.com/2021/08/21/fjRLND.png)](https://imgtu.com/i/fjRLND)

然后还需要去获取一个token。按下图进入，点生成新令牌，名字随便起一个就可以

[![fjRqAO.png](https://z3.ax1x.com/2021/08/21/fjRqAO.png)](https://imgtu.com/i/fjRqAO)

现在需要回到PicGo设置界面，点击刚刚的Gitee图床选项，填入信息

> Owner：Gitee用户名
>
> repo：刚刚新建的仓库名
>
> path：可有可无，和仓库名一样就可以
>
> token：填入你刚刚申请到的token

[![fjRj9H.png](https://z3.ax1x.com/2021/08/21/fjRj9H.png)](https://imgtu.com/i/fjRj9H)

然后点确定。点了就行，它没有什么保存成功的提示。。

## 设置typora

进入typora的设置点击图像栏，如图设置后点击验证一下

[![fjRv3d.png](https://z3.ax1x.com/2021/08/21/fjRv3d.png)](https://imgtu.com/i/fjRv3d)

[![fjRxgA.png](https://z3.ax1x.com/2021/08/21/fjRxgA.png)](https://imgtu.com/i/fjRxgA)

注意多次测试可能会验证失败。查阅PicGo.log发现提示文件已存在

[![fjRzjI.png](https://z3.ax1x.com/2021/08/21/fjRzjI.png)](https://imgtu.com/i/fjRzjI)

只需要去PicGo软件的相册内删除他测试用的两个typora图标即可。

测试成功后你向typora文章内新增图片，它会自动帮你上传并更换连接。

# hexo新建文章后自动打开

每次使用`hexo new xxx` 命令后它会在source文件夹下新建一个文章，还需要再用命令行或者手动来打开文件，同样略显繁琐，所以尝试使用node.js来完成自动化新建打开。

进入blog文件夹，新建一个目录名为scripts，在里边新建一个js文件，名字随意。

编辑这个js文件，写入以下监听事件

```javascript
var exec = require('child_process').exec

hexo.on('new',function(data){
	exec('open '+[data.path]);
});
```



这里open也可以换成code（如果你用的是vscode来编辑文章），注意open后边有一个空格，不要漏了。

然后在terminal里使用`hexo new xxx`命令后他就会自动新建并打开文件辣，可以直线提升100%的效率~
