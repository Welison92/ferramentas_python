import random


def gerar_numero_aleatorio(inicio, fim):
    return random.randint(inicio, fim)


print(gerar_numero_aleatorio(1, 100))