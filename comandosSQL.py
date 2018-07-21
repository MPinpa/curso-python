
import psycopg2

.connect('host=, dbname=, user=, password=') # conectada no banco

.cursor() # curso do Banco

.execute('') # executa um comando SQL

.fetchone() # retorna somente o primeiro dado do select

.fetchall() # retorna todos os dados do select

.rollback() # retorna ao estado incial

