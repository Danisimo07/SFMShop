users = {}
products = {}
visitors = set()

print(
    "🛒 Система магазина (пустая)",
    f"Пользователи: {len(users)}",
    f"Товары: {len(products)}",
    f"Посетители: {len(visitors)}",
    sep='\n'
)

while True:
    print(
        "\n1. Добавить пользователя",
        "2. Добавить товар",
        "3. Зарегистрировать посетителя",
        "4. Найти товар",
        "5. Показать всё",
        "6. Выход",
        sep='\n'
    )


    choice = input("Выбор (1-6): ")

    if choice == '1':
        # Данные на вход
        user_id = input("ID пользователя: ").strip()
        name = input("Имя: ").strip()
        email = input("Email: ").strip()
        # Было сделано преобразование типов с user_id -> int(user_id)
        users[int(user_id)] = {
            "name": name,
            "email": email
        }
        print(f"✅ '{name}' (ID:{user_id}) -> users")

    elif choice == '2':
        # Данные на вход
        product_name = input("Название товара: ").strip()
        price = input("Цена: ").strip()
        category = input("Категория: ").strip()

        products[product_name] = {
            'price': int(price),
            'category': category
        }
        print(f"✅ '{product_name}' -> products")

    elif choice == '3':
        # Данные на вход
        visitor_id = input("ID посетителя: ").strip()

        if visitor_id not in visitors:
            visitors.add(visitor_id)
            print(f"👋 Новый: '{visitor_id}' -> visitors")
        else:
            print(f"👤 Уже есть: '{visitor_id}'")

    elif choice == '4':
        # Поиск в products
        search_name = input("Название для поиска: ").strip()
        # Произвёл замену с product_name на products
        if search_name in products:
            info = products[search_name]
            print(
                f"✅ НАЙДЕН: {search_name}",
                f"- Цена: {info['price']} руб.",
                f"- Категория: {info['category']}",
                sep='\n'
            )
        else:
            print(f"❌ '{search_name}' нет в products")

    elif choice == '5':
        # Показ структуры
        print(f"\n👤 USERS ({len(users)}):")

        for uid, data in users.items():
            print(f"   ID {uid}:\n-{data['name']}\n{data['email']}")

        print(f"\n🛒 PRODUCTS ({len(products)}):")
        for name, info in products.items():
            print(f"   Название {name}:\n- {info['price']}р.\n- {info['category']}")

        print(f"\n👀 VISITORS {len(visitors)}: {sorted(visitors)}")

    else:
        if choice == '6':
            print("Вы вышли!")
            break