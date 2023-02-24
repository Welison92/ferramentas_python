"""
Este código lê o valor da temperatura, a escala original e a escala para
a qual deseja converter, e chama a função convert_temperature com esses
valores. A função verifica a escala original e a escala de destino, e usa
a fórmula apropriada para fazer a conversão.
"""


def convert_temperature(value, from_scale, to_scale):
    if from_scale == "Celsius":
        if to_scale == "Fahrenheit":
            return (value * 9 / 5) + 32
        elif to_scale == "Kelvin":
            return value + 273.15
    elif from_scale == "Fahrenheit":
        if to_scale == "Celsius":
            return (value - 32) * 5 / 9
        elif to_scale == "Kelvin":
            return (value + 459.67) * 5 / 9
    elif from_scale == "Kelvin":
        if to_scale == "Celsius":
            return value - 273.15
        elif to_scale == "Fahrenheit":
            return (value * 9 / 5) - 459.67
    else:
        return "Escalas inválidas!"


value = float(input("Digite o valor da temperatura: "))
from_scale = input("De qual escala de temperatura (Celsius, Fahrenheit, Kelvin)? ")
to_scale = input("Para qual escala de temperatura (Celsius, Fahrenheit, Kelvin)? ")

result = convert_temperature(value, from_scale, to_scale)

if isinstance(result, float):
    print(f"{value} {from_scale} = {result:.2f} {to_scale}")
else:
    print(result)
