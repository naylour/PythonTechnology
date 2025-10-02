from functools import reduce

def farenheitToCelcium(F: float) -> float:
    return 5 / 9 * (F - 32)

countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

print("Средняя температура в странах:")

for [country, temperatures] in countries_temperature:
    average_temperature_f = reduce(lambda x, y: x + y, temperatures) / len(temperatures)

    average_temperature = farenheitToCelcium(average_temperature_f)

    print(f'{country} - {average_temperature:g} C')
