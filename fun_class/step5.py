# -*- coding: cp949 -*-

import sqlite3
import contextlib

@contextlib.contextmanager
def db_connect(url):
    db = sqlite3.connect(url)

    yield db
    db.close()

def main(url):
    with db_connect(url) as conn:
        cur = conn.cursor()
        sql_get_query = '''
            SELECT * FROM stocks
        '''
        for row in cur.execute(sql_get_query):
            print(row)

if __name__ =="__main__":
    url = 'example.db'
    main(url)