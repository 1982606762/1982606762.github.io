---
title: node-study
date: 2023-11-24 09:44:25
tags: node
categories: 前端

---

Intro of node

<!--more-->

# Install&& Use

Use nvm to manage the node version

Use `node index.js` to run single script 

# Node file system

Use `fs.writeFile(file,data)` to write to a file and fs.readFile()` to read from a file. need to require fs first.

```js
const fs = require('fs');

const data = 'This is a test message\n';

// write data into test.txt without deleting the existing data
fs.writeFile('test.txt', data, { flag: 'a+' }, (err) => {
    if (err) {
        console.log(err);
        return;
    }
    console.log('Successfully write data into test.txt');
});

// read data from test.txt
fs.readFile('test.txt', 'utf8', (err, data) => {
    if (err) {
        console.log(err);
        return;
    }
    console.log(data);
});

```

# NPM

use `npm init` to init a npm project

When using the functions in the package normally it needs to use `var xxx =  require("xxxxx")`. But using ECMAScript Modules we can use `import xxx from "xxxxx"`. You need to add `  "type": "module",` in package.json file in order to use import.

