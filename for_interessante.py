
nomes = ['daniel', 'joao', 'maria', 'ana']

print (nomes[0])
for pessoa in nomes:
    if pessoa.lower().strip() == 'ana':
       print ('achei')
       break
else:
    print ('nao achei a ana')