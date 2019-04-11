#!/usr/bin/env python
# encoding: utf-8
'''
@author: fengtao.xue
@license: (C) Copyright 2016-2019, GAUSSCODE.
@contact: fengtao.xue@gausscode.com
@software: 
@file: rpt.py
@time: 2019/4/11 15:37
@desc:
'''
import time
import rpt.rptSql as sql
import utils.dbUtils as db
import pandas as pd
import utils.mailUtils as mail
def genRpt(startDate, endDate, siteId, siteName):

    '''线索总量'''
    leadsBasicCntStr = sql.loadLeadsBasicCntSql(startDate, endDate, siteId)
    leadsBasicCntDf = db.excuteSQL2DF(leadsBasicCntStr)

    '''线索跟进量'''
    leadsTrackCntStr = sql.loadLeadsTrackCntSql(startDate, endDate, siteId)
    leadsTrackCntDf = db.excuteSQL2DF(leadsTrackCntStr)

    '''分数分布量'''
    leadsScoreCntStr = sql.loadLeadsScoreCntSql(startDate, endDate, siteId)
    leadsScoreCntDf = db.excuteSQL2DF(leadsScoreCntStr)
    time.sleep(5)

    '''准备输出文件'''
    file = './output/' + siteName + '_' + startDate + '_' + endDate + '.xls'
    writer = pd.ExcelWriter(file)

    '''输出文件-线索总量'''
    print('output leadsBasicCntDf...')
    leadsBasicCntDf.to_excel(excel_writer=writer,sheet_name='线索总量', columns=['week', 'count'], header=True, encoding="utf-8", index=False)
    time.sleep(3)

    '''输出文件-线索跟进量'''
    print('output leadsTrackCntDf...')
    leadsTrackCntDf.to_excel(excel_writer=writer, sheet_name='线索跟进量', columns=['week', 'count'], header=True, encoding="utf-8",index=False)
    time.sleep(3)

    '''输出文件-分数分布量'''
    print('output leadsScoreCntDf...')
    leadsScoreCntDf.to_excel(excel_writer=writer, sheet_name='分数分布量', columns=['week', 's2Score', 'count'], header=True, encoding="utf-8", index=False)

    '''保存并关闭文件'''
    writer.save()
    writer.close()
    time.sleep(3)

    '''发送邮件'''
    print('prepare sending email...')
    subject = '_周报_' + file.split("/")[-1]
    msg = '这是Python 邮件发送测试……'
    mailInfo = mail.init()
    mailInfo.send(subject, msg, file)

if __name__ == '__main__':
    genRpt('2019-01-01', '2019-01-31', 'af140c3b88a611e8ad8d7cd30ae0f656')