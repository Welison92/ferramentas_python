def eh_bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return True
    return False


print(eh_bissexto(2023))
print(eh_bissexto(2024))
