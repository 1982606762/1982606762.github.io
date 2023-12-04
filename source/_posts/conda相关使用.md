---
title: conda相关使用
date: 2022-08-16 14:56:05
tags: [conda,python]
categories: Python
---

在管理本地Python环境的时候经常用到的就是conda，它可以简单快捷地切换Python环境。

<!--more-->

# 1. 安装

我之前使用过完整版的Anaconda，但是感觉有点太大了，并且也用不到哪些功能，所以就用miniconda来管理。

下载链接：

https://docs.conda.io/en/latest/miniconda.html

# 2. 指令

* 查看当前所有环境`conda env list`

* 创建新的环境`conda create -n ENVNAME python=3.10`

* 删除环境 `conda remove -n ENVNAME --all`

* 克隆环境 `conda create --clone ENVNAME -n NEWENV`

* 安装包`conda install xxx`

* 删除包`conda uninstall xxx`

* 查看包`conda list`

  
