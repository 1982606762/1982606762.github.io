---
title: Git学习笔记
tags: []
id: '374'
categories:
  - - 学习笔记
date: 2020-07-28 19:53:13
---

下载安装

*   到目标文件夹中git init初始化
*   把文件添加到git仓库使用命令`git add <file>`
*   使用命令 `git commit -m <message>`

*   要随时掌握工作区的状态，使用`git status`命令。
*   如果`git status`告诉你有文件被修改过，用`git diff`可以查看修改内容。

*   `HEAD`指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令`git reset --hard commit_id`。（上一个是HEAD^,上100个是HEAD~100）
*   穿梭前，用`git log`可以查看提交历史，以便确定要回退到哪个版本。
*   要重返未来，用`git reflog`查看命令历史，以便确定要回到未来的哪个版本。

场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令`git checkout -- file`。

场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令`git reset HEAD <file>`，就回到了场景1，第二步按场景1操作。

命令`git rm`用于删除一个文件

  
要关联一个远程库，使用命令`git remote add origin git@server-name:path/repo-name.git`；

关联后，使用命令`git push -u origin master`第一次推送master分支的所有内容；

此后，每次本地提交后，只要有必要，就可以使用命令`git push origin master`推送最新修改；.

要克隆一个仓库，首先必须知道仓库的地址，然后使用`git clone`命令克隆。

$ git clone git@github.com:1982606762/worked1

Git鼓励大量使用分支：

查看分支：`git branch`

创建分支：`git branch <name>`

切换分支：`git checkout <name>`或者`git switch <name>`

创建+切换分支：`git checkout -b <name>`或者`git switch -c <name>`

合并某分支到当前分支：`git merge <name>`

删除分支：`git branch -d <name>`

远程连接github：

## 1\. 检查SSH keys是否存在

输入下面的命令，如果有文件`id_rsa.pub` 或 `id_dsa.pub`，则直接进入步骤3将SSH key添加到GitHub中，否则进入第二步生成SSH key

```
ls -al ~/.ssh
# Lists the files in your .ssh directory, if they exist
```

## 2\. 生成新的ssh key

**第一步：生成public/private rsa key pair**  
在命令行中输入`ssh-keygen -t rsa -C "your_email@example.com"`

默认会在相应路径下（/your\_home\_path）生成`id_rsa`和`id_rsa.pub`两个文件，如下面代码所示

```
ssh-keygen -t rsa -C "your_email@example.com"
# Creates a new ssh key using the provided email
Generating public/private rsa key pair.
Enter file in which to save the key (/your_home_path/.ssh/id_rsa):
```

**第二步：输入passphrase（本步骤可以跳过）**

设置passphrase后，进行版本控制时，每次与GitHub通信都会要求输入passphrase，以避免某些“失误”

```
Enter passphrase (empty for no passphrase): [Type a passphrase]
Enter same passphrase again: [Type passphrase again]
```

sample result:

```
Your identification has been saved in /your_home_path/.ssh/id_rsa.
Your public key has been saved in /your_home_path/.ssh/id_rsa.pub.
The key fingerprint is:
#01:0f:f4:3b:ca:85:d6:17:a1:7d:f0:68:9d:f0:a2:db your_email@example.com
```

**第三步：将新生成的key添加到ssh-agent中:**

```
# start the ssh-agent in the background
eval "$(ssh-agent -s)"
Agent pid 59566
ssh-add ~/.ssh/id_rsa
```

## 3\. 将ssh key添加到GitHub中

用自己喜欢的文本编辑器打开`id_rsa.pub`文件，里面的信息即为SSH key，将这些信息复制到GitHub的`Add SSH key`页面即可