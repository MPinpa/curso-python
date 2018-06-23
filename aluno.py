#!/usr/bin/python3

aluno = input("Nome do aluno: ")

nota1 = float(input("Digite a nota 1 : "))

nota2 = float(input("Digite a nota 2 : "))

soma = nota1 + nota2
media = soma / 2

print ("O Aluno {} tem a media {}".format(aluno.title(), media))