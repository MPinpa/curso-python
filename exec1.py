#!/usr/bin/python3

try:
    ling = input('Qual melhor linguagem? ')
    if ling == 'python':
        print('Voce acertou!')
    else:
        raise TypeError
except TypeError as e:
    print('erro: Tipo Invalido!')
finally:
    print('sempre executa')