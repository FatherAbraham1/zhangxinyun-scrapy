# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import tempfile
import subprocess

import requests

class SparkPipline(object):

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        host = settings['HADOOP_NAMENODE_HOST']
        port = settings['HADOOP_NAMENODE_PORT']

        return cls(host, port)

    def __init__(host, port):
        self.namenode_host = host
        self.namenode_port = port

    def open_spider(self, spider):
        temp = tempfile.TemporaryFile()
        self.temp = temp

    def close_spider(self, spider):
        url = "http://{}:{:d}/webhdfs/v1/zxy".format(self.namenode_host, self.namenode_port)
        params = {
            'user.name': 'root',
            'op': 'CREATE',
            'overwrite': 'true'
        }
        response = requests.put(url, params=params, allow_redirects=False)
        
        if response.status_code == requests.codes['temporary_redirect']:
            redirect_location = response.headers['Location']
            requests.put(redirect_location, data=self.temp)
        
        self.temp.close()

        # subprocess.call(['spark-submit', 'tfidf.py', '--py-files', 'jieba.zip'], shell=True)

    def process_item(self, item, spider):
        self.temp.write(item['content'].encode('utf-8'))
        return item