def eh_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]


texto = 'arara'

print(eh_palindromo(texto))
