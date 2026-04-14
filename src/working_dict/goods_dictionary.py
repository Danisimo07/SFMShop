products = {
    "name": [],
    "price": [],
    "quantity": []
}

name_menu = "Меню"

print(
    f"{name_menu:^20}",
    "1. Добавить товар",
    "2. Показать общее кол-во товаров",
    "3. Удалить товар",
    "4. Выход",
    sep='\n'
)

while True:
    # Пользователь вводит номер раздела
    choice = input("Введите номер раздела (1-4): ")

    # Добавление товара
    if choice == "1":
        """
            Чтобы добавить товар нужно ответить на вопрос ->
        Что именно должен в себя включать данный раздел
        """
        name = input("Название товара: ")
        price = int(input("Введите цену товара: "))
        quantity = int(input("Кол-во товаров: "))

        # Добавление товаров и его характеристик по ключу
        products["name"].append(name)
        products["price"].append(price)
        products["quantity"].append(quantity)
        # Вывод результата успешного добавления товара
        print("✅ Товар был успешно добавлен!")

    elif choice == "2":
        # Предпологаем, что в данном разделе отсутствуют товары
        if not products["quantity"]:
            print("❌ По данному запросу ничего не найдено!")
            continue
        # Если товары присутствуют, то можно выделить категории определённых товаров и посчитать их кол-во
        category_total = {}

        for i in range(len(products["name"])):
            name = products["name"][i]
            quiantity = products["quantity"][i]

            if name in category_total:
                category_total[name] += quantity
            else:
                category_total[name] = quantity

        # Выводим результат
        print("📊 Кол-во товаров по их категориям:")
        for name, total_qty in category_total.items():
            print(f"- {name}: {total_qty} шт.")

    elif choice == "3":
        if not products["name"]:
            print("❌ По данному запросу ничего не найдено!")
            continue

        # Показываем текущие товары на складе
        for i in range(len(products["name"])):
            print(f"{i+1}. {products['name'][i]} - {products['price'][i]}")

        try:
            num = int(input("Номер товара для удаления (1-{}): ".format((len(products['name']))))) - 1

            if 0 <= num < len(products['name']):
                # Удаляем из всех списков по одному индексу
                removed_name = products["name"].pop(num)
                removed_price = products["price"].pop(num)
                removed_quantity = products["quantity"].pop(num)

                # Вывод результата удаления товаров по запросу
                print(
                    "🗑️ Удалён:",
                    f"- Название товара: {removed_name};",
                    f"- Цена: {removed_price}р.;",
                    f"- Кол-во: {removed_quantity} шт.",
                    f"Скалд: {len(products['name'])} товаров осталось.",
                    sep='\n'
                )
            else:
                print("❌ Неверный номер!")
        except ValueError:
            print("❌ Введите число!")

    elif choice == "4":
        print("Вы вышли.")
        break

    else:
        print("❌ Неверный выбор!")
