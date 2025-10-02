# my_list = ['2018-01-01', 'yandex', 'cpc', 100]
my_list = ['a', 'b', 'c', 'd', 'e', 'f']

def to_nested_dict(lst: list) -> dict:
    if len(lst) == 2:
        return { lst[0]: lst[1] }

    return { lst[0]: to_nested_dict(lst[1:]) }

print(to_nested_dict(my_list))
