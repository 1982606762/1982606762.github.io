---
title: vue学习
date: 2021-11-05 20:36:24
tags: vue
categories: 前端
---

<!--more-->

# 11月5日

* v-for支持两个参数，第二个是当前项的索引，从0开始

* V-bind:class后可以在某条件达成后获得某个类名

  ```html
  <li v-for="(item,index) in navList" :class="{active:index === activeNavIndex}"
  ```

  
