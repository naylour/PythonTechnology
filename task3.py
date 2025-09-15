class DatingError(Exception):
    pass

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma']

if len(boys) != len(girls):
    raise DatingError('Внимание, кто-то может остаться без пары!')

boys.sort()
girls.sort()

pairs = zip(boys, girls)

print('Идеальные пары:')

for (boy, girl) in pairs:
    print(f'{boy} и {girl}')
