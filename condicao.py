#!/usr/bin/python3

linguagem = input('Digite uma liguagem e programacao: ')

linguagem = linguagem.lower().strip()

if linguagem == 'python':
    print ('voce escolheu certo!')
elif linguagem == 'golang':
    print ("Ta Valendo")
else:
    print ('Sai Disso')