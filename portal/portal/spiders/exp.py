# -*- coding: utf-8 -*-
import scrapy
from random import choice


class ExpSpider(scrapy.Spider):
    name = 'exp'
    allowed_domains = ['richctrl.com']
    start_urls = ['http://baidu.exp.richctrl.com']

    def parse(self, response):
        print(response.request.headers['User-Agent'], '\n')
        for _ in range(10):
            url = "http://" + UrlRandom()
            yield scrapy.Request(url, callback=self.parse, dont_filter = True)




def UrlRandom():
    url = ['baidu.exp.richctrl.com',
           'taobao.exp.richctrl.com',
           'cnki.exp.richctrl.com',
           'buaa.exp.richctrl.com',
           'sina.exp.richctrl.com',
           'nacta.exp.richctrl.com',
           'ituring.exp.richctrl.com',
           'iqiyi.exp.richctrl.com']

    return choice(url)