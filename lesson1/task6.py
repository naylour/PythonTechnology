numbers = input('Введите числа: \n')

numbers = map(lambda number: int(number), numbers.split(' '))

counts = {}

for number in numbers:
    counts[number] = counts.get(number, 0) + 1


counts = sorted([number for number, counts in counts.items() if counts > 1])

print(*counts)
