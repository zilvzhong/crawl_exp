# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NactaSpider(CrawlSpider):
    name = 'nacta'
    allowed_domains = ['exp.richctrl.com']
    start_urls = ['http://nacta.exp.richctrl.com']

    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # print(response.request.headers['User-Agent'], '\n')
        print(response.url)
        return