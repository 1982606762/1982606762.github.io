---
title: page和hexo搭建自己的博客
date: 2021-08-11 22:07:43
tags:
  hexo
categories:
  杂
---

之前用腾讯云的主机和wordpress建站，但是由于主机到期，所以打算换一个平台，找到了免费的github page

<!--more-->

github page虽然免费，但是不像vps那么强大，他只支持静态博客的搭建。没有数据库支持，更新文章需要使用git手动增量上传。博客生成器我用的是hexo，当然也有其他的解决方案。

1. 前置工作

   * 需要电脑有安装git
   * 安装node.js
   * 注册github账户
   * （非必选）域名
   * （非必选）markdown编辑器（推荐typora，vscode也能用而且相关插件很强大）

2. 在本地安装hexo

   打开控制台，输入以下代码

   > npm install hexo -g
   >
   > npm install hexo-server -g

   然后新建hexo项目

   > hexo init blog
   >
   > cd blog
   >
   > npm install
   >
   > hexo s

   等他提示打开localhost就可以看到博客已经打开了，ctrl/control+c可以关闭

   这时为了下边需要不要关terminal，还在blog目录下安装deploy-git

   > npm install hexo-deployer-git --save

3. 配置

   在blog文件夹中找一个叫做_config.yml的文件，打开它

   目前需要改的只有最开头Site部分，按照自己情况写标题作者什么的。

   然后打开github，新建一个仓库

   <img src="https://www.hualigs.cn/image/611cef5f7cb07.jpg" alt="image-20210818181723781" style="zoom:50%;" />

   在下一级新建一个仓库，名称填xxx.github.io，如

   [![fT5WdJ.md.png](https://z3.ax1x.com/2021/08/18/fT5WdJ.md.png)](https://imgtu.com/i/fT5WdJ)

   公开或者私密看你自己心情，然后创建

   再回到刚刚那个yml配置文件，拉到最下边deploy位置，按这个格式填入你刚刚创建的仓库信息然后保存文件。

   > deploy:
   >
   >  type: git
   >
   >  repository: https://github.com/1982606762/1982606762.github.io.git
   >
   >  branch: main

   现在配置文件设置好了，只需要用terminal  cd进blog文件夹使用hexo g&&hexo d就可以部署到远程仓库了。

   等他提示Deploy done的时候可以打开github仓库页面看看有没有部署完成，部署完成在这会有个√

   [![fT5fo9.md.png](https://z3.ax1x.com/2021/08/18/fT5fo9.md.png)](https://imgtu.com/i/fT5fo9)

   有的话就可以用xxx.github,io访问了。

4. 绑定自己的域名

   首先需要去比如说腾讯云或者阿里云注册一个域名，便宜的大概十来块一年。

   到刚刚blog文件夹下的source文件夹内新建一个叫CNAME的文件，注意文件不能有任何后缀。（mac系统新建之后如果用文本编辑器编辑他会自动添加txt后缀。。而且是隐藏的，所以需要用touch命令创建后用vim修改即可）

   修改这个文件内容为你刚刚申请的域名，只包含域名即可如xxx.com

   然后用terminal     hexo g&&hexo d，等他上传之后看看github仓库的这个位置

   [![fT55J1.md.png](https://z3.ax1x.com/2021/08/18/fT55J1.md.png)](https://imgtu.com/i/fT55J1)

   是不是显示published at你的域名

   [![fT5IRx.png](https://z3.ax1x.com/2021/08/18/fT5IRx.png)](https://imgtu.com/i/fT5IRx)

   有的话这边就算设置好了，然后去域名那边设置

   登录到你刚刚买域名的网站，找到控制台里的域名解析或者DNS解析之类的，里边有你刚刚买的域名。找到解析列表，点击添加记录，按照下图第二行设置即可，注意在记录值位置需要改成自己的github账户

   <a href="https://imgtu.com/i/fT54iR"><img src="https://z3.ax1x.com/2021/08/18/fT54iR.png" alt="fT54iR.png" border="0" /></a>

   添加完后等几分钟，等他生效。不出意外此时访问xxx.com(你的域名)就可以打开博客了。

5. 新建文章

   写文章首先需要新建，还是用terminal  cd到blog目录下输入`hexo new 我的博文xxx`其中第三个字段是文章名称。

   然后在blog/source/_posts目录下会多一个我的博文xxx.md的文件，用markdown编辑器打开会看到类似

   > Title:
   >
   > date
   >
   > tags
   >
   > --
   >
   > 

   ---下边就可以用markdown语句写文章，上边是一些参数，可以修改tags

   写完文章后保存这个文件，然后在terminal输入`hexo clean` 之后`hexo g&&hexo d`就可以上传到云端。这时再打开博客就可以看到新写的文章了
