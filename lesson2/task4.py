stats = {
    "facebook": 55,
    "yandex": 115,
    "vk": 120,
    "google": 99,
    "email": 42,
    "ok": 98,
}

max_sales_value = max(stats, key=stats.get) # type: ignore

print(max_sales_value)
