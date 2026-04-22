from date_v import calculate_delivery, log_creation
from datetime import datetime


data = {}

while True:
    print(
        "2. Создать заказ",
        "1. Просмотреть информацию по ID",
        "0. Выход",
        sep='\n'
    )

    try:
        choice = int(input("Введите номер раздела (0-2): "))

        match choice:
            case 2:
                try:
                    quantity_delivery_date = int(input("Введите предварительный срок доставки: "))
                    order_id = int(input("Введите ID: "))
                    order_date = datetime.now()

                    delivery_date = calculate_delivery(
                        order_date,
                        quantity_delivery_date
                        )

                    data[order_id] = {
                        'order_date': order_date,
                        'delivery_date': delivery_date
                    }

                    print(
                        f"Дата создания заказа: {order_date}"
                    )
                except ValueError:
                    print("❌ Неверный ввод")
                except KeyboardInterrupt:
                    print("❗Принудительная остановка❗")
                # except Exception:
                #     print("❌ Обработка данных невозможна ❌")
                else:
                    print(log_creation(order_id, order_date))
            case 1:
                try:
                    order_id = int(input("\nВведите свой ID: "))

                    if order_id in data:
                        start_date = data[order_id]['order_date']
                        end_date = data[order_id]['delivery_date']

                        print(
                            f"Дата на начало оформления: {start_date}",
                            f"Дата доставки: {end_date}",
                            sep='\n'
                        )
                    else:
                        print("❌ Такого ID не существует")
                except ValueError:
                    print("❌ Неверный ввод")
                except KeyboardInterrupt:
                    print("❗Принудительная остановка❗")
            case 0:
                print("🚪Вы вышли")
                break
    except ValueError:
        print("❌ Неверный ввод")
    except KeyboardInterrupt:
        print("❗Принудительная остановка❗")
    # except Exception:
    #     print("❌ Обработка данных невозможна ❌")
    else:
        print("\n✅ Обработка данных прошла успешно ✅")
