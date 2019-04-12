#!/usr/bin/env python
# encoding: utf-8
'''
@author: fengtao.xue
@license: (C) Copyright 2016-2019, GAUSSCODE.
@contact: fengtao.xue@gausscode.com
@software: 
@file: start.py
@time: 2019/4/11 15:35
@desc:
'''
import  sys
import datetime
import rpt.rpt as week
import utils.sqlUtils as sqlutils
import utils.dbUtils as db
from datetime import timedelta
from dateutil.relativedelta import relativedelta

'''周报服务'''
def runWeekRpt(startDate, endDate, siteId):
    print('rum weekEpt server......')
    # 检查siteId是否存在
    print('verify the siteId.......')
    siteStr = sqlutils.loadSysDealerSiteSql(siteId)
    res = db.excuteSQL2DF(siteStr)
    if res.empty:
        print('error: siteId %s is not exist, please check it' % (siteId))
        exit(1)
    # 执行周报服务
    siteName = res.iat[0, 6]
    week.genRpt(startDate, endDate, siteId, siteName)

if __name__ == '__main__':
    print('this start.py script must be run based directory on autoRpt! the first param is report type you needed(1 is weekRpt, 2 is monthRpt), the second param is siteId')
    if len(sys.argv) < 3:
        print(
            'erroe, need 2 input param at least, you can run this script like this: python start.py 1 af140c3b88a611e8ad8d7cd30ae0f656')
        exit(1)
        else:
        startDate = ''
        endDate = ''
        rptType = sys.argv[1]
        siteId = sys.argv[2]
        today = datetime.date.today()
        # 周报服务
        if rptType == '1':
            befor_8weeks_start = today - timedelta(days=49 + today.weekday())  # 8个周数据（包含本周）
            this_week_end = today + timedelta(days=6 - today.weekday())
            startDate = befor_8weeks_start.strftime("%Y-%m-%d")
            endDate = this_week_end.strftime("%Y-%m-%d")
            print("now is outputing weekRpt from %s to %s ..." % (startDate, endDate))
            runWeekRpt(startDate, endDate, siteId)
        # 月报服务
        elif rptType == '2':
            befor_5month = today - relativedelta(months=4)
            befor_5month_start = datetime.date(befor_5month.year, befor_5month.month, 1)  # 5个月数据（包含本月）
            this_month_end = datetime.date(today.year, today.month + 1, 1) - datetime.timedelta(1)
            startDate = befor_5month_start.strftime("%Y-%m-%d")
            endDate = this_month_end.strftime("%Y-%m-%d")
            print("now is outputing monthRpt from %s to %s ..." % (startDate, endDate))
            # runMonthRpt(startDate, endDate, siteId)
        else:
            print('erroe: the fisrt param is invalid!')