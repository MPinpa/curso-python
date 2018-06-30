#!/usr/bin/python3

while(True):

    entrada = input("Digite nomes no arquivo: ")

    if entrada.lower() == 'sair':
        break
    else:
        with open('loop.txt', 'a') as arquivo:
            arquivo.write("{}\n".format(entrada))
