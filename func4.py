#!/usr/bin/python3

from random import choice

lista = [
    lambda name : name.title(),
    lambda name : name.lower(),
    lambda name : name.upper()
]

with open('nomes.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()

nome = choice(conteudo)



for itens in lista:
    print (itens(nome.replace('\n', '')))