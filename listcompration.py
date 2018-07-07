#!/usr/bin/python3

# list comperation = for em unica linha

#listas = ['teste', 'outroteste', 'testes']

#listas = [lista.title() for lista in listas]

#print (listas)

lista = [x+1 for x in range(100) if x%2 == 0]

print (lista)