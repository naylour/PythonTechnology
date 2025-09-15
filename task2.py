def take_num() -> float | None:
    try:
        number = float(input('Введите число: '))

        return number
    except ValueError as _err:
        print('Введите число!')
        return None

sum = 0

while True:
    user_input = take_num()

    if user_input is None:
        continue

    if user_input == 0:
        break

    sum += user_input



print(f'Сумма равна: {sum:g}')
