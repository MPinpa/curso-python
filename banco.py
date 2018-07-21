#!/usr/bin/python3

from pymongo import MongoClient
from pprint import pprint

try:
    con = MongoClient()
    db = con['4linux']
    
    db.pessoas.remove({'_id': 42})

    for doc in db.pessoas.find():
        print(doc)

except Exception as e:
    print('Erro {}'.format(e))
