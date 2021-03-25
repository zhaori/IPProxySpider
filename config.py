# coding=utf-8

database = 'ipproxy'
free_ipproxy_table = 'free_ipproxy'
httpbin_table = 'httpbin'
data_port = 8000

DB_config = {
    # 'db_type': 'mongodb',
    # 'db_type': 'sqlite'
    'db_type': 'mysql',

    'mysql': {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': '123456',
        'charset': 'utf8',
    },
    'redis': {
        'host': 'localhost',
        'port': 6379,
        'password': '123456',
        'db': 1,
    },
    'mongodb': {
        'host': 'localhost',
        'port': 27017,
        'username': '',
        'password': '',
    },
    'sqlite': {
        'db': f'{database}.db'
    }
}


def add_sql(db_table):
    add_sqlite_mode = f"""
        create table {db_table} (
            [id] integer PRIMARY KEY AUTOINCREMENT,
            ip text,
            port varchar (10),
            country varchar (120),
            anonymity varchar (6),
            https varchar (6),
            speed varchar (6),
            source varchar (10),
            save_time text,
            vali_count varchar (120)
        )
    """
    add_sqlite_sql = f"""
        insert into {db_table} (
        ip, port, country, anonymity, https, speed, source, save_time, vali_count
        ) values (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    return [add_sqlite_mode, add_sqlite_sql]