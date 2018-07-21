#!/usr/bin/python3

import psycopg2

try:
    con = psycopg2.connect('host=127.0.0.1 dbname=projeto user=admin password=4linux')
    cur = con.cursor()
    #cur = cur.execute("insert into usuarios (nome, idade) values ('naruto', 23)")
    cur.execute("delete from usuarios where id=5")
    con.commit()
    cur.close()
    con.close()
except Exception as e:
    cur.rollback()
    con.rollback()
    print('Erro; {}'.format(e))