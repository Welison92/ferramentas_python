def calcular_imc(peso, altura):
    return round(peso / altura ** 2, 2)


print(calcular_imc(float(input('Informe o seu peso: ')), float(input('Informe a sua altura: '))))
