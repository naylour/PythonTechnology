results: dict[str, dict[str, float | int]] = { # Пришлось типизировать, редактор ругался
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}

for social in results:
    revenue, cost = results[social]['revenue'], results[social]['cost']

    results[social]['ROI'] = round((revenue / cost - 1) * 100, 2)

print(results)
