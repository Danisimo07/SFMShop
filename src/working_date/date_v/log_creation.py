from datetime import datetime


def log_order_creation(order_id: int, order_time: datetime):
    order_creation = order_time.now()
    return f"✅ Заказ #{order_id} создан: {order_creation.strftime("%Y-%m-%d %H:%M:%S")}"


# try:
#     order_id = int(input("Введите ID: "))

#     order_time = datetime.now()
#     log = log_order_creation(order_id, order_time)
#     print(log)
# except ValueError:
#     print("\n❌ Неверный ввод ❌")
# except KeyboardInterrupt:
#     print("\n❗Принудительная остановка❗")
# else:
#     print("\n✅ Обработка успешно завершена! ✅")
