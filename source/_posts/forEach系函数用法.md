---
title: forEach系函数用法
date: 2021-08-27 10:42:20
tags:
  js
categories:
  学习笔记
---

# 简述forEach()、map()、every()、some()和filter()的用法

<!--more-->

## 一、forEach()，用于遍历数组，无返回值

这里先给出一个数组（以下例子通用）：



```csharp
var arr = [1,-2,3,4,-5];
```

然后我要做事情的就是，将数组中的每一项翻倍。



```php
arr.forEach(function(item,index,array){
    array[index] = item * 2;
});
console.log(arr);   // [2,-4,6,8,-10]
```

可以看到，forEach()可以传入一个匿名函数作为参数，而该匿名函数有含有三个参数，其依次代表数组遍历时的当前元素item，数组遍历时的当前元素的索引index，以及正在遍历的数组array。有了这三个参数，可以方便我们做很多事情，比如说示例当中将每一项数组元素翻倍，这时需要用到第一个参数item。但是，仅仅只是将item乘以2可不行，我们还得将其赋值给原来的数组，这时我们就得用到后面两个参数index和array。

根据上述可知，array[index]是全等于item的。



```php
arr.forEach(function(item,index,array){
    console.log(array[index] === item);   // true
});
```

## 二、map()，用于遍历数组，返回处理之后的新数组



```jsx
var newArr = arr.map(function(item,index,array){
    return item * 2;
});
console.log(newArr);   // [2,-4,6,8,-10]
```

可以看到，该方法与forEach()的功能类似，只不过map()具有返回值，会返回一个新的数组，这样处理数组后也不会影响到原有数组。

## 三、every()，用于判断数组中的每一项元素是否都满足条件，返回一个布尔值



```jsx
var isEvery = arr.every(function(item,index,array){
    return item > 0;
});
console.log(isEvery);   // false
```

可以看到，示例中是要判断数组arr中的元素是否都为正数，很显然不是，所以该方法最终返回false。

## 四、some()，用于判断数组中的是否存在满足条件的元素，返回一个布尔值



```jsx
var isSome = arr.some(function(item,index,array){
    return item < 0;
});
console.log(isSome);   // true
```

可以看到，该方法与every()类似，示例中是要判断数组arr中是否存在负数元素，很显然存在，所以该方法最终返回true。

## 五、filter()，用于筛选数组中满足条件的元素，返回一个筛选后的新数组



```jsx
var minus = arr.filter(function(item,index,array){
    return item < 0;
});
console.log(minus);   // [-2, -5]
```

可以看到，示例中是要筛选出数组arr中的所有负数，所以该方法最终返回一个筛选后的新数组[-2, -5]。

**补充：** 以上五大方法除了传递一个匿名函数作为参数之外，还可以传第二个参数，该参数用于指定匿名函数内的this指向，例如：



```jsx
// 只传一个匿名函数
arr.forEach(function(item,index,array){
    console.log(this);  // window
});
```



```jsx
// 传两个参数
arr.forEach(function(item,index,array){
    console.log(this);  // [1, -2, 3, 4, -5]
},arr);
```

**兼容性：** 由于以上方法均属ES5方法，所以IE8及其以下浏览器均不兼容。

## 重点总结：

> ① forEach()无返回值，map()和filter()返回新数组，every()和some()返回布尔值
>  ② 匿名函数中this指向默认为window，可通过传第二参数来更改之
>  ③ 五种遍历方法均为ES5方法



