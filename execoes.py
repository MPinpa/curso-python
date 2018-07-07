#!/usr/bin/python3

try:

    num = int(input("Digite um numero inteiro: "))
    num1 = int(input("Digite um numero inteiro: "))
    div = num / num1
    print(div)
except ValueError as e:
    print ('nao e um inteiro {}'.format(e))
except ZeroDivisionError as e:
    print('erro de divisao por 0 {}'.format(e))
except KeyboardInterrupt as e:
    print('adeus...')
except Exception as e:
    pass

#print(num)