---
title: Azure-learn
date: 2024-07-07 01:47:49
tags:
categories: Azure
---

AZ 900 note

<!--more-->

# Core Concepts and Service

## Cloud Computing

describe cloud concepts 20-25%



Three deployment models for cloud computing:

### Public cloud

公有云通过公共互联网提供，任何人都能购买使用，按用量支付。

优点：

* 按需消费
* 无需硬件投资
* 自动化快速配置
* 减少硬件维护

### private cloud

私有云是企业专有的计算资源，可以在组织办公地点也可以由第三方提供。

优点：

* 有一些无法在公共云中复制的环境需要
* 无法轻易迁移的程序
* 数据主权和安全
* 法规认证



### hybrid cloud

部分私有部分公有



## Cloud computing types

### ![image-2024070824049880 PM](https://raw.githubusercontent.com/1982606762/picgo/master/image-2024070824049880%E2%80%AFPM.png)

### **SaaS（Software as a Service，软件即服务）**：

​	•	**定义**：SaaS 是一种通过互联网提供的软件服务模式。用户可以通过网络访问和使用软件，而不需要关心软件的安装、维护和管理。

​	•	**特点**：

​	•	软件由服务提供商托管，用户通过浏览器或客户端访问。

​	•	用户不需要管理基础设施或平台，只需使用软件功能。

​	•	适用于各种业务应用，如电子邮件、办公软件、客户关系管理（CRM）系统等。

​	•	**例子**：Google Workspace（原 G Suite）、Microsoft Office 365、Salesforce。

### **IaaS（Infrastructure as a Service，基础设施即服务）**：

​	•	**定义**：IaaS 提供计算基础设施，如虚拟化的计算资源、存储、网络等，用户可以根据需求灵活配置和使用。

​	•	**特点**：

​	•	提供虚拟机、存储空间、网络资源等基础设施，用户可以部署和管理自己的操作系统和应用程序。

​	•	用户需要管理操作系统、应用程序和数据，但不需要管理底层硬件。

​	•	适用于需要高度灵活性和控制力的企业和开发者。

​	•	**例子**：Amazon Web Services（AWS）、Microsoft Azure、Google Cloud Platform（GCP）。

### **PaaS（Platform as a Service，平台即服务）**：

​	•	**定义**：PaaS 提供一个平台，包括操作系统、编程语言执行环境、数据库和 web 服务器，用户可以在这个平台上开发、运行和管理应用程序。

​	•	**特点**：

​	•	提供完整的开发和部署环境，开发者可以专注于代码和应用程序，而不需要管理底层基础设施。

​	•	包括应用程序开发框架、中间件、数据库管理系统等。

​	•	适用于开发、测试和部署应用程序的开发者和企业。

​	•	**例子**：Google App Engine、Heroku、Microsoft Azure App Services。

总结来说，SaaS 是为最终用户提供的软件服务，IaaS 是为需要基础设施的用户提供的服务，而 PaaS 是为开发者提供的开发和部署平台。

## Azure Cosmos DB

基于Azure SQL 的关系型数据库。

> 关系型数据库：使用表来表示和存储数据
>
> **主要特点：**
>
> ​	1.	**表结构**：数据存储在表中，每个表包含多行和多列。每一行代表一条记录，每一列代表一个字段。
>
> ​	2.	**关系**：表之间可以通过外键（foreign keys）建立关系，从而实现数据的关联和查询。
>
> ​	3.	**SQL（Structured Query Language）**：关系型数据库使用SQL作为其标准查询语言，用于执行数据的查询、插入、更新和删除操作。
>
> ​	4.	**数据完整性**：通过主键（primary key）、外键和其他约束（constraints）来确保数据的一致性和完整性。
>
> ​	5.	**事务支持**：关系型数据库支持事务（transactions），保证一组操作的原子性、一致性、隔离性和持久性（ACID属性）。

使用迁移工具可以方便地将本地SQL数据库迁移到Azure SQL里

所有用户每一个订阅都可以有一个免费SQL数据库，有免费的32G存储和100000秒vCore使用，这里vCore在使用时才会计时，不用的时候不计时，所以时间够用。sqluser/password1!

## Azure Synapse Analytics

用于处理大数据

## Azure Blob storage

storage service optimized for very large objects, such as video, audio, bitmaps.

## Azure compute

### Virtual Machines

scale set 可以管理一组虚拟机来实现负载均衡。

### Container Services

可以管理容器。使用kubernetes可以管理一个容器集群。

### Azure App Service

管理app

### Azure functions

无服务器计算服务，只需要运行一些函数代码时使用。

## Azure Storage

blob是非结构化存储方案，用于存储大量文件

![image-2024070984825743 PM](https://raw.githubusercontent.com/1982606762/picgo/master/image-2024070984825743%E2%80%AFPM.png)



## Azure policy

Azure Policy is a service in Azure that you use to create, assign, and manage policies. These policies enforce different rules and effects over your resources, so those resources stay compliant with your corporate standards and service level agreements. You can use Azure Policy to enforce policies that limit the regions available for resource creation.



## Azure AI

### Azure Machine Learning 

使用数据训练。

使用现有数据进行预测而不是预训练模型进行预测。重点在于使用以往数据来做事情。

### Azure Cognitive Service 

包含一些训练好的模型，可以直接进行预测。

语音转文字，语言识别，预测用户行为等，重点在于understand content and meaning



### Azure Bot Service 

提供和人类交流的机器人如ChatBot，重点在于是一个virtual agent。

## Azure DevOps

### Azure DevOps Services

包含一系列软件开发流程相关的工具，如boards, repos, pipelines等。

### Github

代码存储，运行，自动化。

## Azure Serverless technology

### Azure functions

更偏向代码，如果有现成代码就用这个

### Azure Logic apps

更偏向GUI界面

## Azure IOT Service

### Azure IoT Hub

特点：**acts as a central message point for bi-directional communication between your IoT application and the devices it manages**



链接IoT设备到hub管理

可以控制设备，还可以监控设备。

从设备到服务器发送信息

### IoT Central

特点：可以使用预设好的自定义用户界面user interface来远程查看和控制所有设备

推送更新，批量管理

使用设备模板

### Azure Sphere

特点：安全性最高，控制全套安全设置



## Azure Security

### Azure Security Center

1. 监控所有服务的安全情况和设置
2. 当有资源上线时自动申请权限
3. 提供安全建议
4. 监控资源并且识别漏洞
5. 使用机器学习检测漏洞
6. In-time access control可以设置在特定时间允许流量进入

### Azure Sentinel

基于云的SIEM系统

1. 收集大数据
2. 检测威胁
3. 快速相应

### Azure Key Vault

密码管理器

### Azure Dedicated host

为了符合法规要求，它要求某些组织成为唯一使用托管虚拟机的物理机的客户。

## Network Security

Azure 网络由很多层layer来保护

Physical layer：保安

Perimeter layer：防DDoS攻击

Network layer：限制数据通信，通过限制访问权限来保护

Compute layer：系统更新，系统漏洞

Application layer：软件更新，软件漏洞

Azure DDoS protection：可以防护ddos攻击，通过识别攻击流量

Azure security group：可以进行内部防护

Azure服务推荐：

firewall可以提供外部防护

security group可以进行流量分层，主要是保护虚拟网络里的安全

# Service and Lifecycles

包含40%考试内容

20-25%是identity,governance,privacy和compliance feature

10-15%是cost management, service level agreement

## Identity Service

Authentication 和 authorization的区别：

Authentication是确认用户身份

Authorization是给用户权限

### Active Directory

员工管理系统，可以让员工有权限登录各种资源

可以拒绝可疑登录（authentivation），提供单点登录（跳转到登录界面登录），SSO（用一个登录信息登录所有东西），Application management（权限管理），device management（只有已知设备可以登录）

### Single sign-on

让用户登录一次就可以登录所有东西

### Multifactor Authentication

可以要求用户使用其他手段辅助登录如验证码或指纹

## Cloud Governance Strategy



### Resource lock

防止资源被修改或删除

只有管理员可以解锁，要想修改必须先解锁

### Resource tag

可以帮助管理资源

### Azure Policy

帮助控制Azure资源合规性

### Azure blueprint





## Privacy and compliance

Microsoft Privacy Statement：提供微软所有服务的隐私声明

Online Services Terms：微软和用户的法律协议

### Azure Government

隔离的Azure服务，针对美国政府用户



