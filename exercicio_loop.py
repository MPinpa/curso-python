#!/usr/bin/python3

num = int(input("Digite um numero: "))
for numero in range(num):
    if numero % 2 == 0:
        print (numero)

num = int(input("Digite um numero: "))
for numero in range(0, num, 2):
        print (numero)