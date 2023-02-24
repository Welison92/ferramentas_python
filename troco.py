valor = float(input("Informe o valor a ser trocado: "))
notas = [200, 100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for i in notas:
    quantidade = int(valor // i)
    print(f"{quantidade} nota(s) de R$ {i:.2f}")
    valor = valor - quantidade * i

print("\nMOEDAS:")
for i in moedas:
    quantidade = int(valor // i)
    print(f"{quantidade} moeda(s) de R$ {i:.2f}")
    valor = valor - quantidade * i
