#!/usr/bin/python3

def decorator(func):
    def interna(x,y):
        print(x, y)
    return interna

@decorator
def soma(x,y):
    return x + y

