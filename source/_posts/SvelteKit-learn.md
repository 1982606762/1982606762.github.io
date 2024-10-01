---
title: SvelteKit-learn
date: 2024-01-20 00:01:17
tags: sveltekit
categories: 前端
---

Personal SvelteKit learning note

Including Svelte and SvelteKit

<!--more-->

# Basic Svelte

## Introduction

Svelte 可以用来制作小的JS模块，并且通过组合这些组件来构建应用。

组件是可重复使用的代码块，包含HTML，CSS和JS并且一个组件就是一个.svelte文件。

### 简单的添加数据并使用：

```js
<script>
	let src = '/image.gif';
	let name = 'Rick Astley';
</script>

<img {src} alt="{name} dances." />

```

### 添加样式：

```js
<p>This is a paragraph.</p>

<style>
	p {
		color: goldenrod;
		font-family: 'Comic Sans MS', cursive;
		font-size: 2em;
	}
</style>

```

前后顺序并不影响。

### 引用另一个组件的内容：

```js
<script>
	import Nested from "./Nested.svelte"
</script>
<Nested/>
<p>This is a paragraph.</p>

<style>
	p {
		color: goldenrod;
		font-family: 'Comic Sans MS', cursive;
		font-size: 2em;
	}
</style>
```

引用的组件并不会套用当前组件的css，组件名需要首字母大写。

### string里插入html片段

```html
<script>
	let string = `this string contains some <strong>HTML!!!</strong>`;
</script>

<p>{@html string}</p>
```

在使用string变量名的时候添加{@html xxx}即可

### button点击事件

```html
<script>
	let count = 0;

	function increment() {
		count += 1;
	}
</script>

<button on:click={increment}>
	Clicked {count}
	{count === 1 ? 'time' : 'times'}
</button>

```

首先用button标签新建一个按钮，在on监听click事件并绑定给一个函数。

### 可变变量

```html
<script>
	let count = 0;
	$: doubled = count * 2;

	function increment() {
		count += 1;
	}
</script>

<button on:click={increment}>
	Clicked {count}
	{count === 1 ? 'time' : 'times'}
</button>

<p>{count} doubled is {doubled}</p>

```

加这个修饰符可以让他实时计算变量值并更新。这个修饰符里也可以包裹很多其他东西比如if语句，就会实时判断。这个里边的更新只会在这个变量被更改或赋值的时候执行，但是数组操作并不是赋值所以不会触发，所以需要赋值给他自己。

## Props

### components之间传值

首先在需要接收输入的组件里把变量设置为`export let x`

然后在另一个组件里用`<Nested x={42} />`.

也可以在定义变量的时候设置默认值。

## Logic

### If/Else

```js
<script>
	let count = 0;

	function increment() {
		count += 1;
	}
</script>

<button on:click={increment}>
	Clicked {count}
	{count === 1 ? 'time' : 'times'}
</button>

{#if count > 10}
	<p>{count} is greater than 10</p>
{:else}
	<p>{count}</p>
{/if}
```

### Each

可以遍历数组并且循环添加元素

```svelte
<script>
	const colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'];
	let selected = colors[0];
</script>

<h1 style="color: {selected}">Pick a colour</h1>

<div>
	{#each colors as color}
	<button
		aria-current={selected === color}
		aria-label=color
		style="background: {color}"
		on:click={() => selected = color}
	></button>
	{/each}

</div>
```

```svelte
<div>
	{#each colors as color, i}
		<button
			aria-current={selected === color}
			aria-label={color}
			style="background: {color}"
			on:click={() => selected = color}
		>{i + 1}</button>
	{/each}
</div>
```

也可以用第二个参数获得当前index



