import itertools


def gerar_combinacoes(elementos, tamanho):
    combinacoes = itertools.combinations(elementos, tamanho)
    for combinacao in combinacoes:
        print(combinacao)


elementos = ['a', 'b', 'c', 'd', 'e', 'f']
tamanho = 5

gerar_combinacoes(elementos, tamanho)
