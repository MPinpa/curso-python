#!/usr/bin/python3

numeros = []

par = []

impar = []

for x in range(1 , 21):

    num = int(input('Digite o numero: '))

    numeros.append(num) 
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print (numeros)
print (par)
print (impar)    