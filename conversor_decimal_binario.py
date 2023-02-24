def decimal_para_binario(decimal):
    if decimal == 0:
        return "0"
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return binario


print(decimal_para_binario(1000))
