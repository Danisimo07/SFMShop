def safe_order_total(items):
    try:
        index = input("Введите название товара: ")

        total_cost = 0
        for elem in items:
            name_product = elem.get('name')

            if name_product == index:
                try:
                    price = float(elem['price'])
                    quantity = float(elem['quantity'])

                    total_price = price * quantity
                    total_cost += total_price

                    print(f"✅ Товар {name_product}: {total_price} руб.")
                except (KeyError, TypeError, ValueError):
                    print(f"❌ Ошибка в товаре {name_product}: неверные данные")
                else:
                    print("✅ Всё прошло успешно")
        print(f"Общая стоимость: {total_cost}")
        return total_cost
    except KeyboardInterrupt:
        print("\n❌ Выход по Ctrl+C")
    except Exception as e:
        print(f"Неожидонная ошибка: {e}")
    finally:
        print("✅ Обработка завершена!")

test_items = [
    {"name": "Ноутбук", "price": 50000, "quantity": 1},
    {"name": "Мышь", "price": 1500, "quantity": 2},
    {"name": "Клавиатура"},
    {"name": "Монитор", "price": None, "quantity": 1},
    {"name": "Наушники", "price": 3000, "quantity": 3}
]

result = safe_order_total(test_items)
print(f"Общая стоимость: {result}")
