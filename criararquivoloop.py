#!/usr/bin/python3

with open('loop.txt', 'a') as arquivo:

    while True:

        entrada = input("Digite nomes no arquivo: ")

        if entrada.strip().lower() == 'sair':
            break
         arquivo.write("{}\n".format(entrada))
