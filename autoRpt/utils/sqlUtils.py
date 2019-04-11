#!/usr/bin/env python
# encoding: utf-8
'''
@author: fengtao.xue
@license: (C) Copyright 2016-2019, GAUSSCODE.
@contact: fengtao.xue@gausscode.com
@software: 
@file: sqlUtils.py
@time: 2019/4/11 15:39
@desc:
'''
def loadSysDealerSiteSql(id):
    return "select * from calo_frontend.sys_dealer_site where del_flag = 0 and id = '%s';" % (id)