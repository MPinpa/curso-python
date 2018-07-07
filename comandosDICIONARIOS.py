#!/usr/bin/python3

pessoa = {'nome': 'teste', 'email': 'contoso@contoso.com'} # Dicionario

pessoa.keys() # retorna as chaves

pessoa.values() # retorna os valores

pessoa.items(x, y) # retorna uma lista com tuplas indicando chave e valor

pessoa.get('idade', 'nao achei') # busca idade no dicionario, se nao encontrar, apresenta nao achei