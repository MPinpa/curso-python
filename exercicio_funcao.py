#!/usr/bin/python3

def venda_frutas(**produto):
    a = produto['Qtd']
    b = produto['Valor']
    c = produto['Tipo']
    result = 'produto {}: Total: {}'.format(c, a*b)
    return result

frutas = {'Tipo': 'Maca', 'Valor': 6.50 , 'Qtd': 30}

frutas2 = {'Tipo': 'Pessego', 'Valor': 3.50 , 'Qtd': 17}

frutas3 = {'Tipo': 'Uva', 'Valor': 9.50 , 'Qtd': 12}

print (venda_frutas(Tipo='Maca',Valor=6.50 ,Qtd=30))