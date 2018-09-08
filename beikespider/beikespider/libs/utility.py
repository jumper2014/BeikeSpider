#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

from pathlib import Path


def create_dir(name):
    if not Path.exists(name):
        Path.mkdir(name)
