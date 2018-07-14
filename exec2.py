#!/usr/bin/python3

try:
    nomedoarquivo = input('Digite o nome do arquivo: ')
    
    if nomedoarquivo != 'privado':

        with open(nomedoarquivo, 'r') as arquivo:
            conteudo = arquivo.readlines()

        for linha in conteudo:
            print (linha, end='')

    else:

        raise FileNotFoundError

except FileNotFoundError as e:
    print ('Arquivo nao encontrado')
