def nome_da_funcao(parametro, paramentro_default=teste): # Criando a funcao, com um parametro obrigatorio e
    comandos                                             # um parametro default, onde nao precisa definir nos argumentos

nome_da_funcao(argumento) # chamando a funcao com um argumento

nome_da_funcao(paramentro_default=2, parametro=teste ) # especificando qual dos parametro recebe o argumento
                                                       # assim nao importa a ordem

from nome_do_arquivo import nome_da_funcao # importa uma funcao especifica do arquivo

import nome_do_arquivo # importa todas as funcoes do arquivo

import nome_do_arquivo as teste # importa um arquivo com apelidado teste

return #retorna um valor a funcao

global # pega dentro de fora da funcao e traz para dentro do escopo de funcao

Variavel_ local # Se nao existe a variavel no escopo local a funcao vai procurar no escopo global

def nome_da_funcao(*args) # quando nao sei quantos argumento irei receber crio funcao com *args( args e uma variavel )
                          # assim recebendo uma tupla

def nome_da_funcao(*kwargs) # quando nao sei quantos argumento irei receber crio funcao com **kwargs( kwargs e uma variavel )
                          # assim recebendo um dicionario