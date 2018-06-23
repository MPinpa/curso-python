#!/usr/bin/python3
nomes = ['daniel', 'joao', 'maria', 'ana']
numeros = list(range(10))


# preciso me atentar aos 2 pontos, pois senáo vai copiar o mesmo espaco de memoria
copia = nomes[1:] # cortando o primeiro elemento da lista
nomes[0] = 'pedro'
print (copia)
print (nomes)

copia = nomes[::-1] # cortando o primeiro elemento da lista
print (copia)
print (nomes)