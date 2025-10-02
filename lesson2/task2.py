queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

total_number_queries = len(queries)

number_words_in_queries = list(map(lambda s: len(s.split()), queries))

total_number_counts = {num: number_words_in_queries.count(num) for num in set(number_words_in_queries)}

for (number, number_count) in total_number_counts.items():
    percent = (number_count * 100) / total_number_queries

    print(f'Поисковых запросов, содержащих {number} слов(а): {percent:.2f}%')
