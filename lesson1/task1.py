word = input('Введите слово: ')
word = word.strip()

length = len(word)

if length == 0:
    raise SyntaxWarning('Минимум один символ')


center = length // 2

if length % 2 == 0:
    print(word[center - 1:center + 1])
else:
    print(word[center])
