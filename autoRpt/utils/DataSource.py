import pandas as pd
import pymysql


class SqlHelper(object):

    def __init__(self, host, db, user, pwd, port=3306, charset='utf8'):
        """
        :param host:  主机ip地址或者域名
        :param db:  该主键的对应的数据库
        :param user: 该数据库的用户名称
        :param pwd: 该数据库的用户密码
        :param port:  该主键的对应的数据库的端口，默认是3306
        :param charset: 连接mysql时的编码，默认使用utf8
        """
        self.host = host
        self.db = db
        self.user = user
        self.pwd = pwd
        self.port = port
        self.charset = charset
        self.conn = None
        self.cursor = None
        self.__getConn()


    """
         获取连接对象和游标对象
    """
    def __getConn(self):
        self.conn = pymysql.connect(host=self.host, db=self.db, user=self.user, password=self.pwd, port=self.port, charset=self.charset)
        self.cursor = self.conn.cursor()


    '''新增'''
    def insert(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print('插入数据报错！', str(e))

    '''查询'''
    def queryALL(self, sql):
        try:
            count = self.cursor.execute(sql)
            values = self.cursor.fetchall()  # 符合条件的所有数据，全部赋值给values
            return count, values
        except Exception as e:
            print('查询数据报错！', str(e))

    '''查询'''
    def queryOne(self, sql):
        try:
            self.cursor.execute(sql)
            values = self.cursor.fetchone()  # 符合条件的第一个数据
            return values
        except Exception as e:
            print('查询数据报错！', str(e))

    '''更新'''
    def update(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print('更新数据报错！', str(e))

    '''删除'''
    def delete(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print('删除错误', str(e))

    '''查询结果转dateFrame'''
    def excuteSQL2DF(self, sql):
        try:
            res = pd.read_sql(sql, self.conn)
            df = pd.DataFrame(res)
            return df
        except Exception as e:
            print('查询错误', str(e))

    '''提交'''
    def commit(self):
        try:
            self.conn.commit()
        except Exception as e:
            print('提交失败', str(e))
            self.conn.rollback()

    '''关闭连接'''
    def closeResource(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()