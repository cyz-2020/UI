__author__ = 'Woody'

import logging
# import mysql as sql
import pymysql
import requests

from config import Config


class MysqlDb(object):
    """
        example:
        with MysqlDb() as db:
            rt = db.query(sql, params=())
    """
    global config
    host = Config.MYSQL_HOST
    port = Config.MYSQL_PORT
    user = Config.MYSQL_USER
    pwd = Config.MYSQL_PWD
    database = Config.MONGO_DB
    config = {
        'host': str(host),
        'user': user,
        'passwd': pwd,
        'port': int(port),
        'db': database
    }

    def __init__(self):
        self.conn = pymysql.connect(**config)
        self.cursor = self.conn.cursor()
        print('ccsDB is successful connected!')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()
        if exc_tb:
            print("error: ".format(str(exc_val)))

    def close(self):
        self.cursor.close()
        self.conn.close()

    def query(self, sql, params=()):
        rv = None
        cursor = self.cursor
        try:
            cursor.execute(sql, params)
            # rv = cursor.fetchall()
            rv = cursor.fetchone()
        except Exception as err:
            logging.error('query error: {}'.format(str(err)))
            print(str(err))
        return rv

    def operator(self, sql, params=()):
        rv = False
        cursor = self.cursor()
        try:
            cursor.execute(sql, params)
            self.conn.commit()
            rv = True
        except Exception as err:
            logging.error('query error: {}'.format(str(err)))
            print(str(err))
        return rv


if __name__ == '__main__':
    applycd = 'B0202514080002'
    applyinfo = "select * from c_applyinfo where applycd = '{}'".format(applycd)
    tl_assign = "SELECT tl.APPLYCD,u.LOGINCD FROM `dhcs`.`d_telcs_assign_log` tl left join `newerp`.`m_user` u on tl.TOUSERID = u.USERID WHERE tl.STATUS = '0'"
    ss = MysqlDb()
    rv = ss.query(tl_assign)
    print(rv[0])
    url = "https://npm.taobao.org/mirrors/chromedriver/LATEST_RELEASE"
    # url = Config.driver_url + "LATEST_RELEASE"
    r = requests.get("https://npm.taobao.org/mirrors/chromedriver/LATEST_RELEASE_91")
    ss.close()

