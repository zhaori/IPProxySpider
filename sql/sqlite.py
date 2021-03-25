import sqlite3
import logging
from config import free_ipproxy_table, httpbin_table, add_sql, DB_config
from sql.mysql import MySql
from proxy import Proxy
import datetime
import config


class SQLite(MySql):
    def __init__(self, db=None):
        super(MySql, self).__init__()
        if db is None:
            db = DB_config.get('sqlite').get('db')
        self.conn = sqlite3.connect(database=db)
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(add_sql(free_ipproxy_table)[0])
            self.cursor.execute(add_sql(httpbin_table)[0])
            self.commit()
        except sqlite3.OperationalError:
            pass

    def init_database(self, database_name):
        pass

    def init_proxy_table(self, table_name):
        pass

    def insert_proxy(self, table_name, proxy):
        data = (proxy.ip, proxy.port, proxy.country, proxy.anonymity,
                proxy.https, proxy.speed, proxy.source, datetime.datetime.now(), proxy.vali_count)
        try:
            self.cursor.execute(add_sql(table_name)[1], data)
            self.commit()
            return True
        except Exception as e:
            logging.exception(f"SQLite insert_proxy exception msg: {e}")
            return False

    def update_proxy(self, table_name, proxy):
        # 这里构造SQL语句的时候，IP地址不能正确地识别为字符串格式
        try:
            command = 'UPDATE %s SET ip="'"%s"'", port=%s, country="'"%s"'", anonymity=%s, ' \
                      'source=%s , https="'"%s"'" , speed=%s  WHERE id=%s' % (
                          table_name, proxy.ip, proxy.port, proxy.country, proxy.anonymity,
                          proxy.source, proxy.https, proxy.speed, proxy.id)
            self.conn.execute(command)
            logging.debug('sqlite update_proxy command:%s' % command)
        except Exception as e:
            logging.exception('sqlite update_proxy exception msg:%s' % e)


if __name__ == '__main__':
    """d = SQLite(DB_config.get('sqlite').get('db'))
    proxy = Proxy()
    proxy.set_value(ip='154.16.202.22', port=8080, country='德国 Hesse 法兰克福', anonymity= 3, https='no', speed= -1, source='ipjiangxinanli', vali_count= 0)
    d.insert_proxy(free_ipproxy_table, proxy)"""
    # d = SQLite(config.DB_config.get('sqlite').get('db'))
    # db_type = config.DB_config.get('db_type', 'mysql')
    # db_config = config.DB_config.get(db_type)
# print(db_config)
