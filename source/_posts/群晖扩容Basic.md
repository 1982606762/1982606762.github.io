---
title: 群晖扩容Basic
date: 2024-02-10 15:42:05
tags: 群晖
categories: 其他笔记
---

扩容单块硬盘的Basic存储池记录。

<!--more-->

## 升级Raid1

先把要更换的盘插进群晖后开机，然后进存储管理器选择要升级的Basic，更改Raid类型改成Raid1.

## 降级Basic

关机后把所有其他盘都拔出，只剩要更换的新盘放到刚刚旧盘的盘位里,然后开机。

用SSH链接到群晖，登录管理员账号后先使用`cat /proc/mdstat`.

![image-2024021041829465 PM](https://raw.githubusercontent.com/1982606762/picgo/master/image-2024021041829465%E2%80%AFPM.png)

然后输入命令`mdadm --grow --raid-devices=1 --force /dev/md3`.

## 恢复存储空间

把所有盘都插回去，然后进存储管理器的总览，选修复，他就会自动修复，修复好后去存储空间选择刚刚这个，他显示可以扩容，扩容即可。
