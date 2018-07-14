#!/usr/bin/python3
class Dog():
    ''' tentando abstrair um chachorro '''
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.energia = 5
        self.fome = 5


    def andar(self):
        self.energia -= 1
        self.fome -= 1
        print('andando .... \n energia: {} fome:{}'.format(self.energia, self.fome))

    def comer(self):
        self.fome = 5
        print('Comendo ....')

    def dormir(self):
        self.energia = 5
        print('Dormindo .... energia: {}'.format(self.energia))

    def __str__(self):
        return 'nome: {} idade: {} raca: {}'.format(self.nome,self.idade,self.raca)

