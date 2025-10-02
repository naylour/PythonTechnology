from collections import defaultdict

cook_book = {
    "салат": [
        {"ingridient_name": "сыр", "quantity": 50, "measure": "гр"},
        {"ingridient_name": "томаты", "quantity": 2, "measure": "шт"},
        {"ingridient_name": "огурцы", "quantity": 20, "measure": "гр"},
        {"ingridient_name": "маслины", "quantity": 10, "measure": "гр"},
        {"ingridient_name": "оливковое масло", "quantity": 20, "measure": "мл"},
        {"ingridient_name": "салат", "quantity": 10, "measure": "гр"},
        {"ingridient_name": "перец", "quantity": 20, "measure": "гр"},
    ],
    "пицца": [
        {"ingridient_name": "сыр", "quantity": 20, "measure": "гр"},
        {"ingridient_name": "колбаса", "quantity": 30, "measure": "гр"},
        {"ingridient_name": "бекон", "quantity": 30, "measure": "гр"},
        {"ingridient_name": "оливки", "quantity": 10, "measure": "гр"},
        {"ingridient_name": "томаты", "quantity": 20, "measure": "гр"},
        {"ingridient_name": "тесто", "quantity": 100, "measure": "гр"},
    ],
    "лимонад": [
        {"ingridient_name": "лимон", "quantity": 1, "measure": "шт"},
        {"ingridient_name": "вода", "quantity": 200, "measure": "мл"},
        {"ingridient_name": "сахар", "quantity": 10, "measure": "гр"},
        {"ingridient_name": "лайм", "quantity": 20, "measure": "гр"},
    ],
}


def take_user_number(message: str) -> int:
    try:
        return int(input(message))
    except:  # noqa: E722
        raise Exception("Введите число")


number_of_servings = take_user_number("Введите количество порций: ")


all_ingredients = sum(cook_book.values(), [])

grouped = defaultdict(int)

for ingredient in all_ingredients:
    key = (ingredient["ingridient_name"], ingredient["measure"])

    grouped[key] += ingredient["quantity"]


result = [
    {"ingridient_name": name, "measure": measure, "quantity": quantity}

    for (name, measure), quantity in grouped.items()
]

for ingredient in result:
    name = ingredient['ingridient_name']
    quantity = ingredient['quantity'] * number_of_servings
    measure = ingredient['measure']

    print(f'{name}: {quantity} {measure}.'.capitalize())
