#!/usr/bin/python3

aluno = input("Nome do aluno: ")

nota1 = float(input("Digite a nota 1 : "))
nota2 = float(input("Digite a nota 2 : "))
nota3 = float(input("Digite a nota 3 : "))
nota4 = float(input("Digite a nota 4 : "))

soma = nota1 + nota2 + nota3 + nota4
media = soma / 4



if media >= 7:
    result = 'aprovado'

else:

    result = 'reprovado'

print ("O Aluno {} foi {} com a media {}".format(aluno.title(), result, media))