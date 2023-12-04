---
title: 下载kindle购买书籍
date: 2022-06-22 00:08:00
tags: Amazon-kindle
categories:	其他笔记
---

随着kindle在大陆退出市场，我们需要把之前购买过的书籍都下载下来以防万一。

<!--more-->

# 1.批量下载图书

访问 [http://z.cn/myk](https://z.cn/myk) 并登录你的账号，进入电子书列表。把下列js代码保存成书签后在“内容”页点击书签就可以自动批量下载。

```js
javascript:(function()%7Bif(!window.location.hash.startsWith('%23%2Fhome%2Fcontent%2FbooksAll'))%7Balert('Need%20to%20visit%3A%20https%3A%2F%2Fz.cn%2Fmyk')%3Breturn%3B%7Dif(!confirm('Start%20now%3F'))return%3Bconst%20h%3Dz%3D%3Ez.replace(%2F%5B%EF%BC%88%EF%BC%89()%22%E2%80%9C%E2%80%9D%E3%80%8A%E3%80%8B%E3%80%90%E3%80%91%3A%EF%BC%9A%3B%EF%BC%9B%EF%BC%8C%2C.%E3%80%81%5C%2F%E2%80%A2%E3%80%82!%EF%BC%81%3F%EF%BC%9F_%26%C2%B7%E2%80%94%5Cs%2B-%5D%2Fg%2C'').replace('EnglishEdition'%2C'').toLowerCase()%3Bw%3Dms%3D%3Enew%20Promise(r%3D%3EsetTimeout(r%2Cms))%2Cn%3Dz%3D%3EparseInt(%24('.contentCount_myx').text().match(%2F(%5Cd%2B)%2Fg)%5Bz%5D)%2Ca%3Dn(0)%2Cp%3Dz%3D%3Econsole.log(z)%3Blet%20c%3D0%2Cv%3D0%2Co%3D0%2Cx%3D%5B%5D%3Basync%20function%20d()%7Blet%20ls%3D%24('.contentTableListRow_myx%20li')%2Cl%3Dls.length%2Cs%3Dn(2)%3Bif(l%3C200%26%26s%3Ca)%7Bwindow.scrollTo(0%2C%24('body').outerHeight())%3B%7Delse%7Bc%2B%3Dl%3Bfor(const%20j%20of%20ls.get())%7Bconst%20t%3D%24(j).find('div%5Bbo-text%3D%22tab.title%22%5D').text()%3Bp('Downloading%3A%20'%2Bt)%3B%24(j).find('button%5Baria-label%3D%22actions%22%5D').click()%3Bconst%20u%3D%24('%23contentAction_download_myx')%3Bif(u.is('%3Ahidden'))%7Bo%2B%3D1%3Bp('sample%2C%20ignore')%3Bcontinue%3B%7Dif(x.length%26%26x.includes(h(t)))%7Bo%2B%3D1%3Bp('duplicate%2C%20ignore')%3Bcontinue%3B%7Du.click()%3Bif(%24('div%5Bng-show%3D%22noDeviceEligible%22%5D').is('%3Avisible'))%7Bconst%20m%3D'No%20available%20Kindle%20device.'%3Balert(m)%3Bp(m%2B'%20Exit.')%3Breturn%3B%7D%24('a%5Bid%3D%22dialogButton_ok_myx%20%22').click()%3Bv%2B%3D1%3Bp(%60Total%3A%20%24%7Ba%7D%2C%20Done%3A%20%24%7Bv%7D%2C%20Ignore%3A%20%24%7Bo%7D%60)%3Bawait%20w(10000)%3B%7Dif(s%3D%3Da)%7Bp('Done.')%3Breturn%3B%7Delse%7B%24('.contentTableShowMore_myx').eq(1).click()%3B%7D%7Dawait%20w(2000)%3Bawait%20d()%3B%7Dfunction%20q()%7Bif(confirm('Need%20to%20exclude%20files%3F'))%7B%24('body').append('%3Cinput%20id%3D%22e%22%20type%3D%22file%22%20style%3D%22display%3Anone%3B%22%20webkitdirectory%3E')%3Bconst%20e%3D%24('%23e')%3Be.change((ev)%3D%3E%7Bfor(const%20f%20of%20ev.target.files)%7Bx.push(h(f.name.replace(%2F%5C.azw.*%24%2F%2C'')))%3B%7Dd()%3B%7D)%3Be.click()%3B%7Delse%7Bd()%3B%7D%7Dq()%7D)();
```

# 2.解密与转换格式

由于直接从官网下载的图书是DRM加密的，我们需要解密并且更换格式。这里需要用到两个工具：

- **下载 Calibre**：[官方下载页面](https://calibre-ebook.com/download) ｜ [Github 发布页](https://github.com/kovidgoyal/calibre/releases)
- **下载 DeDRM 插件**：[分叉版本](https://github.com/noDRM/DeDRM_tools/releases) ｜ [原始版本](https://github.com/apprenticeharper/DeDRM_tools/releases)（已停止维护）

注意，移除 DRM 是为了维护自己的合法权益，为避免触犯版权方的权益，请勿分发到互联网上。为保护个人隐私及电子书文件不被外泄，建议避免使用任何在线形式的 DRM 去除工具。

下载后先安装Calibre，这一步需要选kindle，其他步骤下一步即可。

![img](https://img.zhaoxuanlang.cn/v2-e66ea24afe92775b4dc3bc24f3f4fa7a_1440w.jpg)

DeDRM插件解压缩后有一个DeDRM_plugin.zip文件，去calibre中首选项-插件-从文件加载插件-选择刚刚那个zip文件-确定-确定-选择这个插件-自定义-eInk Kindle ebooks-点加号，输入你kindle的 序列号（16位）-保存关闭设置页面

![选择插件](https://img.zhaoxuanlang.cn/v2-9b2a9caf7ec2d635a9ad71fec604f9fa_1440w.jpg)

这里就设置完成了，现在可以把刚刚下好的书籍直接拖进软件中，点上边转换书籍，右上角可以选输出格式，输出即可。

![image-20220622上午121826096](https://img.zhaoxuanlang.cn/image-20220622%E4%B8%8A%E5%8D%88121826096.png)

# 3.用脚本提取epub图书

刚刚转换出来的目录格式很不人性化，类似这样：

-dir
	-a/a.epub
	-b/b.epub
	-c/c.epub

这样手工选择就很麻烦，所以需要写个脚本来自动遍历，脚本内容如下：

```sh
#! /bin/bash
# 更改IFS变量，以换号符作为for循环的分隔符
oldIFS=$IFS
IFS=$'\n'
mkdir epubs azw3s
for dir1 in `ls /Users/zxl/Calibre\ 书库/`
do
    for dir2 in `ls /Users/zxl/Calibre\ 书库/$dir1`
    do
        cd /Users/zxl/Calibre\ 书库/$dir1/$dir2
        book=`ls | grep ".epub"`
        echo processing $book .......
        sudo cp $book ~/epubs/$book
        azw3=`ls | grep ".azw3"`
        echo processing $azw3 .......
        sudo cp $azw3 ~/azw3s/$azw3
    done
done
echo "done"
```

运行即可自动把epub和azw3文件分类放好。
