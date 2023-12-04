---
title: 使用meta实现定时跳转链接
date: 2022-05-29 18:56:39
tags:
categories:	前端
---

利用了meta标签的一个功能。

<!--more-->

HTML：

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="5; url=http://www.baidu.com">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    
</head>

<body>
    <h1>页面将在 <span id="time">5</span> 秒后重定向</h1>
    <script src="111.js"></script>
    <form>
        <fieldset>
          <legend>health information</legend>
          height: <input type="text" />
          weight: <input type="text" />
        </fieldset>
      </form>
</body>

</html>
```

js:

```js
let num = document.getElementById('time');
let t = 5
function changeTIme() {
    if (t > 0) {
        t--;
        num.innerHTML = t;
    } else {
        alert('Time out');
        clearInterval(timer);
    }
}
let timer = setInterval(changeTIme, 1000);

```

