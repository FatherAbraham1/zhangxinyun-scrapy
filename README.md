# 毕业设计之网络爬虫

## 安装依赖

使用 Python 包管理器 pip 安装项目依赖

安装开发依赖

	sudo apt-get install build-essential python-dev

安装 *lxml*：

	sudo apt-get install libxml2-dev libxslt-dev

	pip install lxml

安装 *OpenSSL*：

	sudo apt-get install libssl-dev libffi-dev

	pip install pyopenssl

安装 *Scrapy*：

	pip install scrapy

安装 *BeautifulSoup*

	pip install beautifulsoup4

安装 *mysql-connector-python*

	pip install --allow-external mysql-connector-python mysql-connector-python

## 运行

运行爬虫：

	scrapy crawl <spider>
