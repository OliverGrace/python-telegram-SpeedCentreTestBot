# python-telegram-SpeedCentreTestBot

This is a subscription manage bot for telegram.

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://github.com/OliverGrace/python-telegram-SpeedCentreTestBot/">
    <img src="logo/image.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">SpeedCentreTestBot</h3>
  <p align="center">
    一个简单易用的tg测速组订阅管理bot，集成大量功能！
    <br />
    <a href="https://github.com/OliverGrace/python-telegram-SpeedCentreTestBot"><strong>探索本项目的文档 »</strong></a>
    <br />
    <br />
    <a href="https://github.com/OliverGrace/python-telegram-SpeedCentreTestBot">查看Demo</a>
    ·
    <a href="https://github.com/OliverGrace/python-telegram-SpeedCentreTestBot/issues">报告Bug</a>
    ·
    <a href="https://github.com/OliverGrace/python-telegram-SpeedCentreTestBot/issues">提出新特性</a>
  </p>

</p>

集成查看所有机场名，模糊搜索机场对应订阅链接，限定bot可用用户，随机抽取机场订阅，增加机场订阅，快捷clash订阅转换，自动定时删除信息等功能
 
## 目录

- [上手指南](#上手指南)
  - [配置要求](#配置要求)
  - [安装步骤](#安装步骤)
- [文件目录说明](#文件目录说明)
- [开发的架构](#开发的架构)
- [使用到的框架](#使用到的模块)
- [贡献者](#贡献者)
  - [如何参与开源项目](#如何参与开源项目)
- [版本控制](#版本控制)
- [作者](#作者)

### 上手指南



###### 配置要求

1. python3.x(已测试)
2. 安装python-telegram-bot模块

###### **安装步骤**

1. 进入cmd或者linux终端安装模块

```sh
pip3 install python-telegram-bot
```

2. 克隆本项目

```sh
git clone https://github.com/OliverGrace/python-telegram-SpeedCentreTestBot.git
```

3. 修改main.py中的BOT_TOKEN为自己的TOKEN，并修改myuserid为自己的ID


4. 启动.py脚本程序并在后台运行

```sh
nohup python3 main.py &
```

5. 向TelegramBotFather中你的Bot命令编辑发送以下字段：

```sh
listname-/listname查看所有机场名  
getlink-/getlink <搜索关键字>查看机场订阅链接  
addaccess-/addaccess <id>增加访问权限  
add-/add <机场名>+空格+<链接>添加订阅  
random-/random+空格+<个数（可选）>随机抽一个机场  
convert-/convert+空格+链接转换成Clash订阅  
```

### 文件目录说明

```
filetree 
├── README.md
├── add.py
├── clash_sub_converter.py
├── get_link.py
├── listname.py
├── main.py
├── timer.py
├── sub.txt
├── sub_found.txt
└── access.txt

```

### 使用到的模块

- [python-telegram-bot](https://python-telegram-bot.org)

### 贡献者

OliverGrace

#### 如何参与开源项目

贡献使开源社区成为一个学习、激励和创造的绝佳场所。你所作的任何贡献都是**非常感谢**的。


1. Fork 当前项目
2. 创造自己的 Branch (`git checkout -b feature/AmazingFeature`)
3. Commit 你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. Push 到 Branch (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request



### 版本控制

该项目使用Git进行版本管理。您可以在repository参看当前可用版本。

### 作者

Author:OliverGrace  
E-Mail:1328780068@qq.com  
qq:1328780068    

 *您也可以在贡献者名单中参看所有参与该项目的开发者。*

### 版权说明

该项目签署了MIT授权许可，详情请参阅 [LICENSE.txt](https://github.com/OliverGrace/python-telegram-SpeedCentreTestBot/blob/master/LICENSE.txt)

<!-- links -->
[your-project-path]:OliverGrace/python-telegram-SpeedCentreTestBot
[contributors-shield]: https://img.shields.io/github/contributors/OliverGrace/python-telegram-SpeedCentreTestBot.svg?style=flat-square
[contributors-url]: https://github.com/OliverGrace/python-telegram-SpeedCentreTestBot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/OliverGrace/python-telegram-SpeedCentreTestBot.svg?style=flat-square
[forks-url]: https://github.com/OliverGrace/python-telegram-SpeedCentreTestBot/network/members
[stars-shield]: https://img.shields.io/github/stars/OliverGrace/python-telegram-SpeedCentreTestBot.svg?style=flat-square
[stars-url]: https://github.com/OliverGrace/python-telegram-SpeedCentreTestBot/stargazers
[issues-shield]: https://img.shields.io/github/issues/OliverGrace/python-telegram-SpeedCentreTestBot.svg?style=flat-square
[issues-url]: https://img.shields.io/github/issues/OliverGrace/python-telegram-SpeedCentreTestBot.svg
[license-shield]: https://img.shields.io/github/license/OliverGrace/python-telegram-SpeedCentreTestBot.svg?style=flat-square
[license-url]: https://github.com/OliverGrace/python-telegram-SpeedCentreTestBot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/shaojintian



