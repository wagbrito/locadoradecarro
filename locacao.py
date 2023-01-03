import os

carros = [
          ('Chevrolet Tracker', 120), 
          ('Chevrolet Onix', 90), 
          ('Chevrolet Spin', 150), 
          ('Hyundai HB20', 85), 
          ('Hunday Tucson', 120), 
          ('Fiat Uno', 60), 
          ('Fiat Mobi', 70), 
          ('Fiat Pulse', 130)
        ]

alugados = []

def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print('[{}] {} - R$ {} /dia'.format(i, car[0], car[1]))

mostrar_lista_de_carros(carros)        


print('=====')
print('Bem vindo à locadora de carros!')
print('=====')
print('O que deseja fazer?')
print('0 - Mostrar portfólio | 1 - Alugar um carro | 2 - Devolver um carro')