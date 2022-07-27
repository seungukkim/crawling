# -*- coding: cp949 -*-

#fun_class/data

import sqlite3

def db_create():
    print("DB 생성")

    conn = sqlite3.connect('example.db')
    cur = conn.cursor()


    # CREATE TABLE
    sql_create_query= '''
        CREATE TABLE stocks(
            date      text
            ,trans    text
            ,symbol   text
            ,qty      real
            ,price    real
        )
    '''

    cur.execute(sql_create_query)

    # 데이터 추가
    sql_insert_query = '''
        INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)
        '''

    cur.execute(sql_insert_query)

    #save
    conn.commit()
    conn.close

if __name__ =="__main__":
    db_create()