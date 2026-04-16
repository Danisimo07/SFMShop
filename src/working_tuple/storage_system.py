system_delivery = {}

name_menu = "Главное меню"

print(
    f"{name_menu:^20}",
    "1. Создать заказ.",
    "2. Проверить заказ.",
    "3. Выход.",
    sep='\n'
)

while True:
    choice = input("Введите номер раздела (1-3): ")

    if choice == "1":
        name_delivery = input("\nВведите название заказа: ")
        number_id = int(input("Введите номер своего ID(число) заказа: "))
        cor_x = float(input("Введите координаты X(широта): "))
        cor_y = float(input("Введите координаты Y(долгота): "))

        if "Название заказа" not in system_delivery:
            system_delivery['Название заказа'] = {}
        if number_id not in system_delivery.get("Поиск по ID", {}):
            system_delivery["Поиск по ID"] = system_delivery.get("Поиск по ID", {})

        if name_delivery not in system_delivery["Название заказа"]:
            system_delivery["Название заказа"][name_delivery] = {}
        system_delivery["Название заказа"][name_delivery][number_id] = (cor_x, cor_y)

        system_delivery['Поиск по ID'][number_id] = (cor_x, cor_y)

        # Вывод того, что заказ был успешно добавлен
        print("✅ Заказ был успешно добавлен!")

    elif choice == '2':
        # Проверка заказа
        print(
            "1. Поиск по названию заказа: ",
            "2. Поиск по ID(число) заказа: ",
            sep='\n'
        )

        number_menu = input("Введите номер раздела(1-2)")

        if number_menu == '1':
            """
            Нужно вывести следующее:
                1) Если это поиск по навзванию, то:
                - Название заказа,
                - ID заказа,
                - Вывод координат X и Y (широта и долгота);

                2) Если это поиск по ID заказа, то:
                - ID заказа,
                - Вывод координат X и Y (широта и долгота).
            """

            order_name = input("Название заказа: ").strip()

            if 'Название заказа' in system_delivery and order_name in system_delivery["Название заказа"]:
                orders = system_delivery["Название заказа"][order_name]
                # Вывод результата
                print(f"\n📦 Заказ '{order_name}':")
                for order_id, coords in orders.items():
                    print(
                        f"- ID: {order_id}",
                        f"- Широта X: {coords[0]}",
                        f"- Долгота Y: {coords[1]}",
                        sep='\n'
                    )

            else:
                print("❌ заказ не найден!")

        elif number_menu == '2':
            # Поиск по ID
            order_id = int(input("Введите ID заказа: "))

            if 'Поиск по ID' in system_delivery and order_id in system_delivery["Поиск по ID"]:
                coords = system_delivery["Поиск по ID"][order_id]
                print(
                    f"\n📍 ID: {order_id}",
                    f"- Широта X: {coords[0]}",
                    f"- Долгота Y: {coords[1]}",
                    sep='\n'
                )

            else:
                print("❌ ID не найден!")

        else:
            print("❌ 1-2!")

    elif choice == '3':
        print("👋 До скорых встреч!")
        break

    else:
        print("❌ 1-3!")