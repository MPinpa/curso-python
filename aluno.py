#!/usr/bin/python3

aluno = input("Nome do aluno: ")

soma = 0
for x in range(4):
    nota = int(input("Digite nota {}: ".format(x+1)))
    soma += nota

media = soma / 4

if media >= 7:
    result = 'aprovado'
else:
    result = 'reprovado'

print ("O Aluno {} foi {} com a media {}".format(aluno.title(), result, media))