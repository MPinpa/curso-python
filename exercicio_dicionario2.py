#!/usr/bin/python3

from pprint import pprint

frutas = [

    {'Tipo': 'Morango', 'Quantidade': 50, 'valor': 5.0},
    {'Tipo': 'Laranja', 'Quantidade': 25, 'valor': 7.2},
    {'Tipo': 'Limao', 'Quantidade': 31, 'valor': 9.1},
    {'Tipo': 'alface', 'Quantidade': 20, 'valor': 9.99},
]

frutas1 = []

for fruta in frutas:
    fruta['valor'] += fruta['valor']* 0.1

    frutas1.append(fruta)


pprint(frutas1)