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
import rpt.rpt as week
import utils.sqlUtils as sqlutils
import utils.dbUtils as db
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
        startDate = '2019-01-01'
        endDate = '2019-01-31'
        rptType = sys.argv[1]
        siteId = sys.argv[2]
        if rptType == '1':
            runWeekRpt(startDate, endDate, siteId)
        # elif rptType == '2':
            # runMonthRpt(startDate, endDate, siteId)
        else:
            print('erroe: the fisrt param is invalid!')