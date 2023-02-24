import calendar


def gerar_calendario_mensal(ano, mes):
    return calendar.month(ano, mes)


print(gerar_calendario_mensal(2023, 2))
