---
title: Kexue上网查资料
tags: []
id: '83'
categories:
  - - 杂
date: 2019-10-10 11:16:46
---

在管控越来越严的形势下，以前的很多软件都不能再用了，所以自己动手丰衣足食才是最好的方法。

所需软件：1.[Xshell](http://链接：https://pan.baidu.com/s/1dNTBc5rHUXoVC9F5Hh3ttA  ) 提取码opph  2.[shadowsocksr](http://链接：https://pan.baidu.com/s/1NJmhSbLI3SIjRJVgvxKQlg  )      2o4c       

## 一：购买服务器

首先我们需要一个jingwai服务器，我是在 [vultr](https://www.vultr.com/?ref=7743951) 购买的。注册账号后首先选择自己需要的服务器。

![](http://www.zhaoxuanlang.cn/wp-content/uploads/2019/10/image-1024x441.png)

选择第一个

下边的地区根据自己的需求选择即可。

![](http://www.zhaoxuanlang.cn/wp-content/uploads/2019/10/image-1-1024x641.png)

下边的大小选最小的就可以满足需求

之后部署即可。

![](http://www.zhaoxuanlang.cn/wp-content/uploads/2019/10/image-2-1024x368.png)

## 二：连接到服务器

打开xshell，输入刚刚部署的服务器ip后他会自动连接。现在会有两种可能的结果

![](http://www.zhaoxuanlang.cn/wp-content/uploads/2019/10/image-3.png)

一直显示连接中

![](http://www.zhaoxuanlang.cn/wp-content/uploads/2019/10/image-4.png)

瞬间连接上

若是2，那么恭喜你，你的服务器可以用。若是1，现在就需要再去刚刚那个网站，把刚买的fwq销毁掉再买一个，知道出现2即可

## 三：配置

这一步很简单，首先使用 `wget --no-check-certificate https://freed.ga/github/shadowsocksR.sh; bash shadowsocksR.sh` 自动安装

然后安装加速插件，先使用wget -N --no-check-certificate https://freed.ga/kernel/ruisu.sh && bash ruisu.sh更换ubantu版本

再使用wget -N --no-check-certificate https://raw.githubusercontent.com/91yun/serverspeeder/master/serverspeeder-all.sh && bash serverspeeder-all.sh安装加速

![](http://www.zhaoxuanlang.cn/wp-content/uploads/2020/02/image.png)

四：使用

使用刚刚下载的第二个软件输入内容即可