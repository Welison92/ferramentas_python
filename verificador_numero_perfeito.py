def eh_perfeito(numero):
    soma = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma += i
    return soma == numero


for numero in range(20):
    print(eh_perfeito(numero))
