#!/usr/bin/python3

nomes = []
while True :
    nome = input("Digite um nome ou sair: ")
    
    if nome.lower().strip() == 'sair':
        break
    nomes.append(nome)

for nome in nomes:
    print ("Seja bem vindo! {}".format(nome))