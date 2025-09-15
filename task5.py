stream = [
    '2018-01-01,user100,150',
    '2018-01-07,user99,205',
    '2018-03-29,user1001,81'
]

total_views = 0
users = set()

for line in stream:
    date, user, views = line.split(',')

    total_views += int(views)

    users.add(user)

average = total_views / len(users)

print(f'Среднее количество просмотров на уникального пользователя: {round(average, 2):g}')
