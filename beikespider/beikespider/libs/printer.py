#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 用于存放通用的打印函数


def print_item_num(num):
    print("-" * 20)
    print("本页找到数据: {0} 条".format(num))
    print("-" * 20)


def print_time_cost(duration):
    print("-" * 50)
    print("total time cost:{0} seconds".format(duration))
    print("-" * 50)


if __name__ == '__main__':
    pass