order_price = int(input("Введите сумму заказа: "))

# Преобразовани типов с int на float
float_order_price = float(order_price)


print()

if float_order_price > 10_000:
    # размер скидки
    discount = 15 / 100
    # размер скидки в рублях
    price_discount = round(float_order_price * discount, 2) # оригинальнее названия для переменной не смог предумать :)
    # цена с учётом скидки
    discount_price = round(float_order_price * (1 - discount), 2)
    print(
        f"Ваша сумма на оплату товара(-ов) составляет: {float_order_price} рублей.",
        "Размер скидки на товар: 15%.",
        f"Размер скидки на товар в рублях: {price_discount} рублей.",
        f"Итоговая цена на товар с учётом скидки: {discount_price} рублей.",
        sep="\n"
    )
elif float_order_price > 5_000:
    discount = 10 / 100
    price_discount = round(float_order_price * discount, 2)
    discount_price = round(float_order_price * (1 - discount), 2)
    print(
        f"Ваша сумма на оплату товара(-ов) составляет: {float_order_price} рублей.",
        "Размер скидки на товар: 10%.",
        f"Размер скидки на товар в рублях: {price_discount} рублей.",
        f"Итоговая цена на товар с учётом скидки: {discount_price} рублей.",
        sep="\n"
    )
else:
    discount = 5 / 100
    price_discount = round(float_order_price * discount, 2)
    discount_price = round(float_order_price * (1 - discount), 2)
    print(
        f"Ваша сумма на оплату товара(-ов) составляет: {float_order_price} рублей.",
        "Размер скидки на товар: 5%.",
        f"Размер скидки на товар в рублях: {price_discount} рублей.",
        f"Итоговая цена на товар с учётом скидки: {discount_price} рублей.",
        sep='\n'
    )
