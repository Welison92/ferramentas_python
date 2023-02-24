def eh_primo(numero):
    if numero < 2:
        return 'Não é um número primo'
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return 'Não é um número primo'
    return 'É um número primo'


print(eh_primo(2))
