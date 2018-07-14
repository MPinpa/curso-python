#!/usr/bin/python3
class car:

    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.velocidadekm = 0
        self.marcha = 0

    def acelerar(self):
        if self.marcha == 0:
            self.velocidadekm =+ 10
        elif self.marcha > 3 and self.marcha < 5:
            self.velocidade =+ 15
        elif self.marcha == 5 :
            self.velocidade =+ 30

    def frear(self):
        self.velocidade =- 30

    def marcha(self, marcha):
        self.marcha = marcha

    def __str__(self):
        print ('Marca: {} Modelo: {} ano: {}'.format(self.marca, self.modelo, self.ano))


class Carro_eletrico(Car):
    def __init__(self, ano, modelo, marca):
        super().__init__(ano,modelo, marca)
        self.combustivel = 'energia'


        

