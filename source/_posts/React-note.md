---
title: React-note
date: 2024-04-26 14:26:43
tags: React
categories: 前端
---

Learning note for React

代码片段在https://codesandbox.io/dashboard/sandboxes/?workspace=21c09ad6-4546-46a4-8740-fa5a1f9e3798

<!--more-->

## 新建React项目

有index.html,里边要有一个div的id是root

新建index.js并且使用

```js
var React = require("react");
var ReactDOM = require("react-dom");

ReactDOM.render(
  <div>
    <p>Created by {name}</p>
    <p>Copyright {year}</p>
  </div>,
  document.getElementById("root")
);

```

就可以在root元素里渲染一个div元素，render函数第一个输入只能是一个element，所以需要用div包裹。

要想给元素添加class需要使用`className=“”`。

```js
var imglink = "https://picsum.photos/200";
var content = (
  <div>
    <h1 className="qwe">Hello World</h1>
    <img src={imglink} />
    <img src={imglink + "?grayscale"} />
    <ul>
      <li>1</li>
      <li>2</li>
      <li>3</li>
    </ul>
  </div>
);
```

要想添加inline-styling需要使用`style={{color:"red"}}`

还可以使用：

```js
const customStyle = {
  color:"red",
  fontSize:"20px"
}
style={customStyle}
```

### 使用app.jsx规范代码格式

一般来讲新建一个app.jsx文件来管理内容，而index.js里只引用app的函数。

```js
//app.jsx
import React from "react";

function app() {
  return <div>hello</div>;
}
export default app;
```

```js
//index.js
var React = require("react");
var ReactDOM = require("react-dom");

import app from "./App.jsx";

ReactDOM.render(app(), document.getElementById("root"));

```

使用react dev tool 可以查看当前网页树状图

## React module



单文件使用component:
```js
function Heading(){
  return <h1>Heading</h1>
}
<div>
  <Heading></Heading>
</div>
```

注意component文件名和方程名必须用大写字母开头.

如果在另一个文件中定义module，另一个文件需定义成.jsx文件

```js
import React from "react"

function Heading(){
  return <h1>Heading</h1>
}
export default Heading

//import Heading from "./Heading" in the index.js
```

一般来讲在index中只有一个app组件，然后新建一个叫app的文件来包含所有其他东西

## ES6相关

### JSX

JSX可以让用户在JS代码里添加HTML代码。

### export

如果只export一个东西就使用`export default x`, 但是如果想要暴露多个变量或函数就需要用大括号包起来，例如`export {x1,x2,x3}` . 一个文件只能使用一次default,但是可以用很多次大括号export

在imoprt的时候如果使用`import x from "./a.js"`就是引入默认的输出

如果使用`import * as x from './a.js'`就是引入所有东西，之后可以使用a.a1来使用

### Map/filter/reduce

Map可以通过loop一个数组的全部元素来获得一个新数组

Filter可以使用某种条件来过滤数组里所有内容

Reduce可以累计数组元素并且返回一个值

find可以找到数组里第一个符合条件的内容

findindex可以找到第一个index

es6里用法：

```js
var numbers = [3, 56, 2, 48, 5];

//Map -Create a new array by doing something with each item in an array.
var newNumbers = numbers.map(function (x) {
  return x + 1;
});
console.log(newNumbers);
//Filter - Create a new array by keeping the items that return true.
var numberfilter = numbers.filter(function (x) {
  return x > 6;
});
console.log(numberfilter);
//Reduce - Accumulate a value by doing something to each item in an array.
var numberreduce = numbers.reduce(function (accu, curr) {
  return accu + curr;
});
console.log(numberreduce);
//Find - find the first item that matches from an array.
var num1 = numbers.find(function (num) {
  return num > 10;
});
console.log(num1);
//FindIndex - find the index of the first item that matches.
var index = numbers.findIndex(function (num) {
  return num > 10;
});
console.log(index);

```

### Arrow function

箭头函数用于需要用匿名函数的地方，可以用来省略function定义名

```js
var numbers = [3, 56, 2, 48, 5];

//Map -Create a new array by doing something with each item in an array.
var newNumbers = numbers.map((x) => {
  return x + 1;
});


var newNumbers = numbers.map((x) => x + 1);
var newNumbers = numbers.map(x => x + 1);


```









## React Prop

可以把一段重复的HTML封装到一个函数里，然后通过传参的方式来复用，只是这里传参是从properties的位置传参。

```js
//index.js
function Card(props) {
  return (
    <div>
      <h2>{props.name}</h2>
      <img src={props.img} alt="avatar_img" />
      <p>{props.tel}</p>
      <p>{props.email}</p>
    </div>
  );
}
ReactDOM.render(
  <div>
    <h1>My Contacts</h1>
    <Card
      name="Beyonce"
      img="https://blackhistorywall.files.wordpress.com/2010/02/picture-device-independent-bitmap-119.jpg"
      tel="+123 456 789"
      email="b@beyonce.com"
    />
    <Card
      name="Jack Bauer"
      img="https://pbs.twimg.com/profile_images/625247595825246208/X3XLea04_400x400.jpg"
      tel="+7387384587"
      email="jack@nowhere.com"
    />
  </div>,
  document.getElementById("root")
);
```

## React map

假如x是一个数组，在React <div>里使用x.map(func) 可以实现遍历x数组里每一个元素i，将i传入func中执行然后获得返回值。

这里map返回的元素需要有一个prop叫做key，它不能直接被访问到并且他的值需要是唯一的。

正确用法是复用刚刚新建的封装好的函数中，例如：

```js
function Entry(content) {
  return (
    <div className="term">
      <dt>
        <span className="emoji" role="img" aria-label="Tense Biceps">
          {content.emoji}
        </span>
        <span>{content.name}</span>
      </dt>
      <dd>{content.meaning}</dd>
    </div>
  );
}
function createEntry(content) {
  return (
    <Entry
      key={content.id}
      emoji={content.emoji}
      name={content.name}
      meaning={content.meaning}
    />
  );
}
```

## React conditional rendering

可以根据变量值的不同来渲染不一样的组件

利用三元运算符实现

```js
function App(){
  return <div>
		{var1 ? <h1>Hello</h1> : <h1>World</h1>}
    </div>
}
```

也可以用null表示什么都不渲染

如果使用React的and运算符&&可以实现相同的效果，只有左边是true的时候才会运行运算符右边的代码

## React State

用户界面会根据变量值的变化而变化。

如

```js
var isDone = false;
return <p style={isDone? style1:null}> Buy milk </p>
```

但是如果动态修改变量的值渲染不会跟着改变，需要使用hooks。使用useState来保存和更新需要变化的变量。usestate返回两个内容，第一个是变量，第二个是setstate函数来设置变量值。

```js
function App() {
  const [count, setCount] = useState(0);

  function increase() {
    setCount(count + 1);
  }

  function decrease() {
    setCount(count - 1);
  }

  return (
    <div className="container">
      <h1>{count}</h1>
      <button onClick={decrease}>-</button>
      <button onClick={increase}>+</button>
    </div>
  );
}
```

[简单应用](https://codesandbox.io/p/sandbox/usestate-hook-practice-forked-trrlvh?file=%2Fsrc%2Findex.js)

### 复杂State

State也可以作为一个object存在，只需要在useState里加就行

```js
const [fullName, setFullName] = useState({
    fName: "",
    lName: ""
  });
```

在修改的时候需要注意，直接修改会抹去之前的状态，所以需要保存之前状态同时添加新状态

```js
function handleChange(event) {
    const { name, value } = event.target;

    setFullName(prevValue => {
      if (name === "fName") {
        return {
          fName: value,
          lName: prevValue.lName
        };
      } else if (name === "lName") {
        return {
          fName: prevValue.fName,
          lname: value
        };
      }
    });
  }

```

或者使用Spread operator来实现：

```js
function handleChange(event) {
    const { name, value } = event.target;

    setFullName(prevValue => {
      return{
        ...prevValue,
        [name]: value
      }
      
    });
  }

```



## React handle Event 事件管理

mouseover，mouseout之类：

```js
function App() {
  const [headingText, setHeadingText] = useState("Hello");
  const [isMousedOver, setMouseOver] = useState(false);

  function handleClick() {
    setHeadingText("Submitted");
  }

  function handleMouseOver() {
    setMouseOver(true);
  }

  function handleMouseOut() {
    setMouseOver(false);
  }

  return (
    <div className="container">
      <h1>{headingText}</h1>
      <input type="text" placeholder="What's your name?" />
      <button
        style={{ backgroundColor: isMousedOver ? "black" : "white" }}
        onClick={handleClick}
        onMouseOver={handleMouseOver}
        onMouseOut={handleMouseOut}
      >
        Submit
      </button>
    </div>
  );
}
```

处理表单相关event：

使用onChange 来处理输入event。

