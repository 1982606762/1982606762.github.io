---
title: haskell 学习
date: 2022-04-13 22:12:04
tags:
categories: haskell
---

<!--more-->

首先去下载ghcup，它会帮你下载ghc和所需的其他软件

在命令行输入ghci进入交互式界面，`:set prompt "ghci>"`可以设置左侧提示栏。

# 函数

函数调用模板：funcname a b

函数定义：funcname para1 para2 = para1+para2

函数必须返回一个值

# List

定义直接用方括号定义，如list1 = [1,2,3]

获取值使用`list1 !! 1`

## 连接

遍历左边的字符串然后再处理

```haskell
list = [1,2,3,4] ++ [5,6,7,8]
```

在前端插入

```haskell
list = 1 : [2,3,4,5]
```

## 快速获取

**head** 返回一个 List 的头部，也就是 List 的首个元素。

```haskell
ghci> head [5,4,3,2,1] 

5
```

**tail** 返回一个 List 的尾部，也就是 List 除去头部之后的部分。

```haskell
ghci> tail [5,4,3,2,1]  

[4,3,2,1]
```

**last** 返回一个 List 的最后一个元素。

```haskell
ghci> last [5,4,3,2,1]  

1
```

**init** 返回一个 List 除去最后一个元素的部分。

```haskell
ghci> init [5,4,3,2,1]

[5,4,3,2]
```

**length** 返回一个 List 的长度。

**null** 检查一个 List 是否为空。如果是，则返回 `True`，否则返回 `False`。应当避免使用 `xs==[]` 之类的语句来判断 List 是否为空，使用 null 会更好。

**reverse** 将一个 List 反转

**take** 返回一个 List 的前几个元素

**maximum** 返回一个 List 中最大的那个元素。`minimun` 返回最小的。

**sum** 返回一个 List 中所有元素的和。`product` 返回一个 List 中所有元素的积。

**elem** 判断一个元素是否包含于一个 List，通常以中缀函数的形式调用它。

## range

获得1-20可以使用`[1..20]`

获得135..20可以使用`[1,3..20]`

可以这样生成无限长度`list[1,2..]`或者`cycle[1]`或者`repeat 1`

## filtering

形如`[x*2 | x <- [1..10]]`（提取前十个偶数）

左侧是输出函数，右侧是限制条件

