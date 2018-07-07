#!/usr/bin/python3


from datetime import datetime
from func import manipular_arquivo


while(True):
    nome_arq = input('Digite o nome do arq: ')
    if nome_arq == 's':
        break
    mod = input('modo de abertura: ')
    if mod == 'r':
        a = manipular_arquivo(nome_arq,mod)
        print(a)
    elif mod == 'a':
        conteudo = input('Digite o conteudo: ')
        manipular_arquivo(nome_arq, mod, conteudo)

print(datetime.now())