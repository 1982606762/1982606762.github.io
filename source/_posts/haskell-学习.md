---
title: haskell 学习
date: 2022-04-13 22:12:04
tags:
categories: haskell
---

haskell笔记

<!--more-->



# 函数

### 调用

先写函数名后加参数，如`min 1 2`

### 声明

先函数名，后跟空格分隔的参数表，然后加=后定义函数行为

`doubleme x = x+x`

### 常用函数

replicate n m  复制n个m

### 不等于是/=

### if语句

```haskell
doubleme x = if x>100
							then x
							else x*2

```

if里 else部分不能省略

**if语句是一个表达式**，即返回一个值的代码。

## 函数语法

### 模式匹配

模式匹配通过检查数据的特定结构来检查其是否匹配，并按模式从中取得数据。

```haskell
sayMe :: (Integral a) => a -> String  
sayMe 1 = "One!"  
sayMe 2 = "Two!"  
sayMe 3 = "Three!"  
sayMe 4 = "Four!"  
sayMe 5 = "Five!"  
sayMe x = "Not between 1 and 5"

```

若想匹配不需要的东西就需要用括号括起来并且用_表示

递归常使用(x:xs)进行匹配

```haskell
sum' :: (Num a) => [a] -> a  
sum' [] = 0  
sum' (x:xs) = x + sum' xs
```

as模式：

将一个名字和 `@` 置于模式前，可以在按模式分割什么东西时仍保留对其整体的引用。

```haskell
capital :: String -> String  
capital "" = "Empty string, whoops!"  
capital all@(x:xs) = "The first letter of " ++ all ++ " is " ++ [x]
```

### Guards

用来检查一个值的某项属性是否为真

```haskell
bmiTell :: (RealFloat a) => a -> String  
bmiTell bmi  
    | bmi <= 18.5 = "You're underweight, you emo, you!"  
    | bmi <= 25.0 = "You're supposedly normal. Pffft, I bet you're ugly!"  
    | bmi <= 30.0 = "You're fat! Lose some weight, fatty!"  
    | otherwise   = "You're a whale, congratulations!"
```

竖线就是guards，若为真就使用，为假就往下

### Where

写在guards下边

```haskell
bmiTell :: (RealFloat a) => a -> a -> String  
bmiTell weight height  
    | bmi <= skinny = "You're underweight, you emo, you!"  
    | bmi <= normal = "You're supposedly normal. Pffft, I bet you're ugly!"  
    | bmi <= fat    = "You're fat! Lose some weight, fatty!"  
    | otherwise     = "You're a whale, congratulations!"  
    where bmi = weight / height ^ 2  
          skinny = 18.5  
          normal = 25.0  
          fat = 30.0
```



### let

let必须跟一个in，在let里定义的变量可以在in里当成私有变量来使用。

```haskell
cylinder :: (RealFloat a) => a -> a -> a  
cylinder r h = 
    let sideArea = 2 * pi * r * h  
        topArea = pi * r ^2  
    in  sideArea + 2 * topArea
```

let是一个表达式，可以在任何地方使用。

```haskell
ghci> (let (a,b,c) = (1,2,3) in a+b+c) * 100  
600
```

### case

Case 类似switch

```haskell
case expression of pattern -> result  
                   pattern -> result  
                   pattern -> result  
                   ...
```

```haskell
head' :: [a] -> a  
head' xs = case xs of [] -> error "No head for empty lists!"  
                      (x:_) -> x
```



## 常用函数

### zip [a] [b]

返回数组，将a，b组合起来，若长度不同则以短的为准

### replicate a b

返回数组，把b重复a次

### flip f a b

返回f b a的结果

### div a b

返回a/b , 只能用于整数

### zipWith f [a] [b]

返回数组，每一项是a，b中相应项经过f操作后的结果

### map f [a]

返回数组，每一项是a经过f操作后的结果

### filter (a->bool) [a]

返回数组，a数组经过限制条件后剩余元素

### takeWhile (a->bool) [a]

返回符合限制条件的元素数组

### dropWhile (a->bool) [a]

返回去除条件后的数组

### odd

判断是不是基数

### even

判断是不是偶数

### words

把string中的单词拆出来成为数组

### unwords

把单词数组组合成String



## 计算函数

mod 取模

div 除







# 变量

在ghci下使用`let`或在脚本中直接写a=1定义

### List

[_x]匹配只有一个元素时的元素

`let a = [1,2,3,4]` 记得用逗号隔开

字符串就是字符的list

* 合并list：`[1,2,3] ++ [4,5,6]`  `"hello" ++ "world"`

合并时会遍历整个list，长字符串性能差

* 前插元素： `1:[2,3,4,5]`

++操作需要两个操作数都是list，因此需要`[1] ++ [2]`

:操作是将一个字符前插到一个list，因此`[1,2,3]`实质上就是`1:2:3:[]`

* 索引元素：`[1,2,3,4] !! 1`, `[[[],[]],[]] !! 0 !! 1`
* Head 获取第一个元素
* tail 获取除去第一个剩下的
* last 获取最后一个
* init 获取除去最后一个剩下的
* length 获取长度
* null 获取是否为空
* Reverse 反转列表
* take n list 获取前n个元素
  * `take 10 (repeat 5)`
  * `replicate 3 10`

* drop n list 删除前n个元素
* n elem list 判断n是否在list里

### Range

`[1..20]`

`[1,2..20]` 只会按照特定加法步长生成list，不要使用浮点数

可以定义无限长度list，如取前24个3的倍数。`take 24 [3,6..]` 由于Haskell是懒惰的，所以他只会在你取值的时候进行计算。

### 元组Tuple

用小括号定义

与list区别：元组可以存入多种元素，可以包含多种类别的元素 ，但是一个tuple的类型取决于内部数据的数量和类型，如：

```haskell
(1,2)!=(1,2,3)
(1,2) != ('1',2)
```

所以可以用list包裹tuple来表示二维，如[(1,2),(1,3),(1,4)].

`fst (1,2)=1`

`snd (1,2)=2`



zip函数接受两个list，生成一个包含tuple的list。若长短不一则长的那个会断开适配短的。

```haskell
 ghci> zip [1,2,3,4,5] [5,5,5,5,5]

[(1,5),(2,5),(3,5),(4,5),(5,5)]

ghci> zip [1 .. 5] ["one", "two", "three", "four", "five"]

[(1,"one"),(2,"two"),(3,"three"),(4,"four"),(5,"five")]
```



# type and Typeclass

## Type

类型以大写字母开头

可以用`:t`来判断一个东西的类型。

函数的参数之间用->分隔，回传值是最后一项。

常见类型有：

* Int: 整数
* Integer：没有边界的整数
* Float：单精度浮点数
* Double：双精度浮点数
* Bool：只有True和False
* Char：一个字符

## Type variable

函数head的类型是[a]->a

这里的a就是一个类型变量，他可以是任意类型，必须是小写。

## 类型类Typeclass

某个Typeclass定义了这个类型所描述的行为，如果一个类型属于某个类型类那么他就拥有相应的行为。

`(Eq a) => a -> a` 表示a是Eq类型类的类型，这个符号代表typeclass约束。

例如

* show：可以用字符串表示，目前除了函数其他类型都是show的成员。

* Eq：可以做比较

* read: 


# 输入输出

## 输入

putStrLn



# Functor,Applicative Functor,Monoids

## Functor

Functors 是可以被 map over 的对象，这个typeclass只有一个method是fmap

### fmap

fmap :: (a -> b) -> f a -> f b

提供一个函数和一个有盒子的值，输出装着新值的盒子

将输入的方程应用到a上，即 fmap f a = f a

## Applicative Functor

pure a  = a

```haskell
(<*>) :: Applicative f => f (a -> b) -> f a -> f b
```

提供一个在盒子里的函数和一个盒子里的值，输出装着新值的盒子

```haskell
ghci> pure (+) <*> Just 3 <*> Just 5  
Just 8  
ghci> pure (+) <*> Just 3 <*> Nothing  
Nothing  
ghci> pure (+) <*> Nothing <*> Just 5  
Nothing
```

```haskell
(<$>) :: (Functor f) => (a -> b) -> f a -> f b  
f <$> x = fmap f x
pure f <*> x = f <$> x
```

```haskell
ghci> (++) <$> Just "johntra" <*> Just "volta"  
Just "johntravolta"
```

举例：

```haskell
ghci> a = [(*)]<*>[1,2]
ghci> :t a
--a :: Num a => [a -> a]
--a是一个数组，里边每个元素都是一个a->a的函数
ghci> length a
--4
ghci> a<*>[3]
--[3,6,4,5]
a里边是1*,2*,1+,2+
```



# Monads

## bind >>=

```haskell
(>>=) :: Monad m => m a -> (a -> m b) -> m b
```

## Laws:

1. return v>>=f  =>  f v
2. M >>= (\a = a) => M

## pure



## Do statement

```haskell
do
x<-[1,2,3]
y<-[4,5,6]
pure(x*y)
--等价于
[1,2,3]>>=\x->
	[4,5,6]>>=\y->
		pure (x*y)
```

见到左箭头可以认为从右侧取一个值

x<- m a

通过左箭头后x变成a类型









# ghci命令

## :l 装载某个hs文件

`:l aaa.hs`

## :t 查看类型

`:t 'a'`



# quickcheck

查看用当前arbitry生成的样本数据

```haskell
sample' arbitrary :: IO [UpperCaseString]
```

使用erlang的quickCheck需要导入包

```erlang
-include_lib("eqc/include/eqc.hrl").
```

查看eqc生成的样本数据

```erlang
eqc_gen:sample(dict_eqc:dict_5()).
```

# Otp

分离发信息和逻辑部分

## 使用gen_server

cast-> request

Call -> request_reply

handle_cast -> handle_request

## Statefunction mode

-behavior(gen_statem)

需要先明确程序的多个状态

### lamp module implementation

1. module定义，public API定义，callbacks
2. start函数，使用gen_statem的start方法，第一个参数是自身module
3. button函数，使用cast方法，参数是Lamp和button
4. stop函数，使用stop方法
5. callback方法：
6. 定义init，返回一个三元组
7. 定义callback_mode返回state_functions，还可以使用handle_event_functions
8. states方法：
9. Off接受cast,button,Data,返回四元组{next_state,low-UNSTABLE,Data,2000}
10. Low_unstable同样接受三个参数，如果第一个是cast则在触发cast的时候进入，再定义一个第一个是timeout，第二个是_的来等到超时进入。
11. 使用：
12. {ok,L} = Lamp:start()

## supervisor

如果有另一个进程需要执行但是不知道需要执行多久，就spown一个新的，并且用一个supervisor来监督他的执行

理想状况是除了root每个进程都有一个supervisor

### Lamp module supervisior implementation

1. module定义，export start_link, spawn_lamp
2. Export init
3. Behaviour 是supervisor
4. startlink函数，同上start
5. spawnlamp函数，传入一个S，使用supervisior的start_child方法传入两个参数
6. init函数，定义一个Child变量，包含一系列参数的tuple。定义RestartStrategy变量，定义了重启时需要的操作。定义MaxRestart变量和MaxTime变量，返回这些变量。
7. 在lamp.erl文件中新增一个start_link函数，使用的是他自己behavior的方法
8. 使用：
9. {ok,S} = lamp_sup:start_link()
10. {ok,L1} = Spawn_lamp(S)
11. 现在可以使用L1了
12. Exit(S,shutdown)关闭supervisor和他下边的所有进程
