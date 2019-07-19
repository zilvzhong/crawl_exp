# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from elasticsearch_dsl.connections import connections
from .models.es_type import ArticleType


# es = connections.create_connection(ArticleType)
es = connections.create_connection(hosts=['192.168.1.220'])

def gen_suggests(index, info_tuple):
    #根据字符串生成搜索建议数组
    used_words = set()
    suggests = []
    for text, weight in info_tuple:
        if text:
            #调用es的analyze接口分析字符串
            words = es.indices.analyze(index="yyy",  body={'text':text,'analyzer':"ik_max_word"})
            anylyzed_words = set([r["token"] for r in words["tokens"] if len(r["token"])>1])
            new_words = anylyzed_words - used_words
        else:
            new_words = set()

        if new_words:
            suggests.append({"input": list(new_words), "weight": weight})

    return suggests

class PortalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    conntitle = scrapy.Field()
    conn = scrapy.Field()
    url_all = scrapy.Field()

    def save_to_es(self):
        article = ArticleType()
        article.title = self['title']
        article.url = self['url']
        article.conn = self['conn']
        article.suggest = gen_suggests(ArticleType, ((article.title, 10), (article.conn, 7)))
        article.save()
        return