"""Копирование списка заказов"""
# Список заказов
orders = [1500, 2300, 890]

# Копия списка
orders_copy_1 = orders.copy()

orders.append(4500)

print(
    f"Текущие заказы: {orders}",
    f"Архив заказов: {orders_copy_1}",
    sep='\n'
)