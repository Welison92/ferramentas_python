def verificar_palavra(texto, palavra):
    palavras = texto.split()
    return palavra in palavras


texto = "Testando a palavra no texto"
palavra = 'texto'

print(verificar_palavra(texto, palavra))
