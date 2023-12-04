---
title: upload-to-Gdrive
date: 2023-02-06 18:53:48
tags: rclone
categories: Linux
---

rclone is a tool to enable you to sync files on the command line with several online storage platforms.

* install rclone
* Bind with google account
* Upload files to the drive

<!--more-->

# Install rclone


To install rclone on Linux/macOS/BSD systems, run:

```
sudo -v ; curl https://rclone.org/install.sh | sudo bash
```

[official link](https://rclone.org/downloads/)

# Bind with google account

first, create a google service account.[link](https://rclone.org/drive/#:~:text=1.%20Create%20a%20service%20account%20for%20example.com)

[Then configure rclone](https://rclone.org/drive/)

# Upload files to the drive

Upload silently:

`rclone copy <sourcepath> <remotename>:<remotepath> -P >> log.txt`

Check the log file:

`tail --lines=8 log.txt && echo "\n"`

