#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 板块信息相关函数

from beikespider.libs.district import *
from beikespider.libs.request_headers import *
from queue import Queue

q = Queue()

def get_district_url(city, district):
    """
    拼接指定城市的区县url
    :param city: 城市
    :param district: 区县
    :return:
    """
    return "http://{0}.ke.com/xiaoqu/{1}".format(city, district)


def get_areas(city, district):
    """
    通过城市和区县名获得下级板块名
    :param city: 城市
    :param district: 区县
    :return: 区县列表
    """
    page = get_district_url(city, district)
    areas = list()
    try:
        headers = create_headers()
        response = requests.get(page, timeout=10, headers=headers)
        html = response.content
        root = etree.HTML(html)
        links = root.xpath("/html/body/div[3]/div[1]/dl[2]/dd/div/div[2]/a")

        # 针对a标签的list进行处理
        for link in links:
            relative_link = link.attrib['href']
            # 去掉最后的"/"
            relative_link = relative_link[:-1]
            # 获取最后一节
            area = relative_link.split("/")[-1]
            # 去掉区县名,防止重复
            if area != district:
                chinese_area = link.text
                chinese_area_dict[area] = chinese_area
                print(chinese_area)
                areas.append(area)
        q.put(areas)
        return areas
    except Exception as e:
        print(e)


if __name__ == "__main__":
    import threading
    threads = list()
    for dis in ["huangpu", "xuhui"]:
        t = threading.Thread(target=get_areas, args=('sh', dis,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    while not q.empty():
        next_item = q.get()
        print(next_item)

    # print(get_areas("sh", "huangpu"))

