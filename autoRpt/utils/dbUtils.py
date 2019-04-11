#!/usr/bin/env python
# encoding: utf-8
'''
@author: fengtao.xue
@license: (C) Copyright 2016-2019, GAUSSCODE.
@contact: fengtao.xue@gausscode.com
@software: 
@file: dbUtils.py
@time: 2019/4/11 15:31
@desc:
'''
import configparser
import pandas as pd
import pymysql

def loadDBConn():
    """load mysql config"""
    cf = configparser.ConfigParser()
    cf.read('./config.ini', encoding="utf-8-sig")  # 读取配置文件，如果写文件的绝对路径，就可以不用os模块
    host = cf.get("db-dev", "host")
    user = cf.get("db-dev", "user")
    password = cf.get("db-dev", "password")
    db = cf.get("db-dev", "db")
    # print(utils)

    # 连接数据库
    conn = pymysql.connect(host=host, port=3306, user=user, passwd=password, db=db,
                           charset="utf8")
    return conn

def excuteSQL2DF(sql):
    conn = loadDBConn()
    res = pd.read_sql(sql, conn)
    df = pd.DataFrame(res)
    # print(df)
    conn.close()
    return df