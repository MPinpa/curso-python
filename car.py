#!/usr/bin/python3
class Car:

    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.velocidadekm = 0
        self.tanque = 60

    def acelerar(self):
        self.velocidadekm += 30
        self.tanque -= 1
        print ('Acelerando...')


    def frear(self):
        self.velocidadekm = 0
        print ('freiando ...')


    def __str__(self):
        print ('Marca: {} Modelo: {} ano: {}'.format(self.marca, self.modelo, self.ano))


class Carro_eletrico(Car):
    def __init__(self, ano, modelo, marca):
        super().__init__(ano,modelo, marca)
        self.combustivel = 'energia'


        

