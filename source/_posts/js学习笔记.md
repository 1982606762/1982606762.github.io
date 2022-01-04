---
title: JS学习笔记
tags: []
id: '385'
categories:
  - - 学习笔记
date: 2020-07-30 00:07:16
---

## 2020/07/29

6.1对象性质

*   数据属性直接定义，有四个属性
*   访问器只能用函数定义，有set和get，通常用来改一个值就改所有值
*   获取属性使用`var qq = object.getownpropertydescriptor(name,"数据名")`

6.2创建对象

*   构造函数模式，直接写构造函数之后new即可
*   原型模式，使用prototype关键字，初始化定义好属性，使用时修改则会吧原型的同名属性屏蔽，可以用delete删除某一属性

```
//当前使用最广泛
function personq(name,age,job)
{
    this.age = age;
    this.name = name;
    this.job = job;
}

personq.prototype = 
{
    constructor:personq,
    sayname:function(){
        alert(this.name);
    }
}
```

6.3原型链

![](http://www.zhaoxuanlang.cn/wp-content/uploads/2020/07/image-745x1024.png)

![](http://www.zhaoxuanlang.cn/wp-content/uploads/2020/07/image-1-1024x526.png)

继承：

*   组合式继承
*   寄生组合式继承（效果最好）

```

function inheritPrototype(subType,superType){
    var prototype = Object(superType,prototype);
    prototype.constructor = subType;
    subType.prototype = prototype;
}

function Supertype(name)
{
    this.name = name;
}

Supertype.prototype.sayname = function()
{
    alert(this.name)
}

function Subtype(name,age){
    //继承属性
    Supertype.call(this,name);
    this.age = age;
}

//继承方法
Subtype.prototype = new Supertype();
//寄生组合式继承
//inheritPrototype(Subtype,Supertype);


Subtype.prototype.sayage = function(){
    alert(this.age);
}
```

## 2020/07/30

函数表达式可以不对函数命名，即匿名函数

在函数内部定义其他函数是闭包，用处两个

*   创建并立刻调用函数
*   实现私有变量

BOM

window对象：

*   top指向最外围的框架，parent指向上一级
*   window可以指定窗口大小和位置
*   导航和打开窗口

location对象：

*   通过编程访问浏览器导航，逐段修改浏览器url
*   使用replace（）方法可以不能返回

navigator对象：

*   检测插件
*   与浏览器有关