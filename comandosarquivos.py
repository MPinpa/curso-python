#!/usr/bin/python3

open("arquivo.txt", mododeabertura) # abri um arquivo

# r = abre arquivo para leitura

# w = abre para escrita (sobrescrever)

# x = abre para criar, falha se nao existir

arquivo.read() # ler o arquivo

arquivo.close() # fecha o arquivo, se nao fechar corre o risco de perder o arquivo

with open('arquivo.txt', 'w') as f: #funcao para abrir o arquivo sem close, entao garantimos que ele fecha no final

arquivo.readlines() # retorna uma lista, onde cada elemento da lista e uma linha o arquivo.

arquivo.readline()  # retona uma unica linha

arquivo.seek(0) # zera o cursor de bytes do arquivo, voltando para primeira linha do cursor

arquivo.write("conteudo") # escreve no arquivo





























