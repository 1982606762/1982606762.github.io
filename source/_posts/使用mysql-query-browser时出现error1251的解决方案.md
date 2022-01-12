---
title: 使用MYSQL QUERY browser时出现error1251的解决方案
tags: []
id: '357'
categories:
  - - 杂
date: 2020-07-15 11:58:59
---

出现1251一般是密码问题

首先使用cmd 输入

```
mysql -u root -p
```

登录后输入

```
mysql> alter user root@localhost identified by 'newpassword' password expire never;

mysql> alter user root@localhost identified with mysql_native_password by 'newpassword';

mysql> flush privileges;　　　　# 刷新权限
```

newpassword是新密码

之后就可以正常链接了