cart = []

while True:
    print(
        "\n=== МЕНЮ КОРЗИНЫ ===",
        "1. Добавить товар",
        "2. Удалить товар",
        "3. Показать корзину",
        "4. Самый дорогой товар",
        "5. Выход",
        sep='\n'
        )

    choice = input("Выберите действие (1-4): ")

    # Выход из меню выбора
    if choice == "5":
        break
    # Добавление товара в корзину
    elif choice == "1":
        name = input("Название товара: "),
        price = int(input("Цена: "))
        cart.append([name, price])
        print("✅ Товар был успешно добавлен!")
    # Удаление товара из корзины
    elif choice == "2":
        if not cart:
            print("❌ Корзина пустая!")
            continue
        # Первичный вывод всего, что было добавлено в корзину с целью последующего удаления добавений из корзины
        print("\n Корзина:")
        for index, item in enumerate(cart, 1):
            print(f"№{index}: {item[0]} - {item[1]} руб.")


        # Удаление товара по номеру
        num = int(input("Введите номер товара для удаления: "))
        if 1 <= num <= len(cart):
            removed = cart.pop(num - 1)
            print(f"🗑️ Удалён: {removed[0]} - {removed[1]} руб.")
        else:
            print("❌ Неверный номер!")
    # Показать корзину
    elif choice == "3":
        if not cart:
            print("❌ Корзина пустая!")
        else:
            print("Товары в корзине:")
            sum_total = 0
            for index, item in enumerate(cart, 1):
                print(f"№{index}: {item[0]} - {item[1]} руб.")
                sum_total += 1
            print(f"Итого: {sum_total}")
    # Самый дорогой товар
    elif choice == "4":
        if not cart:
            print("❌ Корзина пустая!")
            continue
        # Сортируем корзину от большего к меньшему и выводим самый дорогой товар
        sorted_cart = sorted(cart, key=lambda x: x[1], reverse=True)
        most_expensive = sorted_cart[0]

        print(
            "\n🏆 Самый дорогой товар:",
            f"Название товара: {most_expensive[0]}",
            f"- Цена: {most_expensive[1]} руб.",
            "=" * 10,
            f"Всего товаров: {len(cart)}",
            sep='\n'
        )

    # Неверный выбор
    else:
        print("❌ Неверный выбор!")
