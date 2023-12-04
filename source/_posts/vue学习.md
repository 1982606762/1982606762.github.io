---
title: vue学习
date: 2021-11-05 20:36:24
tags: vue
categories: 前端
---

<!--more-->

# vue app内容

## data

可以return多个内容，代表app要使用的所有数据

```js
data(){
  return {
    list : [
      {
        name: '张三',
        age: 18
      },
      {
        name: '李四',
        age: 20
      },
      {
        name: '王五',
        age: 22
      }
    ],
    name:'',
    num:''
  }
},
```

## mounted

在网页加载完成后自动执行内容

```js
mounted() {
  setInterval(() => {
    this.num = Math.random() * 100
  }, 1000)
}
```

## methods

app要使用的所有函数

```js
methods: {
  handleClick() {
    this.list.push({
      name: this.name,
      age: this.num
    })
    this.name = ''
    this.num = ''
  }
},
```

### 事件

函数默认第一个参数是event，若有参数就可以使用$event作为实参传入

绑定多个事件可以用逗号隔开，并且加上函数的引用括号

阻止事件冒泡，事件修饰符：

* 可以在内层btn上使用@click.stop
* 可以在外层使用@click.self判断是不是点的自己 
* 在外层加.capture让他捕获冒泡
* 在外层加.once让他

按键修饰符：@keydown

Enter,tab,delete,esc,up,down,left,right

鼠标修饰符：@click

Left,right,middle

精确修饰符：@click.ctrl.exact只有点击ctrl才可以

```js
<input @keydown.delete = "handleKeyDown"
```





## template

在app绑定的节点内添加里边的内容

```js
template: `
            <div>
                <input v-model="name">
                <input v-model="num">
                <button v-on:click = "handleClick">添加</button>
                <ul>
                    <li v-for="(item,index) in list">
                        {{item.name}}
                        {{item.age}}
                        {{index}}
                    </li>
                </ul>
            </div>
        `,
}).mount('#root');
```

## component

组件，可以表示任何可见元素

定义：

```js
app.component('my-component', {
  props: ['content',"index"],
  template: `
        <li>
            {{content.name}}
            {{content.age}}
            {{index}}
        </li>
        `
});
```

使用：

```js
<ul>
   <my-component 
v-for="(item,index) in list" 
v-bind:content="item" 
v-bind:index = "index"
/>
</ul>
```

## 计算属性

computed

当计算属性依赖的内容发生变更时才重新执行计算

```js
computed: {
  total() {
    return Date.now()
  }
}
```

## 监听器

```js
//price发生变化时执行
watch: {
  price(current,prev){
    setTimeout(() => {
      this.message = prev + "changed to" + current
    },1000)
  }
},
```

## 样式

在style里定义类，然后给标签绑定类

```js
data(){
  return{
    class:'red',
    classObj:{red:true,green:true},
    classArray:['red','green',{brown:true}]
  }
},
  template: `<div :class="classObj">Hello World</div>`

```

对于组价有两种方法来改变class

```js
//1.每个组价标签都加class
//2.父组件加class，子组件使用:class="$attrs.class"继承父组件的class
```







# vue基本操作

## v-for

支持两个参数，第二个是当前项的索引，从0开始

## V-bind

用于给某个标签绑定属性，如title，class等

简写为:

v-bind:class后可以在某条件达成后获得某个类名

```html
<li v-for="(item,index) in navList" :class="{active:index === activeNavIndex}"
```

## v-on

绑定点击事件`v-on:click = "handleclick"`

简写为@click

## v-model

双向绑定数据和输入框,把输入框变成单标签。

```js
{{message}}
<input v-model="message"/>
```

### 标签

可以使用：input(text,checkbox,video),textarea,select

使用checkbox的时候message可以是一个数组[]，然后input添加value就可以显示当前点的什么

也可以自定义选中和没选中的时候的显示：

```js
message:"world"
<input type="checkbox" v-model="message" true-value="hello" false-value="world"/>
  
```



使用video的时候message是字符串‘’

使用select的时候message是字符串，最好给一个初始值，其中内部的option可以用object来批量初始化：

```js
options:[{
  text:'A',value:'A'
},{
  text:'B',value:'B'
},{
  text:'C',value:'C'
}]


<select v-model="message">
  <option v-for="item in options" :value="item.value">{{item.text}}</option>
</select>
```



### 修饰符

v-model.lazy可以让他变得变慢

V-model.number让输入的值存储成number类型

V-model.trim去除后边的空格



## V-once

让语句里的变量不会在改变的时候进行渲染

内容会变，但是页面上显示的不变

## v-if

根据变量判断是否展示标签

```js
data(){
            return{
                show: false,
                condotion:true

            }
        },
        template: `
        <div :class='classs'>Hello World</div>
        <div v-if="show">if</div>
        <div v-else-if="condotion">elseif</div>
        <div v-else>else</div>
        `
        
```

使用template来做占位符，仅做到for循环的效果并且不添加div

```js
<div>
            <template v-for="(value,key,index) in listItem" :key="index">
                <div v-if="key !== 'second'">
                    {{key}}---{{value}}
                </div>
            </template>    
        </div>
```



## v-show

根据变量判断是否加display:none



# mvvm

> let app = Vue.**createApp**({
>
> ​    });
>
> 创造vue app
>
> let vm = app.mount('#root')
>
> vue应用的根组件

# 生命周期函数

某一时刻被自动执行的函数

![The Vue Instance Lifecycle](https://img.zhaoxuanlang.cn/lifecycle.png)

# 组件

可以复用，每个组件内的data是独立的

全局组件定义后全局可以使用，但是性能不高

局部组件注册才能用

```js
const counter = {
  data(){
    return {
      count:1
    }
  },
  template: `<div @click="count += 1">{{count}}</div>`
}
```

在app里添加components:{'count':counter}，或者{counter}简写

## 传值

在调用的时候传递`<test content="123" />`

或者使用v-bind:content="num"并且在data里定义num

在组件里添加`props:['content']`

## 参数类型校验

在组件里使用

```js
props:{
  content: string
}
```

就是需要传入一个string

可以使用string,boolean,array,object,function

高级用法：可以把content定义为一个object，里边可以包含default函数，validator函数，required元素等。

## 单向数据流

父组件能向子组件传值，但是子组件不能修改

方法：

```js
props:['count']
data(){
  return{
    mycount: this.count
  }
}
```

## non-prop属性

子组件不定义prop的时候父组件传过来的值就会变成一个属性，如msg="hello"

用处：可以快速定义style

可以在子组件加inheritAttrs: false来不接收

子组件有做个的时候可以在想添加的那个组件上添加v-bind="$attrs"来获得属性

## 父子组件间使用方法通信

子组件使用this.$emit('add,1')

父组件监听@add = handle

handle函数有一个参数，获得1

```js
let app = Vue.createApp({
        data(){
            return{
                count:1
            }
        },
        methods:{
            handleadd(para){
                this.count += para
            }
        },
        template:`
        <div>
            <test @add="handleadd" :content="count"/>
        </div>`
        
    });
    app.component('test',{
        props:['content'],
        methods:{
            handleClick(){
                this.$emit('add',2)
            }
        },
        template:`<div @click="handleClick">{{content}}</div>`
    })
```

使用emits是一个数组可以在数组里写所有父组件需要监听的函数名

emits如果里边加一个函数的话可以在传参的时候校验参数

高级用法：使用v-model双向绑定

```js
let app = Vue.createApp({
        data(){
            return{
                count:1
            }
        },
        template:`

            <test v-model="count"/>`
        
    });
    app.component('test',{
        props:['modelValue'],
        methods:{
            handleClick(){
                this.$emit('update:modelValue',this.modelValue+3)
            }
        },
        template:`<div @click="handleClick">{{modelValue}}</div>`
    })
```

## 动态组件

使用component标签实现动态切换

## 同步组件，异步组件

同步组件可以直接加载，异步组件会等一会加载

# 插槽

使用子组件的时候想传入一个dom元素可以使用slot

```js
let app = Vue.createApp({
        template:`
            <test>
                <div>提交</div>    
            </test>
            <test>
                <button>提交</button>
            </test>
            `
        
    });
    app.component('test',{
        methods:{
            handleClick(){
                alert(123)
            }
        },
        template:`
        <div>
            <input /> 
            <span @click="handleClick">  
            <slot></slot>
            </span>
        </div>`
    })
```

可以传入另一个子组件

可以设定默认值

## 具名插槽

把插槽分开，每个片段用template包裹，template上加上v-slot:"name"或者#name

子组件内部使用的时候slot加name=“”属性

## 作用域插槽

子组件渲染的内容由父组件决定的时候使用。父组件可以调用子组件的数据

```js
let app = Vue.createApp({
        template:`
            <list v-slot="{item}">
                <div>{{item}}</div>
            </list>
            `
        
    });
    app.component('list',{
        data(){
            return{
                list:[1,2,3]
            }
        },
        template:`
        <div>
            <slot v-for="item in list" :item="item"/>
        </div>`
    })
```

# Vue 动画效果

## 实现基础过渡和动画

### 动画

```js
<style>
        @keyframes leftToright {
            0%{
                transform: translateX(-100px);
            }
            50%{
                transform: translateX(-50px);
            }
            100%{
                transform: translateX(0px);
            }
        }

        .animation{
            animation: leftToright 3s;
        }
    </style>
let app = Vue.createApp({
        data(){
            return {
                animate:{
                    animation:false
                }
            }
        },
        methods:{
            handleClick(){
                this.animate.animation = !this.animate.animation
            }
        },
        template:`
        <div>    
        <div :class="animate">hello world</div>
        <button @click="handleClick">切换</button>
        </div>
        `
        
    });
```

### 过渡

```js

.transition{
            transition: 3s background-color ease;
        }

        .green{
            background: green;
        }

        .blue{
            background: blue;
        }
let app = Vue.createApp({
        data(){
            return {
                animate:{
                    transition:true,
                    blue:true,
                    green:false
                }
            }
        },
        methods:{
            handleClick(){
                this.animate.blue = !this.animate.blue
                this.animate.green = !this.animate.green

            }
        },
        template:`
        <div>    
        <div :class="animate">hello world</div>
        <button @click="handleClick">切换</button>
        </div>
        `
        
    });
```

## 实现单元素组件动画

### 使用transition标签

css：

```css
.v-enter-from{
  opacity: 0;
}
.v-enter-to{
  opacity: 1;
}
.v-enter-active{
  transition: 2s opacity;
}

.v-leave-from{
  opacity: 1;
}
.v-leave-to{
  opacity: 0;
}
.v-leave-active{
  transition: 2s opacity;
}
```

js:

```js
let app = Vue.createApp({
  data(){
    return {
      show:false
    }
  },
  methods:{
    handleClick(){
      this.show = !this.show
    }
  },
  template:`
        <div>    
            <transition>
            <div v-if="show">hello world</div>
            </transition>
        <button @click="handleClick">切换</button>
        </div>
        `
});
```

动画效果实现也一样，只是v-enter-active里opacity改成动画keyframe名称即可。

在transition添加name=‘aaa'后 v-enter-active就需要改成aaa-enter-active，v只是默认名称。

### 自定义类名

可以在`transition`标签上添加`enter-active-class=""  leave-active-class=""`

里边填入类名，如：

```css
.bye{
  animation:shake 3s
}
.hello{
  animation:shake 3s
}
```

## 列表的动画效果

```js
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <script src="https://unpkg.com/vue@next"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .v-enter-from{
            opacity: 0;
            transform: translateY(30px);
        }
        .v-enter-to{
            opacity: 1;
            transform: translateY(0);
            /* 从下往上的动画效果 */
        }
        .v-enter-active{
            transition: all .5s ease-in;
        }

        .v-move{
            /* 其他元素移动时的移动效果 */
            transition: all .5s ease-in;
        }
        
        .list-item{
            display: inline-block;
            margin-right: 10px;
        }
        .v-leave-from{
            opacity: 1;
            transform: translateY(0);
        }
        .v-leave-to{
            opacity: 0;
            transform: translateY(30px);
        }
        .v-leave-active{
            transition:all .5s ease-out;
        }
    </style>
</head>

<body>
    <div id="root"></div>
</body>
<script>
    let app = Vue.createApp({
        data(){
            return {
                list:[1,2,3],
            }
        },
        methods:{
            handleClick(){
                this.list.unshift(Math.floor(Math.random()*100));
            },
            handleremove(i){
                this.list.splice(i,1)
            }
        },
        template:`
        <div>    
            <transition-group>
                <span name="list" class="list-item" v-for="(item,index) in list" :key="item" @click="handleremove(index)">{{item}}</span>
            </transition-group>
        <button @click="handleClick">增加</button>
        </div>
        `
        
    });

    let vm = app.mount('#root')
</script>

</html>
```

## 状态动画

让某些数据有缓慢变化的过程，应用如svg

```js
let app = Vue.createApp({
        data(){
            return {
                number:1,
                animatenumber:1
            }
        },
        methods:{
            handleClick(){
                this.number = 10;
                let currentNumber = this.animatenumber;
                if(this.animatenumber < this.number){
                    let timer = setInterval(()=>{
                    currentNumber++;
                    this.animatenumber = currentNumber;
                    if(currentNumber>=this.number){
                        clearInterval(timer);
                    }
                },100)
                }
                
            },
            
        },
        template:`
        <div>    
        <div>{{animatenumber}}</div>
        <button @click="handleClick">增加</button>
        </div>
        `
        
```

# 高级语法

## mixin

* 组件data优先级高于mixin优先级

```js
//mixin 混入
    const mixin = {
        data() {
            return {
                number:2
            }
        }
    }
```

* 不能用于子组件，需要使用全局mixin(不推荐使用)

```js
app.mixin({
        data(){
            return {
                number:2,
                count:222
            }
        },
        created(){
            console.log(this.count);
        }
    })
```

