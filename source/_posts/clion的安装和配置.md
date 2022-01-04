---
title: clion的安装和配置
tags: []
id: '223'
categories:
  - - c/c++语言
date: 2020-03-05 09:47:55
---

写代码时一个易用的编译器是很重要的，若想写c/c++我推荐jetbrain家的clion，真的很方便

首先去官网下载[官网页面](https://www.jetbrains.com/clion/)并安装

在这不提供破解方法，建议支持正版，破解方法可以在百度上搜索到

之后需要下载一个c/c++的译码器，我在这用的是MingW.不建议去官网下载，因为即使科学上网速度也还是很慢而且容易出错

在这提供我的百度网盘收藏链接，直接下载安装即可

链接：https://pan.baidu.com/s/1xYOb-eYFKSfJgwFxG9fZWw  
提取码：kiec

**（2）配置CLion**  
打开CLion，左上角File-Settings-Build-Toolchains，然后点击 **+** 号  

![](//upload-images.jianshu.io/upload_images/13625730-59b19c35c9589ad0.png?imageMogr2/auto-orient/stripimageView2/2/w/908/format/webp)

settings

![](//upload-images.jianshu.io/upload_images/13625730-9c1c7b4ac50f2320.png?imageMogr2/auto-orient/stripimageView2/2/w/624/format/webp)

toolchains

Environment选择MinGW，然后填入刚刚解压的MinGW64的路径（这是我的路径）：

```
C:\Users\71022\Documents\mingw64
```

![](//upload-images.jianshu.io/upload_images/13625730-c97f11fcde1a679f.png?imageMogr2/auto-orient/stripimageView2/2/w/780/format/webp)

image.png

然后CLion会自动帮你填上所有你该填的东西，点击OK，等调试的小虫子变绿就可以了。

![](//upload-images.jianshu.io/upload_images/13625730-9f5aa1e8408cef27.png?imageMogr2/auto-orient/stripimageView2/2/w/781/format/webp)

image.png

**当然，也会出现无法检测成功的情况，这时候就需要手动填写啦。**  
CMake一般会自动选择。  
Make填入路径：

```
C:\Users\71022\Documents\mingw64\bin\mingw32-make.exe
```

C Compiler填入路径：

```
C:\Users\71022\Documents\mingw64\bin\gcc.exe
```

C++ Compiler填入路径：

```
C:\Users\71022\Documents\mingw64\bin\g++.exe
```

Debugger一般会自己填入，如果没有可以手动填：

```
C:\Users\71022\Documents\mingw64\bin\gdb.exe
```

然后OK，等一段时间就可以了。