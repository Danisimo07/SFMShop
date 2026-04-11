order_price = int(input("Введите сумму заказа: "))

print()

if order_price > 10_000:
    # размер скидки
    discount = 15 / 100
    # цена с учётом скидки
    discount_price = round(order_price * (1 - discount), 2)
    print(
        "Размер скидки на товар: 15%.",
        f"Цена на товар с учётом скидки составляет: {discount_price} рублей.",
        sep="\n"
    )
elif order_price > 5000:
    discount = 10 / 100
    discount_price = round(order_price * (1 - discount), 2)
    print(
        "Размер скидки на товар: 10%.",
        f"Цена на товар с учётом скидки составляет: {discount_price} рублей.",
        sep="\n"
    )
else:
    discount = 5 / 100
    discount_price = round(order_price * (1 - discount), 2)
    print(
        "Размер скидки на товар: 5%.",
        f"Цена на товар с учётом скидки составлят: {discount_price} рублей.",
        sep='\n'
    )
