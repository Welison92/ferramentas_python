import math


def distancia_entre_dois_pontos(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


print(distancia_entre_dois_pontos(3, 4, 6, 8))
