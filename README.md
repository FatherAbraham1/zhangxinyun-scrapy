# 毕业设计之网络爬虫

## 部署环境

操作系统：Ubuntu 14.04

Python 版本：Python 2.7


## 安装依赖

安装开发依赖

	sudo apt-get install build-essential python-dev

安装 *lxml* 依赖：

	sudo apt-get install libxml2-dev libxslt-dev

安装 *OpenSSL* 依赖：

	sudo apt-get install libssl-dev libffi-dev

安装 Python 包管理器 *pip*：

	wget https://bootstrap.pypa.io/get-pip.py && sudo python get-pip.py
	
安装 Python 虚拟环境 *virtualenv*

	sudo pip install virtualenv

## 运行 Scrapyd

创建目录 *scrapyd*

	mkdir scrapyd && cd scrapyd

创建并启动 Python 虚拟环境

	virtualenv venv && source venv/bin/activate
	
安装 scrapyd

	pip install lxml pyopenssl scrapyd

启动 scrapyd

	scrapyd

## 应用部署

克隆最新的代码到本地

	git clone https://github.com/zhangxinyun/zhangxinyun-scrapy.git && cd zhangxinyun-scrapy
	
创建并启动 Python 虚拟环境

	virtualenv venv && source venv/bin/activeate

安装项目依赖

	pip install -r requirements.txt
	
部署项目到 scrapyd

	pip install scrapyd-client && scrapyd-deploy -p zhangxinyun_scrapy
