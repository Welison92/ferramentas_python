import random


def gerar_cpf():
    numeros = [random.randint(0, 9) for i in range(9)]
    soma = sum([numeros[i] * (10 - i) for i in range(9)])
    digito1 = 11 - soma % 11
    if digito1 > 9:
        digito1 = 0
    numeros.append(digito1)
    soma = sum([numeros[i] * (11 - i) for i in range(10)])
    digito2 = 11 - soma % 11
    if digito2 > 9:
        digito2 = 0
    numeros.append(digito2)
    cpf = ''.join(map(str, numeros))
    return cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]


print(gerar_cpf())
