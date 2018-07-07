#!/usr/bin/python3

def boas_vindas(nome, idade):
    print("Eu sou {} e tenho {}".format(nome, idade))

def soma(x, y):

    return x+y

def manipular_arquivo(nome, modo, conteudo=None):
    if modo == 'r':
        try:
            with open(nome, modo) as arquivo:
                return arquivo.readlines()
        except Exception as e :
            return manipular_arquivo('python.log', 'a', str(e))
    elif modo == 'a':
        try:
            with open(nome, modo) as arquivo:
                arquivo.write('\n'+conteudo)
                return manipular_arquivo(nome, 'r')
        except Exception as e:
            return manipular_arquivo('python.log', 'a', str(e))
        




