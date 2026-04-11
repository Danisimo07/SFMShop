order_price = int(input("Введите сумму заказа: "))

print()

if order_price > 10_000:
    # размер скидки
    discount = 15 / 100
    # размер скидки в рублях
    price_discount = round(order_price * discount, 2) # оригинальнее названия для переменной не смог предумать :)
    # цена с учётом скидки
    discount_price = round(order_price * (1 - discount), 2)
    print(
        f"Ваша сумма на оплату товара(-ов) составляет: {order_price} рублей.",
        "Размер скидки на товар: 15%.",
        f"Размер скидки на товар в рублях: {price_discount} рублей.",
        f"Итоговая цена на товар с учётом скидки: {discount_price} рублей.",
        sep="\n"
    )
elif order_price > 5000:
    discount = 10 / 100
    price_discount = round(order_price * discount, 2)
    discount_price = round(order_price * (1 - discount), 2)
    print(
        f"Ваша сумма на оплату товара(-ов) составляет: {order_price} рублей.",
        "Размер скидки на товар: 10%.",
        f"Размер скидки на товар в рублях: {price_discount} рублей.",
        f"Итоговая цена на товар с учётом скидки: {discount_price} рублей.",
        sep="\n"
    )
else:
    discount = 5 / 100
    price_discount = round(order_price * discount, 2)
    discount_price = round(order_price * (1 - discount), 2)
    print(
        f"Ваша сумма на оплату: {order_price} рублей.",
        "Размер скидки на товар: 5%.",
        f"Размер скидки на товар в рублях: {price_discount} рублей.",
        f"Итоговая цена на товар с учётом скидки: {discount_price} рублей.",
        sep='\n'
    )
