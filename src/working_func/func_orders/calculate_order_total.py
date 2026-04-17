def calculate_order_total(price: float, quantity: int, discount: int) -> float:
    discount_order = 1 - (discount / 100)
    final_price = (price * quantity) * discount_order
    return round(final_price, 2)

# price = float(input("Введите соимость заказа: "))
# quantity = int(input("Введите кол-во продуктов: "))
# discount = int(input("Введите размер скидки: "))

# result = calculate_order_total(price, quantity, discount)

# print(f"Стоимость заказа с учётом скидки: {result}")
