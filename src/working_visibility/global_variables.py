DISCOUNT_RATE = 0.1
DISCOUNT = str(DISCOUNT_RATE * 100) + "%"

def calculate_price_with_discount(price: int) -> float:
    global DISCOUNT_RATE
    if DISCOUNT_RATE <= 1:
        DISCOUNT_RATE += 0.1
    discount_price = price * (1 - DISCOUNT_RATE)
    return round(discount_price, 2)

while True:
    try:
        price = int(input("Введите цену на товар: "))
        # Вывод
        print(f"Цена со скидкой {DISCOUNT}: {calculate_price_with_discount(price)}")
    except ValueError:
        print(
            "❌ Возникли проблема с обработкой данных",
            "Попробуйте ещё раз!",
            sep='\n'
        )
    else:
        print("✅ Обработка данных прошла успешно!")