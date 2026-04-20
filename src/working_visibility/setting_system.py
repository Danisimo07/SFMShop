BASE_DISCOUNT = 0.1
BASE_DELIVERY_COST = 100
DISCOUNT = BASE_DISCOUNT * 100

def calculate_order_price(price: int, quantity: int) -> float:
    subtotal = price * quantity
    discount = subtotal * BASE_DISCOUNT
    total = subtotal - discount + BASE_DELIVERY_COST
    return total


def update_discount(new_discount: int) -> None:
    global BASE_DISCOUNT
    BASE_DISCOUNT = new_discount

while True:
    try:
        print(
            "2. Расчёт стоимости с учётом базовой скидки",
            "1. Обновление базовой скидки",
            "0. Выход",
            sep='\n'
        )

        choice = input("Введите номер раздела (0-2): \n")

        if choice == '0':
            print("Вы вышли")
            break

        if choice == '2':
            try:
                price = int(input("Введите цену: "))
                quantity = int(input("Введите кол-во: "))
                result = calculate_order_price(price, quantity)
                print(f"Итого {result} руб. (скидка {BASE_DISCOUNT*100:.0f}%)\n")

            except ValueError:
                print("❌ Введите число, а не строку\n")
            else:
                print("✅ Обработка данных прошла успешно!\n")

        if choice == '1':
            try:
                discount = float(input("Новая скидка (0.15): "))
                update_discount(discount)
                print(f"✅ Скидка изменена на {BASE_DISCOUNT*100:.0f}%\n")
            except ValueError:
                print("❌ Введите число\n")
            else:
                print("✅ Обработка данных прошла успешно!\n")
    except ValueError:
        print("❌ Введите строку\n")
