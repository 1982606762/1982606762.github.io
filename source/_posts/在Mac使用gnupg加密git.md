---
title: 在Mac使用gnupg加密git
date: 2022-01-04 13:18:13
tags: Mac
categories: Linux
---

让你的git提交也能拥有酷炫的认证标志

<!--more-->

## 生成gpg密码并测试可以使用

首先需要下载安装gpg

``brew install gpg``

安装好之后看一眼有没有pinentry ``pinentry -h``

有的话用``which pinentry``查找一下在哪，没有的话使用``brew install pinentry``安装

找到目录后使用``vim ~/.gnupg/gpg-agent.conf`` 添加一行`` pinentry-program /usr/local/bin/pinentry``这里写你自己的路径

然后使用``gpg --full-generate-key``生成，跟着指引走即可，注意一点，邮箱需要和github里添加的一样

然后使用``echo "test"|gpg --clearsign``测试一下能不能用，在这一步可能会报错

> gpg: 签名时失败： Inappropriate ioctl for device
> gpg: [stdin]: clear-sign failed: Inappropriate ioctl for device

解决方案：编辑~/.gnupg目录下的gpg.conf和gpg-agent.conf两个文件

gpg.conf

```php
use-agent
pinentry-mode loopback
```

gpg-agent.conf

```undefined
allow-loopback-pinentry
```

更改完后使用``gpgconf --kill gpg-agent``重启gpg，然后再尝试，此时应该可以生成密码了

## 配置git

使用``gpg --list-secret-keys --keyid-format=long``查看当前的秘钥

> /Users/zxl/.gnupg/pubring.kbx
>
> sec   rsa3072/89E3C55059BE3D97 2022-01-04 [SC]
>       CE52DE13A3615D3687F9C82389E3C55059BE3D97
> uid                   [ 绝对 ] Zhaoxuanlang (It's me!) <1982606762@qq.com>
> ssb   rsa3072/1CF09AC8CF982194 2022-01-04 [E]

这里你密钥的ID是89E3C55059BE3D97

然后使用``gpg --armor --export 89E3C55059BE3D97``查看公钥，复制所有包括BEGIN和END的内容

进入github页面-settings-SSH-新增GPG，复制进去即可

还需要在本地设置git使用密钥

```
git config --global user.signingkey "GPG key ID"
```

然后在commit的时候使用``git commit -S -m "xxxx"``来加密本次提交，push之后就可以见到![image-20220104122352299](https://gitee.com/Squirrel_01/img/raw/master/img/image-20220104122352299.png)

防止每次都加-S太麻烦可以使用``git config --global commit.gpgsign true``来默认使用加密提交

此外，还可以使用``gpg --delete-secret-and-public-key your@email.addr``来删除已生成的本地密钥

或是两步删除密钥

``` 
gpg -k #列出所有密钥
gpg --delete-secret-keys id
gpg --delete-keys id
```



## 参考链接

https://blog.csdn.net/qq_33154343/article/details/106030946

https://superuser.com/questions/1628782/gpg-signing-failed-no-pinentry

https://docs.github.com/cn/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key

https://frostming.com/2019/11-25/git-commit-sign/

https://blog.chaos.run/dreams/using-gpg/

