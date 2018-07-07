#!/usr/bin/python3

def boas_vindas(nome, idade):
    print("Eu sou {} e tenho {}".format(nome, idade))

def soma(x, y):

    return x+y

def ler_arquivo(nome_do_arquivo):

    try:

        with open(nome_do_arquivo, 'r') as arquivo:
            return [arquivo.readlines().replace('\n', '') for linha in conteudo]

    except Exception as e:
        
        return "Falha ao ler o arquivo: {}".format(e)

conteudo = ler_arquivo('frutas.txt')

for linha in conteudo:
    print (linha)


