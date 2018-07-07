#!/usr/bin/python3

aluno = input("Nome do aluno: ")

soma = 0

try:

    for x in range(2):
        nota = int(input("Digite nota {}: ".format(x+1)))
        soma += nota

    media = soma / 2

    if media >= 7:
        result = 'aprovado'
    else:
        result = 'reprovado'

    print ("O Aluno {} foi {} com a media {}".format(aluno.title(), result, media))

except ValueError:
    print("Nao e inteiro")