# Заказ 1: с обычной скидкой
order_1_price = 2000.0 # цена за единицу
order_1_quantity = 2 # кол-во
order_1_dicount = 0.15 # скидка


"""Решение задачи с заказом 1"""
# Исходная цена
original_price_1 = order_1_price * order_1_quantity

# Размер скидки
discount_amount_1 = original_price_1 * order_1_dicount

# Итоговая стоимость
total_cost_1 = round(original_price_1 - discount_amount_1, 2)

# Вывод
print("Заказ 1:", f"Исходная цена: {original_price_1}", f"Размер скидки: {discount_amount_1}", f"Итоговая стоимость: {total_cost_1}", sep='\n', end='\n\n')


# Заказ 2: без скидки
order_2_price = 3000.0
order_2_quantity = 1
order_2_dicount = 0.0


"""Решение задачи с заказом 2"""
# Исходная цена
original_price_2 = order_1_price * order_2_quantity

# Размер скидки
discount_amount_2 = original_price_2 * order_2_dicount

# Итоговая стоимость
total_cost_2 = round(original_price_2 - discount_amount_2, 2)

# Вывод
print("Заказ 2:",f"Исходная цена: {original_price_2}", f"Размер скидки: {discount_amount_2}", f"Итоговая стоимость: {total_cost_2}", sep='\n', end='\n\n')


# Заказ 3: с большой суммой
order_3_price = 5000.0
order_3_quantity = 3
order_3_dicount = 0.2


"""Решение задачи с заказом 3"""
# Исходная цена
original_price_3 = order_3_price * order_3_quantity

# Размер скидки
discount_amount_3 = original_price_3 * order_3_dicount

# Итоговая стоимость
total_cost_3 = round(original_price_3 - discount_amount_3, 2)

# Вывод
print("Заказ 3:", f"Исходная цена: {original_price_3}", f"Размер скидки: {discount_amount_3}", f"Итоговая стоимость: {total_cost_3}", sep='\n')