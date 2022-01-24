---
title: 强制git使用ssh
date: 2022-01-22 22:01:49
tags: git
categories: Linux
---

国内使用github时由于网络问题，push和pull时经常会卡，因此建议使用ssh代替http.

<!--more-->

虽然在github页面可以直接选择使用ssh链接，但是有一些软件会使用git服务，这时就不是很好切换，我的例子是在使用cocoapods的时候没法pod install。所以尝试在gitconfig里强制使用ssh。

只需要在~/.gitconfig里加以下内容即可：

``` 
[url "git@github.com:"]
  insteadOf = https://github.com/
[url "git@github.com:"]
  pushInsteadOf = "git://github.com/"
[url "git@github.com:"]
  pushInsteadOf = "https://github.com/"
```

