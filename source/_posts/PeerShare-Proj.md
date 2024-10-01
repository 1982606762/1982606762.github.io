---
title: PeerShare-Proj
date: 2024-03-01 11:58:39
tags: 
categories: 前端
---

A note for the PeerShare project.

<!--more-->

## 使用gun

gun是一个图表型数据库，首先需要新建数据库链接：

```js
var db = GUN(['http://localhost:8765/gun', 'https://gun-manhattan.herokuapp.com/gun']);
//var db = GUN(); default node
```

然后链接到一个结点

```js
let expenses = db.get('expensestest');
```

要想保存一个数据到这个结点下：

```js
expenses.set(expense)
```

读取数据：

```js
expenses.map().on(function(data, key){
  console.log("selected_option:"+data.selected_option)
  console.log("input_value:"+data.input_value)
});
```

