#!/usr/bin/python3

from subprocess import run

name = input('digite nome do arquivo: ')

try:

    with open(name, 'r') as arquivo:
        conteudo = arquivo.readlines()
        conteudo.insert(0, '#!/usr/bin/python3\n')

    with open(name, 'w+') as arquivo:
        for linha in conteudo:
            arquivo.write(linha)

except FileNotFoundError:

    with open(name, 'a') as arquivo:
        arquivo.writelines('#!/usr/bin/python3\n')

run(['sudo', 'chmod', '+x', name])