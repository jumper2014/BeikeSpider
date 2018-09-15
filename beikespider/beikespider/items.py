# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BeikespiderXiaoQuItem(scrapy.Item):
    # 小区数据项
    name = scrapy.Field()
    price = scrapy.Field()
    on_sale = scrapy.Field()


class BeikespiderErShouFangItem(scrapy.Item):
    # 二手房的数据项
    name = scrapy.Field()
    price = scrapy.Field()