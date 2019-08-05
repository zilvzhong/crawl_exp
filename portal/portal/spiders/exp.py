# -*- coding: utf-8 -*-
import scrapy
from random import choice

class ExpSpider(scrapy.Spider):
    name = 'exp'
    url_all = []
    allowed_domains = ['richctrl.com']
    start_urls = ['http://taobao.exp.richctrl.com']

    def parse(self, response):
        # print(response.request.headers['User-Agent'], '\n')
        # print(response.text)
        # url_link = response.xpath('//a/@href').extract()
        #
        # for url in url_link:
        #     url = response.urljoin(url)
        #     if "richctrl.com" in url and len(self.url_all) < 100:
        #         self.url_all.append(url)

        for _ in range(10):
            ul = UrlRandom()
            yield scrapy.Request(ul, callback=self.parse, dont_filter=True)
                # yield scrapy.Request(url, callback=self.parse_exp, dont_filter=True)
        # for _ in range(10):
            # url = UrlRandom()
            # yield scrapy.Request(url, callback=self.parse, dont_filter = True)

    # def parse_exp(self, response):
        # a = list.extend(self,)
        # url = choice()
        # print(url, self.url_all)
        # yield scrapy.Request(url, callback=self.parse_exp, dont_filter=True)


def UrlRandom():
    url = ['http://baidu.exp.richctrl.com',
           'http://taobao.exp.richctrl.com',
           'http://cnki.exp.richctrl.com',
           'http://sina.exp.richctrl.com',
           'http://iqiyi.exp.richctrl.com']

    return choice(url)