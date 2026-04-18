def validate_user_data(user_data: dict) -> dict:
    result = {}
    errors = []

    # Проверяем name
    try:
        name = user_data.get('name', '')
        if not isinstance(name, str) or len(name.strip()) == 0:
            result['name'] = 'ошибка - не может быть пустым'
            errors.append('name')
        else:
            result["name"] = 'OK'
    except Exception:
        result["name"] = 'ошибка - неверный тип данных'
        errors.append('name')


    # Проверяем age
    try:
        age_str = str(user_data.get('age', ''))
        age = int(age_str)
        if 18 <= age <= 120:
            result['age'] = f"OK ({age})"
        else:
            result["age"] = 'ошибка - возраст должен быть от 18 до 120'
            errors.append('age')
    except (ValueError, TypeError):
        result["age"] = 'ошибка - невозможно преобразовать в число'
        errors.append('age')


    # Проверяем email
    try:
        phone = str(user_data.get('phone', ''))
        # Удаляем пробелы, дефисы, скобки
        clean_phone = ''.join(c for c in phone if c.isdigit())
        if len(clean_phone) > 0:
            result['phone'] = 'OK'
        else:
            result['phone'] = 'ошибка - телефон должен содержать только цифры'
            errors.append('phone')
    except:
        result['phone'] = 'ошибка - неверный тип данных'
        errors.append('phone')

    # Итоговый статус
    result['status'] = 'все поля корректны' if not errors else 'найдены ошибки'

    return result

# Тестовые данные
user_1 = {"name": "Иван Петров", "age": "25", "email": "ivan@sfmshop.ru", "phone": "89001234567"}
user_2 = {"name": "", "age": "молодой", "email": "неверный_email", "phone": "89oo1234567"}


print("Проверка пользователя 1:")
result_1 = validate_user_data(user_1)
for key, value in user_2.items():
    if key != 'status':
        print(f"{key.capitalize()}: {value}")

print(f"Результат: {result_1['status']}\n")


print("Проверка пользователя 2:")
result_2 = validate_user_data(user_2)
for key, value in user_2.items():
    if key != 'status':
        print(f"{key.capitalize()}: {value}")

print(f"Результат: {result_2['status']}")