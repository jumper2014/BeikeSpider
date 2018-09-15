# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
from beikespider.libs.const import *
from beikespider.spiders.xiaoqu_spider import *
from beikespider.spiders.ershoufang_spider import *
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
        self.init = False


    def process_item(self, item, spider):
        if isinstance(spider, XiaoQuSpider):
            file_name = "xiaoqu.csv"
        elif isinstance(spider, ErShouFangSpider):
            file_name = "ershoufang.csv"

        if not self.init:
            create_date_path("bk", spider.city, get_date_string())
            self.file = codecs.open("data/bk/" + spider.city + "/" + get_date_string() + "/" + file_name, 'w',
                                    encoding='utf-8')  # 保存为json文件
            self.init = True

        # line = json.dumps(dict(item), ensure_ascii=False) + "\n"  # 转为json的
        print(item)
        # item = dict(item)
        if isinstance(spider, XiaoQuSpider):
            line = item['name'] + ',' + item['price'] + ',' + item['on_sale'] + '\n'
        elif isinstance(spider, ErShouFangSpider):
            line = item['name'] + ',' + item['price']+ '\n'
        self.file.write(line)  # 写入文件中
        return item

    def spider_closed(self, spider):  # 爬虫结束时关闭文件
        self.file.close()
