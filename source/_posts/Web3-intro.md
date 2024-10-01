---
title: Web3-intro
date: 2024-09-02 00:09:07
tags: web3
categories: Blockchain
---

Web3 note from Udemy course.

<!--more-->

# Web3 Decentralised App Development

## How does the blockchain actually work?

区块链就像一个账本，目标是保存一些记录，没有人可以解密并且篡改这些记录。

为了加密我们使用哈希处理。

### block

具体来讲，有一些不一样的block，每一个block的内容都使用sha-256进行哈希处理。每个block包含以下内容：

* block编号
* 随机数Nonce
* block内容
* prev
* hash

通过组合随机数和内容可以得到一个hash值。要想把一个block加入到blockchain中需要这个hash值满足某些要求，比如说以000开头，这时就需要通过不断修改nonce来试出一个合适的随机数。这个要求称为区块链的难度(difficulty)。

某个区块通过随机数来加密，只有这个随机数和block内容的组合可以满足要求，如果内容修改过这个block就不满足要求了。

![image-2024090213948929 AM](https://raw.githubusercontent.com/1982606762/picgo/master/image-2024090213948929%E2%80%AFAM.png)

### blockchain

对于一个链来说，每个block都是通过prev来链接起来的，这时每个block的hash值是通过结合nonce，data和prev三个内容计算出来的。假如某一个block的内容被修改了，那么他后续的所有block都会失效，因为prev修改了。这样可以达到链上所有内容都不能被修改的效果。

![image-2024090214032572 AM](https://raw.githubusercontent.com/1982606762/picgo/master/image-2024090214032572%E2%80%AFAM.png)

### Distributed blockchain

现在有很多矿工，每一个矿工都需要先下载当前的区块链。此时所有人手里的区块链内容都完全一致。假如某个人想修改内容，那么他手上的区块链会首先失效。就算他重新计算每个块的哈希值使其满足要求，他手上区块链的哈希值也和别人手里的不一样，无法通过验证。

![image-2024090214758098 AM](https://raw.githubusercontent.com/1982606762/picgo/master/image-2024090214758098%E2%80%AFAM.png)

## What are Decentralised Apps and how to develop them?

当前每个block的内容部分存储的是一些字段，例如A欠B多少钱之类。还可以在block里存储代码来创建智能合约(smart contracts)，例如当满足某些条件的时候自动触发一些事件。

传统来讲，创建一个公司需要先写代码，然后筹资资金然后上市。但是在Web3时代，可以先写代码，然后发布一些token。其中有一些“管理token”可以让拥有者参与决策，这样每个人都想要让公司价值上升，因为这样的话token就会升值。

首先需要确定要在哪条链上开发Dapps。最多开发的是以太坊，但是在上边进行开发的成本很高，而且他不能存储数据。这时就需要借助Internet computer来进行开发。

### Internet computer

当前绝大多数DApps并不是将全部数据都放在区块链上，而是只把一些逻辑放在区块链上，大多数的数据还是存储在Azure或AWS上。这样他们并没有完全享受到DApps的全部优势，因为会受制于大公司的服务限制。但是要想把巨量的数据保存在传统区块链如以太坊中是很困难的，因为成本很高。

## Motoko Development

actor类似一个类，使用var声明变量.

可以用candid界面来观察函数。

