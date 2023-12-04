---
title: hexo上github-pages后的一些优化
date: 2022-01-15 10:35:09
tags: hexo
categories: 前端
---

本文介绍使用github pages负载hexo的优化，包括push不受网络问题影响，网站https设置，使用CDN加速浏览

<!--more-->

# 使用ssh加速push操作

由于国内网络问题，使用http向github push的时候经常遇到卡顿或者无法连接的情况，建议使用ssh

首先需要用`ssh-keygen`来生成一个ssh密钥。然后把id_rsa.pub里的内容复制到github里

在_config.yml中将github链接改为ssh对应的链接，删除.git_deploy文件，使用hexo clean，然后再hexo g && hexo d



# 使用https给网页加密

在腾讯云可以免费申请ssl证书。申请后可以搭配下边cdn一起使用。在github pages位置开启强制HTTPS即可

# 使用CDN加速网站访问

在腾讯云-内容分发网络-域名管理新建针对网站域名的CDN服务

在原站配置选自有源，https![image-20220115111541902](https://gitee.com/Squirrel_01/img/raw/master/img/image-20220115111541902.png)

地址就填github官方给的地址

>```
>185.199.108.153
>185.199.109.153
>185.199.110.153
>185.199.111.153
>```

开启后在缓存位置可以改短一些，我设置的是1天缓存。缓存时间太长会导致网页更新后访问不到最新的页面。你也可以手动在刷新预热-URL刷新删除所有CDN缓存。

测试结果：

![1s-测速](https://gitee.com/Squirrel_01/img/raw/master/img/1s-%E6%B5%8B%E9%80%9F.png)

![1h-测速](https://gitee.com/Squirrel_01/img/raw/master/img/1h-%E6%B5%8B%E9%80%9F.png)

![1d-测速](https://gitee.com/Squirrel_01/img/raw/master/img/1d-%E6%B5%8B%E9%80%9F.png)
