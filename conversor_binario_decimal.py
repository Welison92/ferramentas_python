def binario_para_decimal(binario):
    decimal = 0
    for digito in binario:
        decimal = decimal * 2 + int(digito)
    return decimal


binario = '00001'

print(binario_para_decimal(binario))  # 1
