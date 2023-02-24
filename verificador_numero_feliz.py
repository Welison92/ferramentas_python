def eh_feliz(numero):
    historico = set()
    while numero != 1 and numero not in historico:
        historico.add(numero)
        soma = 0
        while numero > 0:
            digito = numero % 10
            soma += digito ** 2
            numero //= 10
        numero = soma
    return numero == 1


for numero in range(20):
    print(eh_feliz(numero))
