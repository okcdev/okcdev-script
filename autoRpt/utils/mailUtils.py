#!/usr/bin/env python
# encoding: utf-8
'''
@author: fengtao.xue
@license: (C) Copyright 2016-2019, GAUSSCODE.
@contact: fengtao.xue@gausscode.com
@software: 
@file: mailUtils.py
@time: 2019/4/11 15:33
@desc:
'''
import configparser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

'''邮件信息对象'''
class MailInfo:
    sender = ''
    recivers = ''
    subject = ''
    msgfrom = ''
    msgto = ''
    smtphost = ''

    def __init__(self, sender, recivers, subject, msgfrom, msgto, smtphost):
        self.sender = sender
        self.recivers = recivers
        self.subject = subject
        self.msgfrom = msgfrom
        self.msgto = msgto
        self.smtphost = smtphost

    '''发送邮件'''
    def send(self,rptType, msg, file):
        print('sending email...')
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = Header(self.msgfrom, 'utf-8')
        message['To'] = Header(self.msgto, 'utf-8')
        message['Subject'] = Header(self.subject + rptType, 'utf-8')
        # 邮件正文内容
        message.attach(MIMEText(msg, 'plain', 'utf-8'))
        # 构造附件
        att1 = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename为邮件中附件名
        filename = file.split("/")[-1]
        # 附件名称为中文时的写法
        att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", filename))
        # 附件名称非中文时的写法
        # att1["Content-Disposition"] = 'attachment; filename="%s"'% (filename)
        message.attach(att1)
        # 发送邮件
        try:
            smtpObj = smtplib.SMTP(self.smtphost)
            smtpObj.sendmail(self.sender, self.recivers, message.as_string())
            print("Info: send email successfully")
        except smtplib.SMTPException:
            print("Error: send email failed")

'''初始化邮件信息'''
def init():
    print('init MailInfo...')
    cf = configparser.ConfigParser()
    cf.read('./config.ini',encoding="utf-8-sig")
    sender = cf.get("mail-info", "SEMDER")
    recivers = cf.get("mail-info", "RECEIVERS").split(',')
    subject = cf.get("mail-info", "SUBJECT")
    msgfrom = cf.get("mail-info", "MSGFROM")
    msgto = cf.get("mail-info", "MSGTO")
    smtphost = cf.get("mail-info", "SMTPHOST")
    return MailInfo(sender, recivers, subject, msgfrom, msgto, smtphost)

if __name__ == '__main__':
    rptType = '周报SMTP测试'
    msg = '这是Python 邮件发送测试……'
    file = '../output/报表_2019-01-01_2019-01-31.xls'
    mailInfo = init()
    mailInfo.send(rptType, msg, file)