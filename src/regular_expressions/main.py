from utils.validation import validate_email_regex, validate_phone_regex, clean_input, extract_email_from_text


while True:
    print(
        "\n4. Проверить валидность email",
        "3. Проверить валидность номера телефона: ",
        "2. Очистить текст от ненужных символов: ",
        "1. Извлечь email: ",
        "0. Выход",
        sep="\n"
    )

    try:
        choice = int(input("Введите номер раздела (0-4): "))

        match choice:
            case 4:
                try:
                    email = input("Введите email для проверки: ")

                    if validate_email_regex(email):
                        print("✅ Адрес почты валиден")
                    else:
                        print("❌ Адрес почты не валиден")
                except KeyboardInterrupt:
                    print("\n❗Принудительный выход❗")
                except Exception:
                    print("\n❌ Обработка данных невозможна ❌")

            case 3:
                try:
                    phone_number = input("\nВведите номер телефона для проверки: ")

                    if validate_phone_regex(phone_number):
                        print("\n✅ Номер телефона валиден")
                    else:
                        print("\n❌ Номер телефона не валиден")
                except KeyboardInterrupt:
                    print("\n❗Принудительный выход❗")
                except Exception:
                    print("\n❌ Обработка данных невозможна ❌")
            case 2:
                try:
                    text = input("\nВведите текст для очистки: ")

                    new_text = clean_input(text)
                    print(f"\nОчищенный текст: \"{new_text}\"")
                except KeyboardInterrupt:
                    print("\n❗Принудительный выход❗")
                except Exception:
                    print("\n❌ Обработка данных невозможна ❌")
            case 1:
                try:
                    text = input("\nВведите текст для извлечения email: ")

                    email = extract_email_from_text(text)
                    print(f"\nИзвлечённый email: {email}")
                except KeyboardInterrupt:
                    print("\n❗Принудительный выход❗")
                except Exception:
                    print("\n❌ Обработка данных невозможна ❌")
            case 0:
                print("🚪Вы вышли")
                break
            case _:
                print("\n❌ Неверный ввод")
    except ValueError:
        print("\n❌ Неверный ввод")
    except KeyboardInterrupt:
        print("\n❗Принудительный выход❗")
    except Exception:
        print("\n❌ Обработка данных невозможна ❌")
    else:
        print("\n✅ Обарботка данных прошла успешно")
