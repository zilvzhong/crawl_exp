# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
from ..items import PortalItem


def extract_text_by_bs(doc_text):
    """
    提取html页面的所有文本信息。
    """
    title, text = '', ''
    soup = BeautifulSoup(doc_text, 'lxml')
    try:
        for script in soup(["script", "style"]):
            script.extract()
    except Exception as error:
        print(error, "1")
        pass
    else:
        try:
            # get text
            title = soup.title.string
        except Exception as error:
            print(error, "2")
            pass
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
    return title, text




class PorcraSpider(CrawlSpider):
    name = 'porcra'
    allowed_domains = ['buaa.edu.cn']
    start_urls = ['https://www.buaa.edu.cn/']

    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = PortalItem()
        if response.headers['Content-Type'] == b'text/html':
            conntitle, conn = extract_text_by_bs(response.text)
            title = response.xpath('//title/text()').extract_first()
            item['conntitle'] = conntitle
            item['title'] = title
            item['url'] = response.url
            item['conn'] = conn
        return item
