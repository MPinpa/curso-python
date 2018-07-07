#!/usr/bin/python3

from random import choice

from func import manipular_arquivo

lista = [
    lambda name : name.title(),
    lambda name : name.lower(),
    lambda name : name.upper(),
    lambda name : name.replace('a', '@')
]

conteudo = manipular_arquivo('nomes.txt', 'r')


nome = choice(conteudo)



for itens in lista:
    print (itens(nome), end='')