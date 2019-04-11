#!/usr/bin/env python
# encoding: utf-8
'''
@author: fengtao.xue
@license: (C) Copyright 2016-2019, GAUSSCODE.
@contact: fengtao.xue@gausscode.com
@software: 
@file: rptSql.py
@time: 2019/4/11 15:37
@desc:
'''
'''
周报-线索总量
'''
def loadLeadsBasicCntSql(startDate, endDate, siteId):
    leadsBasucCntStr = "select " \
                       "date_format(a.first_biz_date, '%s') as week, " \
                       "count(1) as count " \
                       "from calo_frontend.leads_basic_info a " \
                       "where " \
                       "a.del_flag = 0 " \
                       "and a.site_id = '%s' " \
                       "and a.first_biz_date >= '%s' " \
                       "and a.first_biz_date <=  '%s' " \
                       "group by week " \
                       "order by week asc;" % ('%y-%v', siteId, startDate, endDate)
    return leadsBasucCntStr

'''周报-线索跟进量
'''
def loadLeadsTrackCntSql(startDate, endDate, siteId):
    leadsTrackCntStr = "select " \
                       "date_format(a.track_biz_date, '%s') as week, " \
                       "count(1) as 'count' " \
                       "from calo_frontend.leads_track_log a " \
                       "left join calo_frontend.sys_user b on a.track_by = b.id " \
                       "where " \
                       "a.del_flag = 0 " \
                       "and b.site_id = '%s' " \
                       "and a.track_biz_date >=  '%s' " \
                       "and a.track_biz_date <=  '%s' " \
                       "group by week " \
                       "order by week asc;" % ('%y-%v', siteId, startDate, endDate)
    return leadsTrackCntStr

'''
周报-分数分布量
'''
def loadLeadsScoreCntSql(startDate, endDate, siteId):
    leadsScoreCntSql = "select " \
                       "date_format(a.first_biz_date, '%s') as week, " \
                       "s2_score as s2Score, " \
                       "count(1) as count " \
                       "from calo_frontend.leads_basic_info a " \
                       "where a.del_flag = 0 " \
                       "and a.s2_score > 0 " \
                       "and a.site_id = '%s' " \
                       "and a.first_biz_date >= '%s' " \
                       "and a.first_biz_date <= '%s' " \
                       "group by week,s2_score " \
                       "order by week asc" % ('%y-%v', siteId, startDate, endDate)
    return leadsScoreCntSql