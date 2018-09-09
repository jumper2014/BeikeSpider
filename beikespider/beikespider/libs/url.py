#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 解析各城市的小区版块URL-多线程提速

from beikespider.libs.city import *
from beikespider.libs.district import *
from beikespider.libs.area import *
from beikespider.libs.page import *
import threading


class XiaoQuURL(object):

    def __init__(self):
        prompt = create_prompt_text()
        city = input(prompt)
        self.city = city
        print('[{0}]'.format(city))
        chinese_city = get_chinese_city(city)
        if chinese_city is None:
            print("No such city, please try again.")
        else:
            print('OK, start to crawl ' + chinese_city)

        areas = []
        # 从单个页面获得区县的信息
        districts = get_districts(city)
        # 这个地方开始可以并发获得每个区县的版块信息
        # for district in districts:
        #     areas.extend(get_areas(city, district))

        threads = list()
        for district in districts:
            t = threading.Thread(target=get_areas, args=(city, district,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        while not q.empty():
            next_item = q.get()
            areas.extend(next_item)

        print("-------------")
        print("Area is: ")
        print(areas)
        print("-------------")
        self.start_urls = []
        threads = list()
        for area in areas:
            t = threading.Thread(target=get_page_count,
                                 args=('https://{0}.ke.com/xiaoqu/{1}'.format(city, area), area,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        while not page_q.empty():
            next_item = page_q.get()
            (area, page_count) = next_item
            print("area, page: {0} {1}".format(area, page_count))
            for i in range(1, page_count + 1):
                self.start_urls.append('https://{0}.ke.com/xiaoqu/{1}/pg{2}'.format(city, area, i))
            # page_count = get_page_count('https://{0}.ke.com/xiaoqu/{1}'.format(city, area))
            # print('total page: {0} for {1}:{2}'.format(page_count, city, area))
            # for i in range(1, page_count + 1):
            #     self.start_urls.append('https://{0}.ke.com/xiaoqu/{1}/pg{2}'.format(city, area, i))
        print(self.start_urls)


if __name__ == '__main__':
    pass
