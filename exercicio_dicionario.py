#!/usr/bin/python3

frutas = [

    {'Tipo': 'Morango', 'Quantidade': 50, 'valor': 5.0},
    {'Tipo': 'Laranja', 'Quantidade': 25, 'valor': 7.2},
    {'Tipo': 'Limao', 'Quantidade': 31, 'valor': 9.1},
    {'Tipo': 'alface', 'Quantidade': 20, 'valor': 9.99},
]

total = 0

for fruta in frutas:
    total += fruta['valor'] * fruta['Quantidade']

print(total)

