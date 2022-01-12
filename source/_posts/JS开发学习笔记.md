---
title: JS开发学习笔记
date: 2021-08-11 21:47:37
tags:
  js
categories:
  学习笔记
---



## margin参数数量

> margin: 20px;（上、下、左、右各20px。）
>
> margin: 20px 40px;（上、下20px；左、右40px。）
>
> margin: 20px 40px 60px;（上20px；左、右40px；下60px。）
>
> margin: 20px 40px 60px 80px;（上20px；右40px；下60px；左80px。）

## 单独设置角度

`border-bottom-left-radius:2px`

<!--more-->

## 设置单元格内文字不溢出还有padding

> .right_menu_inner .module_unit{
> 	width: 40%;
> 	left: 60%;
> 	border: 1px solid #ccc;
>
> position: absolute;
>
> ​    padding: 6px 12px;
>
> ​    font-size: 14px;
>
> ​    line-height: 1.42857143;
>
> ​    height: 100%;
>
> ​    border-radius: 5px;
>
> ​    background-color: white;
>
> ​    overflow: scroll;
>
> ​    border-top-left-radius: 0;
>
> ​    border-bottom-left-radius: 0;
>
> }
>
> .right_menu_inner .module_unit::-webkit-scrollbar{
>
> ​    display: none;
>
> }

效果：![E7FA839551193991515F3BE73B5A0C73](/Users/zxl/Library/Containers/com.tencent.qq/Data/Library/Caches/Images/E7FA839551193991515F3BE73B5A0C73.jpg)   

## 添加输入框后自动编辑

*div*.contentEditable=true

div.focus()

## css定义变量

`:root{
		--bianliangming:xxxxx;
}`

需要前边两个横线

使用：

`div{
color:div(--bianliangming,morenzhi)`
`}`

## 使用vh进行响应式开发

vh就是viewed Height,同理还有vw就是width，他是相对目前打开的页面大小进行更改

> 使用方法：
> 1vh就是1%

## 使用calc进行css计算

> 表达式中有“+”和“-”时，其前后必须要有空格，如"widht: calc(12%+5em)"这种没有空格的写法是错误的；

> 表达式中有“*”和“/”时，其前后可以没有空格，但建议留有空格。  

> 如height:(100vh - 20px);

## 下方浮动的div实现

只需

```css
position:fixed
buttom:0px
```

就可以



## array 操作

* Array.replace(a,b)

  > 把a用b替换，a可以使用正则表达式匹配多个内容
  >
  > 例如：
  >
  > ```js
  > array.replace(/\t/g,' ')
  > ```
  >
  > 选择所有的tab换成空格
  >
  > 再如：
  >
  > ```js
  > array.replace(/# |\n/g,'')
  > ```
  >
  > 选择形如# 和\n消除

* Array.split(a,b)

  > 接收两个传入参数，第一个是用什么把array分离开，第二个是可选项 分离的最大项数
  >
  > 例如:	
  >
  > ```js
  > <script type="text/javascript">
  > 
  > var str="How are you doing today?"
  > 
  > document.write(str.split(" ") + "<br />")
  > document.write(str.split("") + "<br />")
  > document.write(str.split(" ",3))
  > 
  > </script>
  > ```
  >
  > 输出
  >
  > ![image-20210221202626935](/Users/zxl/Library/Application Support/typora-user-images/image-20210221202626935.png)

* Array.join(a)

> 返回一个字符串。该字符串是通过把 arrayObject 的每个元素转换为字符串，然后把这些字符串连接起来，在两个元素之间插入 *separator* 字符串而生成的。

```html
<script type="text/javascript">

var arr = new Array(3)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"

document.write(arr.join())

</script>
```

![image-20210221202904663](/Users/zxl/Library/Application Support/typora-user-images/image-20210221202904663.png)

* Array.slice(start,end)

  > ### 返回值
  >
  > 返回一个新的数组，包含从 start 到 end （不包括该元素）的 arrayObject 中的元素。
  >
  > ### 说明
  >
  > 请注意，该方法并不会修改数组，而是返回一个子数组。如果想删除数组中的一段元素，应该使用方法 Array.splice()。
  >
  > **注释：**您可使用负值从数组的尾部选取元素。
  >
  > **注释：**如果 end 未被规定，那么 slice() 方法会选取从 start 到数组结尾的所有元素。

```html
<script type="text/javascript">

var arr = new Array(3)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"

document.write(arr + "<br />")
document.write(arr.slice(1) + "<br />")
document.write(arr)

</script>
```

输出：

```
George,John,Thomas
John,Thomas
George,John,Thomas
```

* array.trim()

  > 去除头尾的空格

```js
var str = "       Runoob        ";
alert(str.trim());
```

* Array.map()

  > 映射
  >
  > 类似于foreach
  >
  > var data = [1, 2, 3, 4];
  >
  > var arrayOfSquares = data.map(function (item) {
  >
  > 　　return item * item;
  >
  > });
  >
  > alert(arrayOfSquares); // [1, 4, 9, 16]
  >
  > 如果没有return就会把所有内容都映射成undefined

综合题：

![](https://img-blog.csdnimg.cn/2020092411313370.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTExMTM4NA==,size_16,color_FFFFFF,t_70#pic_center)



```js
var fs = require('fs');fs.readFile('./data.text', function(err, data) {    if(err) throw err;    var array = data.toString().split("\n");var arr = []var temp =[]for(i in array) {    arr[i]=array[i].split(',');    temp[i] = arr[i]    arr[i] = temp[i].join().trim().replace(/\s+/ig," ").split(" ")}console.log('arr',arr);});
```

## 给console.log加颜色

使用npm下载colors

用法：colors.xxx.xxx(text)

支持：

> https://www.npmjs.com/package/colors



## 获得文件扩展名

```js
var path = require('path')path.extname('index.html')// returns'.html'
```



## 获得文件名



```js
f.replace(/\.[^/.]+$/, "")
```



## nodejs控制台输入流



```js
const readline = require('readline').createInterface({ input: process.stdin, output: process.stdout});readline.question('Who are you?', name => { console.log(`Hey there ${name}!`); readline.close();});
```



用JQ实现左右侧的滑动标签

利用jq的animate实现

```html
<a href="#" id="right_hide">                    <span class="glyphicon glyphicon-forward"></span> </a>                <div id="right_show" class="right_show">显示新建栏<a href="#"><span class="glyphicon glyphicon-backward"></span> </a></div>
```

```javascript
$(function () {                $("#right_hide").click(function () {                    $("#right1").animate({ right: '-288px' });                    $("#right_show").delay(500).animate({ right: '0' });                    if ($("#left1").css("left") != "0px") {                        $(".canvasall").css("width", "calc(100% - 60px)");                        $(".top_select_bar").css("width", "calc(100% - 60px)");                    } else {                        $(".canvasall").css("width", "calc(80% - 30px)");                        $(".top_select_bar").css("width", "calc(80% - 30px)");                    }                });                $("#right_show").click(function () {                    $("#right_show").animate({ right: '-30px' });                    $("#right1").delay(500).animate({ right: '0' });                    if ($("#left1").css("left") != "0px") {                        $(".canvasall").css("width", "calc(100% - 318px)");                        $(".top_select_bar").css("width", "calc(100% - 318px)");                    } else {                        $(".canvasall").css("width", "calc(80% - 288px)");                        $(".top_select_bar").css("width", "calc(80% - 288px)");                    }                });});
```

原理就是下边遮盖一层，点击后让上边这层向左/右滑走，下边那层滑入即可。

## 实现可拖动div

首先在需要缩放的div旁边实现一个小div

## js深拷贝复制element

`var newnode = oldnode.clone(true)`

true参数表示克隆节点所有后代

## html实现滑块

用h5自带的input就可以实现

` <input type="range" min="10" max="300" value="100" step="10" οnchange="showValue(this.value)" style="">`

然后只需要写个showValue函数就可以修改值



## 设置某个div滚动条位置

```先给div设置一个id然后使用document.getElementbyid.scroll(x,y)调整```

> 其中xy可以用ll.scrollWidth/ll.scrollHeight获得最大值

## 哈希表/map用法

> 1，js创建map对象
>
> var map = new Map();
>
> 
>
> 2.将键值对放入map对象
>
> map.set("key",value)
>
> map.set("key1",value1)
>
> map.set("key2",value2)
>
> 
>
> 3.根据key获取map值
>
> map.get(key)
>
> 
>
> 4.删除map指定对象
>
> delete map[key]
>
> 或
>
> map.delete(key)
>
> 
>
> 5.循环遍历map
>
> map.
>
> forEach(function(key){
> 　　console.log("key",key) //输出的是map中的value值
>
> })

## js取整

> 只保留整数
> parseInt(1.111)

## css渐变过渡动画

>transition: property duration timing-function delay 

transition属性是个复合属性，包括以下几个子属性：

- transition-property ：规定设置过渡效果的css属性名称
- transition-duration ：规定完成过渡效果需要多少秒或毫秒
- transition-timing-function ：指定过渡函数，规定速度效果的速度曲线
- transition-delay ：指定开始出现的延迟时间

默认值分别为：all 0 ease 0 

```
div {  width: 100px;  height: 100px;  background-color: orange;  margin: 20px auto;  border-radius: 100%;  -webkit-transition-property: -webkit-border-radius;  transition-property: border-radius;  -webkit-transition-duration: 3s;  transition-duration: 3s;  -webkit-transition-timing-function：ease; transition-timing-function：ease; div:hover {  border-radius: 0px;}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

