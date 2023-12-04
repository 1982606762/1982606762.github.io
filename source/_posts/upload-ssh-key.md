---
title: upload-ssh-key
date: 2023-02-05 14:36:12
tags: ssh
categories: Linux
---

* Generate ssh file
* upload it to the server

<!--more-->

# Generate ssh file

To log in to a server with ssh keys you need to first generate a key file using `ssh-keygen` and get two files id_rsa and id_rsa.pub. The .pub file is a public key, you need to put it into .ssh/authorized_keys file. 

# Upload it to the server

You can paste it yourself or use `ssh-copy-id -i key_file user@host` to upload it automatically.

Or you can do it manually:

1. login to your server and go to ~/.ssh dir
2. `vi authorized_keys`
3. Paste the content of id_rsa.pub into it
