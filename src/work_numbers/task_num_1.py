"""
    Расчёт итоговой стоимости заказа
"""

price_per_item = 1500.0
quantity = 3
discount = 0.1 # 10% скидки


# расчёт цены с учётом скидки
final_price = price_per_item * quantity * (1 - discount)

# финальная стоимость с округлением
final_price_rounded = round(final_price, 2)

# вывод
print(f"Итоговая цена с учётом скидки составляет - {final_price_rounded}")