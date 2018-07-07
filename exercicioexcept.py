#!/usr/bin/python3


try:

    with open('teste.txt', 'r') as arquivo:
        conteudo = arquivo.readlines
        print(conteudo)
except FileNotFoundError as e:
    print ('arquivo nao existe')