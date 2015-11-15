# -*- coding: utf-8 -*-
import scrapy

from zhangxinyun_scrapy.items import ArticleItem

class InfoqSpider(scrapy.Spider):
    name = "infoq"
    allowed_domains = ["infoq.com"]

    def __init__(self, category=None, *args, **kwargs):
        super(InfoqSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["http://www.infoq.com/cn/articles/"] + ["http://www.infoq.com/cn/articles/%d" % page_index for page_index in range(1, 20) if page_index % 12 == 0]

    def parse(self, response):
        type1_article_href_array = response.css(".news_type1 > h2 > a::attr(href)").extract()
        type2_article_href_array = response.css(".news_type2 > h2 > a::attr(href)").extract()
        article_href_array = type1_article_href_array + type2_article_href_array
        for article_href in article_href_array:
            yield scrapy.Request("http://www.infoq.com" + article_href, callback=self.parse_article)

    def parse_article(self, response):
        title = response.css("#content h1::text").extract()[0].strip()

        #content = response.css("#content .text_content_container .text_info_article").extract()[0]
        
        article = ArticleItem()
        article['url'] = response.url
        article['title'] = title
        #article['content'] = content

        #yield article