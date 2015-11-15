# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from bs4 import BeautifulSoup
import mysql.connector
import uuid
import re

class ReduceNoisePipeline(object):

    def process_item(self, item, spider):
        content = item['content']

        soup = BeautifulSoup(content)
        content = soup.get_text()
        if content:
            pattern = re.compile('\s+')
            content = re.sub(pattern, '', content)
            print content
            item['content'] = content
            return item
        else:
            raise DropItem("Missing content in %s" % item)

class PersistentPipline(object):

    def __init__(self):
        self.database_config = {
            'host': '192.168.1.104',
            'user': 'lizhen',
            'password': '1',
            'database': 'scrapy',
            'raise_on_warnings': True
        }

    def open_spider(self, spider):
        self.connection = mysql.connector.connect(**(self.database_config))

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        cursor = self.connection.cursor()

        item['id'] = str(uuid.uuid1()).replace('-', '')

        sql = ("INSERT INTO blog "
            "(id, url, title, content) "
            "VALUES (%(id)s, %(url)s, %(title)s, %(content)s)")
        cursor.execute(sql, {'id': item['id'], 'url': item['url'], 'title': item['title'], 'content': item['content']})
        self.connection.commit()
        cursor.close()