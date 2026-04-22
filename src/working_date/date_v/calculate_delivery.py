from datetime import datetime, timedelta


def calculate_delivery_date(order_date: datetime, delivery_days: int):
    result = order_date + timedelta(days=delivery_days)
    return result


# try:
#     quantity_delivery_day = int(input("Кол-во дней до доставки: "))
#     # Формирование даты заказа
#     order_date = datetime.now()

#     delivery_date = calculate_delivery_date(order_date, quantity_delivery_day)

#     print(
#         f"\nДата отправки: {order_date.strftime("%Y-%m-%d %H:%M:%S")}",
#         f"Дата доставки: {delivery_date.strftime("%Y-%m-%d")}",
#         sep='\n'
#         )
# except ValueError:
#     print("\n❌ Неправильный ввод ❌")
# except KeyboardInterrupt:
#     print("\n❗ Принудительная остановка ❗")
# else:
#     print("\n✅ Обработка прошла успешно! ✅")
