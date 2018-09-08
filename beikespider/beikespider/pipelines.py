# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
from beikespider.libs.const import *
from beikespider.spiders.xiaoqu_spider import XiaoQuSpider
from beikespider.libs.path import *
from beikespider.libs.date import *


class BeikespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class CsvWithEncodingPipeline(object):
    """
    保存到文件中对应的class
    1、在settings.py文件中配置
    2、在自己实现的爬虫类中yield item,会自动执行
    """

    def __init__(self):
        create_date_path("bk", XiaoQuSpider.city, get_date_string())
        self.file = codecs.open("data/bk/"+XiaoQuSpider.city+"/"+get_date_string()+"/"+XIAOQU_CSV, 'w', encoding='utf-8')  # 保存为json文件

    def process_item(self, item, spider):
        # line = json.dumps(dict(item), ensure_ascii=False) + "\n"  # 转为json的
        print(item)
        # item = dict(item)
        line = item['name'] + ',' + item['price'] + ',' + item['on_sale'] + '\n'
        self.file.write(line)  # 写入文件中
        return item

    def spider_closed(self, spider):  # 爬虫结束时关闭文件
        self.file.close()
