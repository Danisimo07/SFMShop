def format_product_info(name: str, price:int, quantity: int) -> str:
    return f"Название товара: {product}\n- Цена: {price} руб.;\n- Количество: {quantity}."


info_product = {}
unique_product = set()


while True:
    print(
        "3. Добавить информацию о товаре",
        "2. Просмотреть информацию о товаре",
        "1. Товары",
        "0. Выход",
        sep='\n'
    )

    choice = input("Введите номер раздела (0-3): ")

    if choice == '3':
        try:
            name = input("Введите название: ")

            if name in unique_product:
                print("❌ Товар уже есть в наличии")
            else:
                try:
                    price = int(input("Введите цену на товар: "))
                    quantity = int(input("Введите кол-во товара"))

                    unique_product.add(name)
                    info_product[name] = {
                        "Цена": price,
                        "Кол-во": quantity
                    }
                except ValueError:
                    print("❌ Неверно введены данные")
        except Exception:
            print("❌ Неверно введены данные")
        else:
            print("✅ Обработка данных прошла успешно")

    elif choice == "2":
        name_product = input("Введите название продукта: ").strip()

        if name_product in info_product:
            product = name_product
            price = info_product[name_product]['Цена']
            quantity = info_product[name_product]['Кол-во']

            print(format_product_info(product, price, quantity))
        else:
            print("❌ Такой товар отсутствует")

    elif choice == "1":
        if unique_product:
            lst_products = list(unique_product)
            print(f"Имеющие товары в наличии: {', '.join(sorted(unique_product))}")
        else:
            print("❌ Данные отсутствуют!")

    elif choice == "0":
        print("Выход!")
        break

    else:
        print("❌ Неверный выбор")