nome = input("Qual é o seu nome? \n")

pergunta = (input("{}, você sabe a distância?\n ".lower().format(nome)))
if pergunta.startswith('s'):

    distancia = float(input("qual é a distância?\n"))

    aproveitamento = float(input('{}, quantos quilometros seu carro faz por litro? \n'.format(nome)))

    precogas = int(input('{}, qual é o preço da gasolina atualmente?\n'.format(nome)))

    consumo = distancia / aproveitamento

    print("Foram gastos ", consumo, " litros de combustível.")

    custo = consumo * precogas

    print("E você vai gastar", custo, "reais")

elif pergunta.startswith('n'):

    tempohoras = float(input("{}, digite o tempo gasto na viagem (Apenas quantas horas): \n".format(nome)))

    tempominutos = float(input("{}, e quantos minutos? \n".format(nome)))

    velocidade = float(input('{}, digite agora a velocidade média durante a viagem:\n'.format(nome)))

    aproveitamento = float(input('{}, quantos quilometros seu carro faz por litro? \n'.format(nome)))

    precogas = float(input('{}, qual é o preço da gasolina atualmente?\n'.format(nome)))

    consumo = (velocidade * (tempohoras + (tempominutos / 60))) / aproveitamento

    print("Foram gastos ", consumo, " litros de combustível.")

    custo = consumo * precogas

    distancia = velocidade * (tempohoras + (tempominutos / 60))

    print("E você vai gastar", custo, "reais")

    print("A distância percorrida foi de ", distancia, "quilometros.")

else:
    print ("responda sim ou não")