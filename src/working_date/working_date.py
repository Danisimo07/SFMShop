from datetime import datetime, timedelta

date = datetime.now()
format_date = date.strftime("%Y-%m-%d %H:%M:%S")

order_date = datetime(2026, 4, 22, 10, 0, 0)
format_order = order_date.strftime("%Y-%m-%d %H:%M:%S")

delivery_date = datetime(2026, 4, 25, 10, 0, 0)
format_delyivery = delivery_date.strftime("%Y-%m-%d %H:%M:%S")

difference_date = delivery_date - order_date
difference_day = difference_date.days

print(
    f"Текущее время: {format_date}",
    f"Дата доставки: {format_order}",
    f"Дата доставки: {format_delyivery}",
    f"Дней до доставки: {difference_day}",
    sep='\n'
    )
