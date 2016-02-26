from urlparse import urlparse
import re

from scrapy import Request
from scrapy.spiders import XMLFeedSpider
from bs4 import BeautifulSoup

from ..items import ArticleItem

class InfoQSpider(XMLFeedSpider):
    name = 'infoq'
    allowed_domains = ['infoq.com']
    start_urls = ['http://www.infoq.com/cn/feed']
    itertag = 'item'

    def parse_node(self, response, node):
        item = ArticleItem()
        item['title'] = node.xpath('title/text()').extract()[0]
        item['date'] = node.xpath('pubDate/text()').extract()[0]
        item['url'] = node.xpath('link/text()').extract()[0]

        if urlparse(item['url']).path.startswith(('/cn/news', '/cn/articles')):
            request = Request(url=item['url'], callback=self.parse_article)
            request.meta['item'] = item
            yield request

    def parse_article(self, response):
        item = response.meta['item']
        body = BeautifulSoup(response.body, 'lxml')

        article_content = body.find('div', class_='text_info')
        for script in article_content.find_all('script'):
            script.extract()
        for style in article_content.find_all('style'):
            style.extract()

        content = article_content.get_text()
        content = re.sub(re.compile('\s+'), '', content)

        item['content'] = content

        yield item