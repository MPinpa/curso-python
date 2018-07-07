#!/usr/bin/python3

def boas_vindas(*nomes):
    '''funcao de boas vindas '''
    for nome in nomes:
        print('Seja bem vindo {}'.format(nome))

def boas_vindas2(**pessoas):
    print(pessoas)

boas_vindas2(nome='Daniel', sobrenome='prata', idade=24)

boas_vindas()