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
   

while True:
    os.system('cls')
    print('=====')
    print('Bem vindo à locadora de carros!')
    print('=====')
    print('O que deseja fazer?')
    print('0 - Mostrar portfólio | 1 - Alugar um carro | 2 - Devolver um carro')
    op = int(input())

    os.system('cls')
    if op == 0: #mostrar a lista de carros
        mostrar_lista_de_carros(carros)
    
    elif op == 1: #fazer a locação do carro
        mostrar_lista_de_carros(carros)
        print('=====')
        print('Escolha o código do carro:')
        cod_car = int(input())
        print('Por quanto dias você deseja alugar este carro?')
        dias = int(input())

        print('Você escolheu {} por {} dias.'.format(carros[cod_car][0], dias))
        print('O aluguel totalizaria R$ {}. Deseja continuar?'.format(dias * carros[cod_car][1]))

        print('0 - sim | 1 - não')
        conf = int(input())
        if conf == 0:
            print('Parabéns você alugou o {} por {} dias'.format(carros[cod_car][0], dias))
            alugados.append(carros.pop(cod_car))

    elif op == 2: #devolução do carro
        if len(alugados) == 0:
            print('Não há carros para devolver')
        else:
            print('Segue a lista de carros alugados. Qual você deseja devolver?')
            mostrar_lista_de_carros(alugados)
            print()
            print('Escolha o código do carro que deseja devolver:')
            cod = int(input())
            if conf == 0:
                print('Obrigado por devolver o carro {}'.format(alugados[cod][0]))
                carros.append(alugados.pop(cod))

    print('')
    print('=====')
    print('0 para CONTINUAR | 1 para SAIR')
    if float(input()) == 1:
        break