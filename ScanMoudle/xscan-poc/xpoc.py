#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/31/19 10:38 AM
# @Author  : Archerx
# @Blog    : https://blog.ixuchao.cn
# @File    : xpoc.py
# modify from poc-T Proj by Archerx
# xpoc将作为一个单独可运行的组件，和主调度引擎之间耦合度很小


import os
from lib.core.common import set_paths
from lib.core.data import scan_option

def module_path():
    return os.path.dirname(os.path.realpath(__file__))

def main():
    try:
        set_paths(module_path())

        x = {'engine_thread': False, 'engine_gevent': False, 'concurrent_num': 100, 'script_name': '', 'show_scripts': False, 'target_single': '', 'target_file': '', 'target_range': '', 'target_network': '', 'zoomeye_dork': '', 'shodan_dork': '', 'fofa_dork': '', 'censys_dork': '', 'api_limit': 100, 'api_offset': 0, 'search_type': 'host', 'output_path': '', 'logging_level': 0, 'proxy': ''}
        scan_option.update(x)

    except:
        pass

if __name__ == '__main__':
    pass