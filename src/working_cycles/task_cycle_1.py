# Пять товаров с ценами
prices = [500, 1500, 800, 2000, 1200]

# Подсчёт кол-ва товаров, где цена первышает 1000 рублей
count = 0

# Товары цена которых превышает 1000 рублей
new_prices = []

# Подсчёт максимальной цены товара
maximum_price = 0

# Номер товара c макимальной ценой
maximum_index_price = 0

for num_product, product_price in enumerate(prices):
    if product_price > 1000:
        count += 1
        new_prices.append(f"Товар номер {num_product + 1}: {product_price} рублей.")
        if maximum_price < product_price:
            maximum_price = product_price
            maximum_index_price = num_product + 1


# Вывод товаров у которых цена превышает 1000 рублей.
print(
    "Товары с ценой больше 1000 рублей:",
    )
for price in new_prices:
    print(f"- {price}",)

print()

# Вывод кол-ва товаров и максимальной цены
print(
    f"Кол-во товаров с ценой больше 1000 рублей: {count}.",
    f"Товар с максимальной ценой:\n- Товар {maximum_index_price}, цена - {maximum_price} рублей.",
    sep='\n\n'
    )
