from utils.calculations import calculate_final_price
from utils.validators import validate_age, validate_email

try:
    age = int(input("Введите возраст: "))
    email = input("Введите почту: ")

    if validate_age(age) and validate_email(email):
        try:
            price = int(input("\nВведите цену: "))
            discount = int(input("Введите скидку на товар: "))
            weight = int(input("Введите вес: "))

            final_price = calculate_final_price(price, discount, weight)
            print(f"Итоговая цена за товар: {final_price} руб.")
        except ValueError:
            print("❌ Введите число, а не строку!")
        else:
            print("✅ Обработка прошла успешно!")
    else:
        print("❌ Вы непрошли проверку!")
except ValueError:
    print("❌ Введите число, а не строку!")
