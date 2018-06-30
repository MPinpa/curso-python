#!/usr/bin/python3

with open('frutas.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    cont = 1
    
with open('frutas2.txt', 'a') as arquivo2:
    for linha in conteudo:
        arquivo2.write("{} - {}".format(cont, linha))
        cont+=1


